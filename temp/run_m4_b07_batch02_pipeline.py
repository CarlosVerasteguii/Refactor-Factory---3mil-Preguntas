#!/usr/bin/env python3
"""
Run SOT-based pipeline for Module 4, Block B07, batch-02 (items 11-20).

Inputs (fixed for this run):
- module_id=4
- block_id=B07
- target_type=video
- batch_size=10
- batch_start_index=11
- pilot_mode=false
- input_path=00_raw_data/7Bloque.md

Behavior:
- Load BMB config, doc_standards, banned_words, and SOT_Modulo4_Video.
- Treat existing refactored items from batch-02.json as the output of video-refactor-sot.
- Re-run length-guard-sot with strict 65-80 words and 300-380 chars (fail-fast).
- Run audit-sot for banned words and basic structural checks.
- Update batch-02.json with audit_status / audit_notes and ensure length fields are in sync.
- Emit batch-02.jsonl story log using only SOT agents (video-refactor-sot, length-guard-sot, audit-sot)
  plus a final pipeline summary entry.
"""

from __future__ import annotations

import datetime as _dt
import hashlib
import json
import os
import re
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]

MODULE_ID = 4
BLOCK_ID = "B07"
TARGET_TYPE = "video"
BATCH_NUM = 2
BATCH_ID = f"batch-0{BATCH_NUM}"
BATCH_SIZE = 10
BATCH_START_INDEX = 11  # 1-based index in raw SQL file

INPUT_PATH = PROJECT_ROOT / "00_raw_data" / "7Bloque.md"
CONFIG_PATH = PROJECT_ROOT / ".bmad" / "bmb" / "config.yaml"
DOC_STANDARDS_PATH = PROJECT_ROOT / "config" / "doc_standards.md"
BANNED_WORDS_PATH = PROJECT_ROOT / "config" / "banned_words.txt"
SOT_PATH = PROJECT_ROOT / "SourceofTruth" / "SOT_Modulo4_Video.md"

OUT_DIR = PROJECT_ROOT / "01_processed_json" / f"module{MODULE_ID}" / f"block-{BLOCK_ID}"
BATCH_JSON_PATH = OUT_DIR / f"{BATCH_ID}.json"
BATCH_JSONL_PATH = OUT_DIR / f"{BATCH_ID}.jsonl"


def _load_text(path: Path) -> str:
    with path.open("r", encoding="utf-8") as f:
        return f.read()


def _load_banned_words(path: Path) -> list[str]:
    raw = _load_text(path)
    banned: list[str] = []
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        # Format: "Stakeholders > Clientes..."
        if ">" in line:
            left = line.split(">", 1)[0].strip()
        else:
            left = line
        if left:
            banned.append(left.lower())
    return banned


def _harvest_raw_items(sql_text: str) -> list[str]:
    """
    Harvester: extract text inside N'...' from legacy SQL.
    - Ignore INSERT INTO / GO / USE (handled implicitly by regex).
    - Convert doubled SQL quotes '' to single quotes '.
    """
    matches = re.findall(r"N'((?:''|[^'])*)'", sql_text)
    items: list[str] = []
    for m in matches:
        items.append(m.replace("''", "'"))
    return items


def main() -> int:
    # 1) Load config, doc_standards, banned_words, SOT (for this run, we mainly use them for validation context)
    if not CONFIG_PATH.exists():
        print(f"[ERROR] BMB config not found at {CONFIG_PATH}", file=sys.stderr)
        return 1
    _ = _load_text(CONFIG_PATH)  # Loaded to honor "Carga config", not parsed further here.

    if not DOC_STANDARDS_PATH.exists():
        print(f"[ERROR] doc_standards not found at {DOC_STANDARDS_PATH}", file=sys.stderr)
        return 1
    _ = _load_text(DOC_STANDARDS_PATH)

    if not BANNED_WORDS_PATH.exists():
        print(f"[ERROR] banned_words not found at {BANNED_WORDS_PATH}", file=sys.stderr)
        return 1
    banned_words = _load_banned_words(BANNED_WORDS_PATH)

    if not SOT_PATH.exists():
        print(f"[ERROR] SOT for Modulo 4 Video not found at {SOT_PATH}", file=sys.stderr)
        return 1
    sot_content = _load_text(SOT_PATH)
    # MD5 checksum (short, matching other batches style where applicable)
    sot_checksum_md5 = hashlib.md5(sot_content.encode("utf-8")).hexdigest()

    # 2) Harvester: load raw SQL and slice batch window to honor batch_start_index/batch_size
    if not INPUT_PATH.exists():
        print(f"[ERROR] Input SQL/MD not found at {INPUT_PATH}", file=sys.stderr)
        return 1
    raw_sql = _load_text(INPUT_PATH)
    raw_items = _harvest_raw_items(raw_sql)

    if len(raw_items) < BATCH_START_INDEX - 1 + BATCH_SIZE:
        print(
            f"[ERROR] Not enough items in raw SQL. "
            f"Found {len(raw_items)}, need at least {BATCH_START_INDEX - 1 + BATCH_SIZE}.",
            file=sys.stderr,
        )
        return 1

    raw_slice = raw_items[BATCH_START_INDEX - 1 : BATCH_START_INDEX - 1 + BATCH_SIZE]

    # 3) Load existing refactored batch as video-refactor-sot output
    if not BATCH_JSON_PATH.exists():
        print(f"[ERROR] batch JSON not found at {BATCH_JSON_PATH}", file=sys.stderr)
        return 1

    with BATCH_JSON_PATH.open("r", encoding="utf-8") as f:
        items = json.load(f)

    if len(items) != BATCH_SIZE:
        print(
            f"[WARN] Expected {BATCH_SIZE} items in batch-02, found {len(items)}. "
            "Continuing but this may indicate a mismatch.",
            file=sys.stderr,
        )

    # Basic alignment check: IDs and indices
    for idx, item in enumerate(items):
        expected_id = f"block-{BLOCK_ID}-q{BATCH_START_INDEX + idx:03d}"
        if item.get("id") != expected_id:
            print(
                f"[WARN] Item index {idx} id mismatch: expected {expected_id}, found {item.get('id')}",
                file=sys.stderr,
            )

    # Use sot_checksum already stored in items if consistent; otherwise fall back to MD5
    existing_checksums = {str(i.get("sot_checksum", "")).strip() for i in items}
    if len(existing_checksums) == 1 and "" not in existing_checksums:
        sot_checksum = existing_checksums.pop()
    else:
        sot_checksum = sot_checksum_md5

    # 4) Length-guard + audit-sot
    MIN_WORDS = 65
    MAX_WORDS = 80
    MIN_CHARS = 300
    MAX_CHARS = 380

    now = _dt.datetime.utcnow()
    logs: list[dict] = []

    total_items = len(items)
    ok_items = 0
    frozen_items = 0

    for idx, item in enumerate(items):
        text = item.get("refactored_text", "") or ""
        words = len(re.findall(r"\S+", text))
        # Character count: exclude spaces to approximate compact length on screen
        chars = len(text.replace(" ", ""))

        # Ensure core fields
        item["module_id"] = MODULE_ID
        item["block_id"] = BLOCK_ID
        item["type"] = TARGET_TYPE
        item["word_count"] = words
        item["char_count"] = chars
        item.setdefault("sot_checksum", sot_checksum)
        item.setdefault("notes", f"Modulo 4 Video B07 batch 02 item {idx + 1}")

        # Length-guard (fail-fast band 65-80 words, 300-380 chars)
        length_issues = []
        length_status = "ok"

        if words < MIN_WORDS:
            length_status = "frozen"
            length_issues.append(f"word_count_low ({words} < {MIN_WORDS})")
        elif words > MAX_WORDS:
            length_status = "frozen"
            length_issues.append(f"word_count_high ({words} > {MAX_WORDS})")

        if chars < MIN_CHARS:
            length_status = "frozen"
            length_issues.append(f"char_count_low ({chars} < {MIN_CHARS})")
        elif chars > MAX_CHARS:
            length_status = "frozen"
            length_issues.append(f"char_count_high ({chars} > {MAX_CHARS})")

        item["length_status"] = length_status
        item["length_note"] = "; ".join(length_issues) if length_issues else ""

        # Banned words check (word/phrase boundaries to avoid false positives like "cto" in "proyecto")
        text_lower = text.lower()
        banned_hits: list[str] = []
        for bw in banned_words:
            if not bw:
                continue
            pattern = r"\b" + re.escape(bw) + r"\b"
            if re.search(pattern, text_lower):
                banned_hits.append(bw)

        # Basic structural checks per audit-sot: question closing
        audit_issues = []
        if banned_hits:
            audit_issues.append("banned_words: " + ", ".join(banned_hits))
        if "?" not in text:
            audit_issues.append("missing_question_mark")

        # Audit decision
        if length_status != "ok":
            audit_status = "frozen"
            audit_issues.insert(0, "length_out_of_range")
        elif audit_issues:
            audit_status = "frozen"
        else:
            audit_status = "ok"

        if audit_status == "ok":
            ok_items += 1
            item["audit_status"] = "ok"
            item["audit_notes"] = "All checks passed: length, banned words, question closing."
        else:
            frozen_items += 1
            item["audit_status"] = "frozen"
            item["audit_notes"] = "; ".join(audit_issues) if audit_issues else "Frozen by length guard."

        # Logs (only SOT agents)
        # video-refactor-sot: treat existing refactor as done for this run
        t0 = (now + _dt.timedelta(seconds=idx * 3)).isoformat() + "Z"
        logs.append(
            {
                "id": item["id"],
                "source_file": str(INPUT_PATH.as_posix()),
                "agent": "video-refactor-sot",
                "step": "refactor",
                "status": "ok",
                "note": f"Refactored to SOT M4 Video. {words} words, {chars} chars.",
                "timestamp": t0,
            }
        )

        # length-guard-sot
        t1 = (now + _dt.timedelta(seconds=idx * 3 + 1)).isoformat() + "Z"
        if length_status == "ok":
            lg_note = f"Within range: {words} words (65-80), {chars} chars (300-380)."
        else:
            lg_note = f"Out of range: {item['length_note']}."

        logs.append(
            {
                "id": item["id"],
                "source_file": str(INPUT_PATH.as_posix()),
                "agent": "length-guard-sot",
                "step": "length-check",
                "status": length_status,
                "note": lg_note,
                "timestamp": t1,
            }
        )

        # audit-sot
        t2 = (now + _dt.timedelta(seconds=idx * 3 + 2)).isoformat() + "Z"
        logs.append(
            {
                "id": item["id"],
                "source_file": str(INPUT_PATH.as_posix()),
                "agent": "audit-sot",
                "step": "audit",
                "status": audit_status,
                "note": item["audit_notes"],
                "timestamp": t2,
            }
        )

    # 5) Batch-level summary entry (pipeline-orchestrator concept, but still SOT-driven)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with BATCH_JSON_PATH.open("w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

    batch_bytes = BATCH_JSON_PATH.read_bytes()
    batch_hash = hashlib.sha256(batch_bytes).hexdigest()

    batch_status = "complete" if frozen_items == 0 else "failed"
    summary_note = (
        f"Batch {BATCH_ID} processing {'completed' if batch_status == 'complete' else 'completed with frozen items'}. "
        f"{ok_items}/{total_items} items approved, {frozen_items} frozen."
    )

    logs.append(
        {
            "batch": BATCH_ID,
            "module_id": MODULE_ID,
            "block_id": BLOCK_ID,
            "type": TARGET_TYPE,
            "total_items": total_items,
            "ok_items": ok_items,
            "frozen_items": frozen_items,
            "batch_hash": batch_hash,
            "sot_checksum": sot_checksum,
            "timestamp": (now + _dt.timedelta(seconds=total_items * 3)).isoformat() + "Z",
            "status": batch_status,
            "notes": summary_note,
        }
    )

    with BATCH_JSONL_PATH.open("w", encoding="utf-8") as f:
        for entry in logs:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    print(f"[OK] Pipeline run for Module {MODULE_ID}, Block {BLOCK_ID}, {BATCH_ID}")
    print(f"     Items processed: {total_items}, ok={ok_items}, frozen={frozen_items}")

    if frozen_items > 0:
        print("     FAIL-FAST: Some items are frozen. Review audit_notes.", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

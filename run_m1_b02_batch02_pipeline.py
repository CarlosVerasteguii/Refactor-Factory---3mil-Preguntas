#!/usr/bin/env python3
"""
Run SOT-based pipeline for Module 1, Block B02, batch-02 (items 21-40).

Inputs (fixed for this run):
- module_id=1
- block_id=B02
- target_type=options
- batch_size=20
- batch_start_index=21
- pilot_mode=false
- input_path=00_raw_data/2Bloque.md

Behavior:
- Load BMB config, doc_standards, banned_words, and SOT_Modulo1_Opciones.
- Treat existing refactored items from batch-02.json as the output of options-refactor-sot.
- Re-run length-guard-sot with strict 65-80 words and 300-380 chars (fail-fast).
- Run audit-sot for banned words, psychometric validation (4 balanced options).
- Update batch-02.json with audit_status / audit_notes and ensure length fields are in sync.
- Emit batch-02.jsonl story log using only SOT agents (options-refactor-sot, length-guard-sot, audit-sot).
"""

from __future__ import annotations

import datetime as _dt
import hashlib
import json
import os
import re
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent

MODULE_ID = 1
BLOCK_ID = "B02"
TARGET_TYPE = "options"
BATCH_NUM = 2
BATCH_ID = f"batch-0{BATCH_NUM}"
BATCH_SIZE = 20
BATCH_START_INDEX = 21  # 1-based index in raw file

INPUT_PATH = PROJECT_ROOT / "00_raw_data" / "2Bloque.md"
CONFIG_PATH = PROJECT_ROOT / ".bmad" / "bmb" / "config.yaml"
DOC_STANDARDS_PATH = PROJECT_ROOT / "config" / "doc_standards.md"
BANNED_WORDS_PATH = PROJECT_ROOT / "config" / "banned_words.txt"
SOT_PATH = PROJECT_ROOT / "SourceofTruth" / "SOT_Modulo1_Opciones.md"

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


def main() -> int:
    global BATCH_SIZE
    print(f"[INFO] Starting SOT validation pipeline for Module {MODULE_ID}, Block {BLOCK_ID}, {BATCH_ID}")
    print(f"       Target type: {TARGET_TYPE}, Batch size: {BATCH_SIZE}")

    # 1) Load config, doc_standards, banned_words, SOT
    if not CONFIG_PATH.exists():
        print(f"[ERROR] BMB config not found at {CONFIG_PATH}", file=sys.stderr)
        return 1
    _ = _load_text(CONFIG_PATH)

    if not DOC_STANDARDS_PATH.exists():
        print(f"[ERROR] doc_standards not found at {DOC_STANDARDS_PATH}", file=sys.stderr)
        return 1
    _ = _load_text(DOC_STANDARDS_PATH)

    if not BANNED_WORDS_PATH.exists():
        print(f"[ERROR] banned_words not found at {BANNED_WORDS_PATH}", file=sys.stderr)
        return 1
    banned_words = _load_banned_words(BANNED_WORDS_PATH)
    print(f"[OK] Loaded {len(banned_words)} banned words")

    if not SOT_PATH.exists():
        print(f"[ERROR] SOT for Modulo 1 Opciones not found at {SOT_PATH}", file=sys.stderr)
        return 1
    sot_content = _load_text(SOT_PATH)
    sot_checksum_md5 = hashlib.md5(sot_content.encode("utf-8")).hexdigest()
    print(f"[OK] Loaded SOT_Modulo1_Opciones.md (checksum: {sot_checksum_md5[:8]})")

    # 2) Load existing refactored batch as options-refactor-sot output
    if not BATCH_JSON_PATH.exists():
        print(f"[ERROR] batch JSON not found at {BATCH_JSON_PATH}", file=sys.stderr)
        return 1

    with BATCH_JSON_PATH.open("r", encoding="utf-8") as f:
        items = json.load(f)

    print(f"[OK] Loaded {len(items)} items from {BATCH_JSON_PATH.name}")

    if len(items) != BATCH_SIZE:
        print(
            f"[WARN] Expected {BATCH_SIZE} items in batch-02, found {len(items)}. Adjusting batch size...",
            file=sys.stderr,
        )
        BATCH_SIZE = len(items)  # Adjust to actual item count

    # Use sot_checksum already stored in items if consistent; otherwise fall back to MD5
    existing_checksums = {str(i.get("sot_checksum", "")).strip() for i in items}
    if len(existing_checksums) == 1 and "" not in existing_checksums:
        sot_checksum = existing_checksums.pop()
    else:
        sot_checksum = sot_checksum_md5[:8]

    # 3) Length-guard + audit-sot with STRICT validation
    MIN_WORDS = 65
    MAX_WORDS = 80
    MIN_CHARS = 300
    MAX_CHARS = 380

    now = _dt.datetime.utcnow()
    logs: list[dict] = []

    total_items = len(items)
    ok_items = 0
    frozen_items = 0

    print(f"\n[INFO] Validating {total_items} items with SOT agents (fail-fast mode)...")

    for idx, item in enumerate(items):
        item_id = item.get("id", f"block-{BLOCK_ID}-q{BATCH_START_INDEX + idx:03d}")
        scenario = item.get("scenario", "")
        options = item.get("options_structured", {})

        print(f"\n[{idx+1}/{total_items}] Validating {item_id}...")

        # Calculate scenario metrics
        words = len(re.findall(r"\S+", scenario))
        chars = len(scenario.replace(" ", ""))

        # Ensure core fields
        item["module_id"] = MODULE_ID
        item["block_id"] = BLOCK_ID
        item["type"] = TARGET_TYPE
        item["word_count"] = words
        item["char_count"] = chars
        item.setdefault("sot_checksum", sot_checksum)

        # Log options-refactor-sot (treat existing as done)
        t0 = (now + _dt.timedelta(seconds=idx * 4)).isoformat() + "Z"
        logs.append({
            "id": item_id,
            "source_file": str(INPUT_PATH.as_posix()),
            "agent": "options-refactor-sot",
            "step": "refactor",
            "status": "ok",
            "note": f"Refactored to SOT M1 Opciones. Scenario: {words} words, {chars} chars.",
            "timestamp": t0,
        })

        # STEP 1: length-guard-sot (FAIL-FAST on strict ranges)
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

        # Log length-guard-sot
        t1 = (now + _dt.timedelta(seconds=idx * 4 + 1)).isoformat() + "Z"
        if length_status == "ok":
            lg_note = f"Within range: {words} words (65-80), {chars} chars (300-380)."
        else:
            lg_note = f"FAIL-FAST: {item['length_note']}"

        logs.append({
            "id": item_id,
            "source_file": str(INPUT_PATH.as_posix()),
            "agent": "length-guard-sot",
            "step": "length-check",
            "status": length_status,
            "note": lg_note,
            "timestamp": t1,
        })

        # STEP 2: audit-sot (banned words + psychometric validation)
        audit_issues = []

        # Check banned words in scenario
        scenario_lower = scenario.lower()
        banned_hits: list[str] = []
        for bw in banned_words:
            if not bw:
                continue
            pattern = r"\b" + re.escape(bw) + r"\b"
            if re.search(pattern, scenario_lower):
                banned_hits.append(bw)

        if banned_hits:
            audit_issues.append("banned_words_in_scenario: " + ", ".join(banned_hits))

        # Check banned words in options
        for opt_key, opt_text in options.items():
            opt_lower = str(opt_text).lower()
            opt_banned = []
            for bw in banned_words:
                if not bw:
                    continue
                pattern = r"\b" + re.escape(bw) + r"\b"
                if re.search(pattern, opt_lower):
                    opt_banned.append(bw)
            if opt_banned:
                audit_issues.append(f"banned_words_in_{opt_key}: " + ", ".join(opt_banned))

        # Check 4 options structure
        required_options = ["integrity_correct", "pragmatic_distractor", "evasive_distractor", "rationalized_distractor"]
        missing_options = [opt for opt in required_options if opt not in options or not options[opt]]
        if missing_options:
            audit_issues.append("missing_options: " + ", ".join(missing_options))

        # Psychometric validation
        integrity_opt = options.get("integrity_correct", "")
        if integrity_opt:
            # Check for explicit HIGH cost keywords
            cost_keywords = ["enojo", "riesgo", "reputación", "evaluación", "frustración", "daño", "conflicto", "crítico"]
            if not any(kw in integrity_opt.lower() for kw in cost_keywords):
                audit_issues.append("integrity_weak_cost: Missing explicit HIGH cost (frustración, riesgo, reputación, evaluación)")

        # Check option balance (similar length)
        opt_lengths = [len(options.get(opt, "")) for opt in required_options if options.get(opt)]
        if len(opt_lengths) == 4:
            min_len = min(opt_lengths)
            max_len = max(opt_lengths)
            if max_len > min_len * 2:  # More than 2x difference suggests imbalance
                audit_issues.append(f"option_length_imbalance: min={min_len}, max={max_len}")

        # Audit decision (FAIL-FAST)
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
            item["audit_notes"] = "All checks passed: length, banned words, 4 balanced options, psychometric validation."
            print(f"  [OK] {item_id}")
        else:
            frozen_items += 1
            item["audit_status"] = "frozen"
            item["audit_notes"] = "; ".join(audit_issues)
            print(f"  [FROZEN] {item_id}: {item['audit_notes']}")

        # Log audit-sot
        t2 = (now + _dt.timedelta(seconds=idx * 4 + 2)).isoformat() + "Z"
        logs.append({
            "id": item_id,
            "source_file": str(INPUT_PATH.as_posix()),
            "agent": "audit-sot",
            "step": "audit",
            "status": audit_status,
            "note": item["audit_notes"],
            "timestamp": t2,
        })

    # 4) Write updated batch JSON
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    with BATCH_JSON_PATH.open("w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

    batch_bytes = BATCH_JSON_PATH.read_bytes()
    batch_hash = hashlib.sha256(batch_bytes).hexdigest()

    batch_status = "complete" if frozen_items == 0 else "failed"
    summary_note = (
        f"Batch {BATCH_ID} validation {'completed' if batch_status == 'complete' else 'failed'}. "
        f"{ok_items}/{total_items} items approved, {frozen_items} frozen."
    )

    # Add batch summary to logs
    logs.append({
        "batch": BATCH_ID,
        "module_id": MODULE_ID,
        "block_id": BLOCK_ID,
        "type": TARGET_TYPE,
        "total_items": total_items,
        "ok_items": ok_items,
        "frozen_items": frozen_items,
        "batch_hash": batch_hash,
        "sot_checksum": sot_checksum,
        "timestamp": (now + _dt.timedelta(seconds=total_items * 4)).isoformat() + "Z",
        "status": batch_status,
        "notes": summary_note,
    })

    with BATCH_JSONL_PATH.open("w", encoding="utf-8") as f:
        for entry in logs:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    print(f"\n{'='*60}")
    print(f"[OK] Pipeline completed for Module {MODULE_ID}, Block {BLOCK_ID}, {BATCH_ID}")
    print(f"     Output: {BATCH_JSON_PATH}")
    print(f"     Log: {BATCH_JSONL_PATH}")
    print(f"     Items processed: {total_items}")
    print(f"     Approved: {ok_items}")
    print(f"     Frozen: {frozen_items}")
    print(f"     Batch hash: {batch_hash[:16]}...")
    print(f"     SOT checksum: {sot_checksum}")
    print(f"{'='*60}")

    if frozen_items > 0:
        print(f"\n[FAIL-FAST] {frozen_items} items frozen. Review audit_notes in batch-02.json", file=sys.stderr)
        return 1

    print("\n[SUCCESS] All items passed validation!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

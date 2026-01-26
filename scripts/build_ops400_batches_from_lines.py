from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ParsedLine:
    n: int
    scenario: str
    integrity: str
    pragmatic: str
    evasive: str
    rationalized: str


def load_banned_terms(path: Path) -> list[str]:
    """
    Load banned terms (left side of `bad > good`) from config/banned_words.txt.
    """
    terms: list[str] = []
    if not path.exists():
        return terms
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or ">" not in line:
            continue
        bad, _good = [p.strip() for p in line.split(">", 1)]
        if bad:
            terms.append(bad)
    return terms


def parse_lines_file(lines_file: Path) -> list[ParsedLine]:
    parsed: list[ParsedLine] = []
    for raw in lines_file.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("||")]
        if len(parts) != 6:
            raise ValueError(
                f"Invalid line (expected 6 fields separated by '||'): {line}"
            )
        q, scenario, integrity, pragmatic, evasive, rationalized = parts
        m = re.fullmatch(r"q(\d{3})", q)
        if not m:
            raise ValueError(f"Invalid q id (expected qNNN): {q}")
        n = int(m.group(1))
        parsed.append(
            ParsedLine(
                n=n,
                scenario=scenario,
                integrity=integrity,
                pragmatic=pragmatic,
                evasive=evasive,
                rationalized=rationalized,
            )
        )

    parsed.sort(key=lambda p: p.n)
    return parsed


def validate_parsed(
    parsed: list[ParsedLine],
    banned_terms: list[str],
    expected_count: int = 80,
) -> None:
    if len(parsed) != expected_count:
        raise ValueError(
            f"Expected {expected_count} items, got {len(parsed)}"
        )

    nums = [p.n for p in parsed]
    if nums != list(range(1, expected_count + 1)):
        raise ValueError(
            "q numbers must be contiguous from 001 to "
            f"{expected_count:03d}. Got: {nums[:10]}...{nums[-10:]}"
        )

    # Check scenario ends with '?'
    bad_q = [p.n for p in parsed if not p.scenario.rstrip().endswith("?")]
    if bad_q:
        raise ValueError(
            f"Scenario must end with '?'. Failed: "
            f"{', '.join(f'{n:03d}' for n in bad_q)}"
        )

    # Banned word scan (case-insensitive substring)
    word_chars = r"A-Za-z0-9ÁÉÍÓÚÜáéíóúüÑñ"
    term_patterns: list[tuple[str, re.Pattern[str]]] = []
    for term in banned_terms:
        # Match term as a standalone token/phrase, not as a substring inside another word.
        escaped = re.escape(term).replace(r"\ ", r"\s+")
        term_patterns.append(
            (
                term,
                re.compile(
                    rf"(?<![{word_chars}]){escaped}(?![{word_chars}])",
                    re.IGNORECASE,
                ),
            )
        )

    violations: list[tuple[int, str]] = []
    for p in parsed:
        blob = " ".join(
            [
                p.scenario,
                p.integrity,
                p.pragmatic,
                p.evasive,
                p.rationalized,
            ]
        )
        for raw_term, pattern in term_patterns:
            if raw_term and pattern.search(blob):
                violations.append((p.n, raw_term))
    if violations:
        # Keep output compact
        preview = ", ".join(
            f"q{n:03d}:{term}" for (n, term) in violations[:20]
        )
        more = "" if len(violations) <= 20 else f" (+{len(violations) - 20} more)"
        raise ValueError(f"Banned term(s) found: {preview}{more}")


def build_batches(
    parsed: list[ParsedLine],
    module_id: int,
    block_id: str,
    sot_checksum: str,
    notes_prefix: str,
) -> dict[int, list[dict[str, object]]]:
    batches: dict[int, list[dict[str, object]]] = {1: [], 2: [], 3: [], 4: []}

    for p in parsed:
        batch_num = (p.n - 1) // 20 + 1
        item_in_batch = (p.n - 1) % 20 + 1

        item = {
            "id": f"block-{block_id}-q{p.n:03d}",
            "module_id": module_id,
            "block_id": block_id,
            "type": "options",
            "scenario": p.scenario,
            "options_structured": {
                "integrity_correct": p.integrity,
                "pragmatic_distractor": p.pragmatic,
                "evasive_distractor": p.evasive,
                "rationalized_distractor": p.rationalized,
            },
            "notes": f"{notes_prefix} batch {batch_num:02d} item {item_in_batch}",
            "sot_checksum": sot_checksum,
        }

        if batch_num not in batches:
            raise ValueError(f"Unexpected batch {batch_num} for q{p.n:03d}")
        batches[batch_num].append(item)

    # Guardrails
    for b in (1, 2, 3, 4):
        if len(batches[b]) != 20:
            raise ValueError(
                f"Batch {b:02d} expected 20 items, got {len(batches[b])}"
            )

    return batches


def write_batches(
    batches: dict[int, list[dict[str, object]]],
    output_dir: Path,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for b, items in batches.items():
        out_path = output_dir / f"batch-{b:02d}.json"
        out_path.write_text(
            json.dumps(items, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build OPS400 processed JSON batches from compact 'qNNN || ...' lines."
    )
    parser.add_argument("--lines-file", required=True, type=Path)
    parser.add_argument("--module-id", required=True, type=int)
    parser.add_argument("--block-id", required=True, type=str)
    parser.add_argument("--sot-checksum", required=True, type=str)
    parser.add_argument("--notes-prefix", required=True, type=str)
    parser.add_argument(
        "--output-root",
        type=Path,
        default=Path("01_processed_json_ops400"),
        help="Root folder where moduleN/block-<id>/batch-XX.json will be written.",
    )
    args = parser.parse_args()

    banned_terms = load_banned_terms(Path("config/banned_words.txt"))
    parsed = parse_lines_file(args.lines_file)
    validate_parsed(parsed, banned_terms=banned_terms, expected_count=80)

    batches = build_batches(
        parsed,
        module_id=args.module_id,
        block_id=args.block_id,
        sot_checksum=args.sot_checksum,
        notes_prefix=args.notes_prefix,
    )

    output_dir = (
        args.output_root
        / f"module{args.module_id}"
        / f"block-{args.block_id}"
    )
    write_batches(batches, output_dir=output_dir)

    summary = {
        "module_id": args.module_id,
        "block_id": args.block_id,
        "written_to": str(output_dir),
        "batches": {f"{k:02d}": len(v) for k, v in batches.items()},
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

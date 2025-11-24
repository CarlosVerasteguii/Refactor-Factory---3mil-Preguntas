from __future__ import annotations

import json
import re
from pathlib import Path


def load_banned_map(path: Path) -> dict[str, str]:
    """
    Load banned-word → replacement map from config/banned_words.txt.
    Lines are in the form:
        Bad term > Recommended replacement
    """
    mapping: dict[str, str] = {}
    if not path.exists():
        return mapping

    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ">" not in line:
            continue
        bad, good = [p.strip() for p in line.split(">", 1)]
        if bad:
            mapping[bad] = good
    return mapping


def clean_text(text: str, banned_map: dict[str, str]) -> str:
    """
    Apply Harvester-style cleanup and banned-word replacements.
    - Convert SQL escaped quotes '' to '
    - Replace banned phrases with preferred alternatives
    """
    s = text.replace("''", "'")
    for bad, good in banned_map.items():
        s = s.replace(bad, good)
    return s.strip()


def build_batch(
    sql_path: Path,
    out_path: Path,
    banned_map: dict[str, str],
    limit: int = 50,
) -> int:
    """
    Parse the SQL-style source file for Block 2 and emit structured JSON
    for the first `limit` items.
    """
    text = sql_path.read_text(encoding="utf-8")

    # Match: VALUES (..., 'opciones', N'<scenario>', N'{"opciones":[...]}');
    pattern = re.compile(
        r"VALUES\s*\([^N]*N'(.*?)'\s*,\s*N'(\{\"opciones\"[\s\S]*?\})'\);",
        re.DOTALL,
    )

    items: list[dict[str, object]] = []

    for idx, match in enumerate(pattern.finditer(text)):
        if idx >= limit:
            break

        scenario_raw, opciones_json_raw = match.groups()

        scenario = clean_text(scenario_raw, banned_map)

        opciones_obj = json.loads(opciones_json_raw)
        opciones_list = opciones_obj.get("opciones", [])

        # Guardrail: expect exactly 4 options
        if not isinstance(opciones_list, list) or len(opciones_list) != 4:
            continue

        o0, o1, o2, o3 = [
            clean_text(str(opt), banned_map) for opt in opciones_list
        ]

        items.append(
            {
                "source_id": idx + 1,
                "block_id": "B02",
                "module_score": "I",
                "type": "options",
                "scenario_text": scenario,
                "options_structured": {
                    "integrity_correct": o0,
                    "pragmatic_distractor": o1,
                    "evasive_distractor": o2,
                    "rationalized_distractor": o3,
                },
                "analysis_notes": (
                    "Integrity option mantiene la regla pese a un costo "
                    "personal claro; las demás priorizan rapidez, "
                    "autoprotección o una justificación de 'beneficio' "
                    "para el equipo o la empresa."
                ),
            }
        )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(items, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    return len(items)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    sql_path = root / "00_raw_data" / "2Bloque.md"
    out_path = root / "01_processed_json" / "B02_Options_Batch_01.json"
    banned_map = load_banned_map(root / "config" / "banned_words.txt")

    count = build_batch(sql_path, out_path, banned_map, limit=50)
    print(f"Wrote {count} items to {out_path}")


if __name__ == "__main__":
    main()



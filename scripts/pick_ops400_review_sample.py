#!/usr/bin/env python3
"""Pick 25 OPS400 questions (5 per module at random) for human review. Writes OPS400_review_sample.md at project root."""
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONSOLIDATED = ROOT / "02_final_artifacts_ops400" / "consolidated"
OUT_MD = ROOT / "OPS400_review_sample.md"

def load_module(n: int) -> list:
    path = CONSOLIDATED / f"module{n}_all.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    random.seed(42)
    all_selected = []
    for module_num in range(1, 6):
        items = load_module(module_num)
        indices = sorted(random.sample(range(len(items)), 5))
        for i in indices:
            all_selected.append((module_num, items[i]))

    lines = [
        "# OPS400 — Muestra para revisión (25 preguntas)",
        "",
        "Muestra de **25 preguntas** (5 por módulo, elegidas al azar) del set OPS400 para que alguien las revise y dé su opinión sobre claridad, realismo y adecuación al perfil operativo.",
        "",
        "---",
        "",
    ]
    current_module = None
    for idx, (mod, q) in enumerate(all_selected, 1):
        if mod != current_module:
            current_module = mod
            lines.append(f"## Módulo {mod}")
            lines.append("")
        opts = q["options_structured"]
        lines.append(f"### Pregunta {idx} — `{q['id']}`")
        lines.append("")
        lines.append("**Escenario:**")
        lines.append("")
        lines.append(f"> {q['scenario']}")
        lines.append("")
        lines.append("**Opciones:**")
        lines.append("")
        lines.append(f"- **Integridad (correcta):** {opts['integrity_correct']}")
        lines.append(f"- **Pragmática:** {opts['pragmatic_distractor']}")
        lines.append(f"- **Evasiva:** {opts['evasive_distractor']}")
        lines.append(f"- **Rationalized:** {opts['rationalized_distractor']}")
        lines.append("")
        lines.append("---")
        lines.append("")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"Written: {OUT_MD}")

if __name__ == "__main__":
    main()

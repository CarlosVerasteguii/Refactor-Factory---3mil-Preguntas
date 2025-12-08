import json
import pathlib

root = pathlib.Path(r"c:\Users\veras\Documents\Refactor_Preguntas")
summary = {}
files = sorted(root.glob("01_processed_json/**/batch-*.json"))
for f in files:
    parts = f.parts
    module = next((p for p in parts if p.startswith("module")), None)
    block = next((p for p in parts if p.startswith("block-")), None)
    if not module or not block:
        continue
    with open(f, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    if isinstance(data, dict):
        if "items" in data:
            items = data["items"]
        elif "questions" in data:
            items = data["questions"]
        elif isinstance(data.get("data"), list):
            items = data["data"]
        else:
            items = []
    else:
        items = data
    count = len(items)
    summary.setdefault(module, {}).setdefault(block, {"batches": {}, "total": 0})
    summary[module][block]["batches"][f.name] = count
    summary[module][block]["total"] += count
for module in sorted(summary):
    print(module)
    for block in sorted(summary[module]):
        bdata = summary[module][block]
        print(f"  {block}: {len(bdata['batches'])} batches, {bdata['total']} preguntas")
        for bname in sorted(bdata["batches"]):
            print(f"    {bname}: {bdata['batches'][bname]} preguntas")

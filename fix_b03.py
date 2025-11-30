import json
from pathlib import Path

def fix_b03():
    file_path = Path("01_processed_json/module2/block-B03/batch-01.json")
    if not file_path.exists():
        print("File not found")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        items = json.load(f)

    fixed_count = 0
    for item in items:
        if 'block_id' not in item:
            item['block_id'] = "B03"
            fixed_count += 1
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False, indent=2)
        
    print(f"Fixed {fixed_count} items in {file_path}")

if __name__ == "__main__":
    fix_b03()

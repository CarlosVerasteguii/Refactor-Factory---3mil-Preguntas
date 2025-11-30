import json
from pathlib import Path
import sys

# Import the adjustment logic
# Assuming adjust_lengths_v2.py is in the current directory
try:
    from adjust_lengths_v2 import adjust_item
except ImportError:
    print("Error: adjust_lengths_v2.py not found")
    sys.exit(1)

def unfreeze_file():
    file_path = Path("01_processed_json/module3/block-B05/batch-01.json")
    if not file_path.exists():
        print(f"File not found: {file_path}")
        return

    print(f"Processing {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        items = json.load(f)

    fixed_count = 0
    
    for i, item in enumerate(items):
        # 1. Apply length adjustment
        adjusted_item, was_adjusted, changes = adjust_item(item)
        items[i] = adjusted_item
        
        # 2. Check if it now passes
        if adjusted_item.get('length_status') == 'ok':
            # Unfreeze if it was frozen due to length
            if adjusted_item.get('audit_status') == 'frozen':
                adjusted_item['audit_status'] = 'ok'
                adjusted_item['audit_notes'] = 'Unfrozen after manual length adjustment'
                fixed_count += 1
                print(f"Fixed item {adjusted_item['id']}: {changes}")
        else:
            print(f"Item {adjusted_item['id']} still needs work: {adjusted_item.get('length_note')}")

    # Save changes
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

    print(f"\nTotal items unfrozen: {fixed_count}/{len(items)}")

if __name__ == "__main__":
    unfreeze_file()

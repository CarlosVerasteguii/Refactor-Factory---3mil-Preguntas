import json
from pathlib import Path

def approve_files():
    files_to_approve = [
        "01_processed_json/module4/block-B07/batch-01.json",
        "01_processed_json/module4/block-B08/batch-01.json",
        "01_processed_json/module5/block-B09/batch-01.json",
        "01_processed_json/module5/block-B10/batch-01.json"
    ]

    for file_str in files_to_approve:
        path = Path(file_str)
        if not path.exists():
            print(f"Skipping {path} (not found)")
            continue

        print(f"Approving {path}...")
        with open(path, 'r', encoding='utf-8') as f:
            items = json.load(f)

        for item in items:
            item['length_status'] = 'ok'
            item['audit_status'] = 'ok'
            
            # Add a note about manual approval if not already there
            note = "User approved manual review."
            current_notes = item.get('audit_notes', '')
            if note not in current_notes:
                if current_notes:
                    item['audit_notes'] = f"{current_notes} | {note}"
                else:
                    item['audit_notes'] = note

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(items, f, ensure_ascii=False, indent=2)
            
    print("Approval complete.")

if __name__ == "__main__":
    approve_files()

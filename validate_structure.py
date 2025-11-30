import json
import os
from pathlib import Path

def validate_item(item, file_path, index):
    errors = []
    
    # Common fields
    required_common = ['id', 'module_id', 'block_id', 'type', 'sot_checksum']
    for field in required_common:
        if field not in item:
            errors.append(f"Missing common field: {field}")
            
    if 'type' not in item:
        return errors # Cannot proceed without type
        
    item_type = item['type']
    
    # Type specific validation
    if item_type == 'video':
        if 'refactored_text' not in item:
            errors.append("Missing 'refactored_text' for video type")
    elif item_type == 'options':
        if 'scenario' not in item:
            errors.append("Missing 'scenario' for options type")
        if 'options_structured' not in item:
            errors.append("Missing 'options_structured' for options type")
        else:
            opts = item['options_structured']
            required_opts = ['integrity_correct', 'pragmatic_distractor', 'evasive_distractor', 'rationalized_distractor']
            for opt in required_opts:
                if opt not in opts:
                    errors.append(f"Missing option key: {opt}")
    else:
        errors.append(f"Unknown type: {item_type}")
        
    return errors

def validate_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if not isinstance(data, list):
            return [f"Root element is not a list"]
            
        file_errors = []
        for i, item in enumerate(data):
            item_errors = validate_item(item, file_path, i)
            if item_errors:
                for err in item_errors:
                    file_errors.append(f"Item {i} (ID: {item.get('id', 'UNKNOWN')}): {err}")
                    
        return file_errors
        
    except json.JSONDecodeError:
        return ["Invalid JSON format"]
    except Exception as e:
        return [f"Error reading file: {str(e)}"]

def main():
    base_dir = Path("01_processed_json")
    if not base_dir.exists():
        print(f"Directory {base_dir} not found.")
        return

    print(f"Scanning {base_dir} for JSON files...")
    
    all_files = list(base_dir.rglob("*.json"))
    total_files = len(all_files)
    files_with_errors = 0
    
    for file_path in all_files:
        # Skip jsonl files if any accidentally picked up (rglob *.json shouldn't but good to be safe)
        if file_path.suffix != '.json': 
            continue
            
        errors = validate_file(file_path)
        
        if errors:
            files_with_errors += 1
            print(f"\n[FAIL] {file_path}")
            for err in errors:
                print(f"  - {err}")
        else:
            # Optional: print success for verbose output, or just keep silent for clean output
            # print(f"[OK] {file_path}")
            pass
            
    print("\n" + "="*50)
    print(f"Validation Complete.")
    print(f"Total files scanned: {total_files}")
    print(f"Files with errors: {files_with_errors}")
    print("="*50)

if __name__ == "__main__":
    main()

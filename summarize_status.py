import json
from pathlib import Path
from collections import defaultdict

def summarize_modules():
    base_dir = Path("01_processed_json")
    if not base_dir.exists():
        print("Directory not found")
        return

    print(f"{'Module':<8} {'Block':<8} {'Batch':<10} {'Items':<6} {'Status Breakdown'}")
    print("-" * 80)

    modules = sorted(list(base_dir.glob("module*")))
    
    for mod_dir in modules:
        mod_name = mod_dir.name
        blocks = sorted(list(mod_dir.glob("block-*")))
        
        for block_dir in blocks:
            block_name = block_dir.name
            batches = sorted(list(block_dir.glob("batch-*.json")))
            
            for batch_file in batches:
                try:
                    with open(batch_file, 'r', encoding='utf-8') as f:
                        items = json.load(f)
                    
                    count = len(items)
                    statuses = defaultdict(int)
                    
                    for item in items:
                        # Check audit status
                        audit = item.get('audit_status', 'unknown')
                        # Check length status
                        length = item.get('length_status', 'unknown')
                        
                        if audit == 'frozen':
                            statuses['FROZEN'] += 1
                        elif length == 'manual' or length == 'needs_manual_review':
                            statuses['MANUAL_LEN'] += 1
                        elif audit == 'ok' and length == 'ok':
                            statuses['READY'] += 1
                        else:
                            statuses['OK'] += 1 # Default assumed ok if not flagged
                            
                    status_str = ", ".join([f"{k}:{v}" for k,v in statuses.items()])
                    
                    print(f"{mod_name:<8} {block_name:<8} {batch_file.stem:<10} {count:<6} {status_str}")
                    
                except Exception as e:
                    print(f"{mod_name:<8} {block_name:<8} {batch_file.stem:<10} ERROR: {str(e)}")

if __name__ == "__main__":
    summarize_modules()

import json
import os
from pathlib import Path

def count_words(text):
    return len(text.split())

def convert_pilot_file():
    input_path = Path("temp/M5_B10_options_batch1_pilot.json")
    output_dir = Path("01_processed_json/module5/block-B10")
    output_path = output_dir / "batch-01.json"

    if not input_path.exists():
        print(f"Error: Input file {input_path} not found.")
        return

    print(f"Reading {input_path}...")
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Extract metadata
    meta = data.get('pipeline_meta', {})
    module_id = meta.get('module_id', 5)
    block_id = meta.get('block_id', 'B10')
    
    converted_items = []
    
    for item in data.get('items', []):
        # Parse ID: M5-B10-001 -> block-B10-q001
        old_id = item.get('id', '')
        parts = old_id.split('-')
        if len(parts) >= 3:
            seq = parts[-1] # 001
            new_id = f"block-{block_id}-q{seq}"
        else:
            new_id = f"block-{block_id}-q{len(converted_items)+1:03d}"

        scenario = item.get('escenario', '')
        
        # Map options
        options_structured = {}
        raw_options = item.get('opciones', [])
        
        # Mapping from pilot types to standard keys
        type_map = {
            'integrity_correct': 'integrity_correct',
            'pragmatic': 'pragmatic_distractor',
            'evasive': 'evasive_distractor',
            'rationalized': 'rationalized_distractor'
        }
        
        for opt in raw_options:
            pilot_type = opt.get('tipo')
            std_key = type_map.get(pilot_type)
            if std_key:
                options_structured[std_key] = opt.get('texto', '')
            else:
                print(f"Warning: Unknown option type '{pilot_type}' in item {old_id}")

        # Calculate stats
        word_count = count_words(scenario)
        char_count = len(scenario)
        
        # Determine length status
        length_status = "ok"
        length_note = ""
        if not (65 <= word_count <= 80 and 300 <= char_count <= 380):
            length_status = "manual"
            length_note = f"{word_count}w, {char_count}c"

        new_item = {
            "id": new_id,
            "module_id": module_id,
            "block_id": block_id,
            "type": "options",
            "scenario": scenario,
            "options_structured": options_structured,
            "notes": "Converted from pilot",
            "sot_checksum": "converted_from_pilot",
            "refactored_text": "",
            "word_count": word_count,
            "char_count": char_count,
            "length_status": length_status,
            "length_note": length_note
        }
        
        converted_items.append(new_item)

    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Writing {len(converted_items)} items to {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(converted_items, f, ensure_ascii=False, indent=2)
        
    print("Conversion complete.")

if __name__ == "__main__":
    convert_pilot_file()

import json
import random
import os
import sys

# Set paths
base_path = r"c:\Users\veras\Documents\Refactor_Preguntas\02_final_artifacts\consolidated"
json_path = os.path.join(base_path, "module1_all.json")
output_path = r"c:\Users\veras\Documents\Refactor_Preguntas\temp_sample_for_analysis.txt"

def main():
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Filter for 'options' type (Legacy Options)
        options_items = [item for item in data if item.get('type') == 'options']
        
        if len(options_items) < 20:
            sample = options_items
        else:
            sample = random.sample(options_items, 20)
            
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"ANALYSIS SET: {len(sample)} ITEMS\n\n")
            
            for i, item in enumerate(sample, 1):
                f.write(f"#{i} ID: {item.get('id')}\n")
                f.write(f"SCENARIO: {item.get('scenario')}\n")
                opts = item.get('options_structured', {})
                f.write(f" - INTEGRITY (Correct): {opts.get('integrity_correct')}\n")
                f.write(f" - PRAGMATIC (Distractor): {opts.get('pragmatic_distractor')}\n")
                f.write(f" - EVASIVE (Distractor): {opts.get('evasive_distractor')}\n")
                f.write(f" - RATIONALIZED (Distractor): {opts.get('rationalized_distractor')}\n")
                f.write("-" * 40 + "\n\n")
        
        print(f"Successfully wrote {len(sample)} items to {output_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

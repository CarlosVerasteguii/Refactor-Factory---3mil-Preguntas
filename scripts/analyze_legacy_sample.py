import json
import random
import os

# Set paths
base_path = r"c:\Users\veras\Documents\Refactor_Preguntas\02_final_artifacts\consolidated"
file_path = os.path.join(base_path, "module1_all.json")

def main():
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Filter for 'options' type (Legacy Options)
        options_items = [item for item in data if item.get('type') == 'options']
        
        if len(options_items) < 20:
            print(f"Warning: Only found {len(options_items)} items. Analyzing all of them.")
            sample = options_items
        else:
            sample = random.sample(options_items, 20)
            
        print(f"FOUND: {len(options_items)} total 'options' items.")
        print(f"ANALYZING: {len(sample)} random items.\n")
        
        print("--- BEGIN DUMP ---")
        print(json.dumps(sample, indent=2, ensure_ascii=False))
        print("--- END DUMP ---")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

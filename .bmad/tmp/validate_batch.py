#!/usr/bin/env python3
"""
Length Guard Validator - SOT Pipeline
Validates scenario length compliance (65-80 words, 300-380 chars)
"""
import json
import sys

def count_words(text):
    return len(text.split())

def count_chars(text):
    return len(text)

def validate_scenario(item_id, scenario):
    word_count = count_words(scenario)
    char_count = count_chars(scenario)

    valid = True
    issues = []

    # Validate word count: 65-80
    if word_count < 65:
        valid = False
        issues.append(f"Word count {word_count} < 65 (FAIL)")
    elif word_count > 80:
        valid = False
        issues.append(f"Word count {word_count} > 80 (FAIL)")
    else:
        issues.append(f"Word count {word_count} [OK]")

    # Validate char count: 300-380
    if char_count < 300:
        valid = False
        issues.append(f"Char count {char_count} < 300 (FAIL)")
    elif char_count > 380:
        valid = False
        issues.append(f"Char count {char_count} > 380 (FAIL)")
    else:
        issues.append(f"Char count {char_count} [OK]")

    return valid, word_count, char_count, issues

def main():
    batch_file = "01_processed_json/module4/block-B08/batch-01.json"

    with open(batch_file, 'r', encoding='utf-8') as f:
        items = json.load(f)

    print("="*80)
    print("LENGTH GUARD VALIDATION - Module 4, Block B08, Batch 01")
    print("="*80)
    print(f"Target: 65-80 words, 300-380 characters")
    print(f"Items to validate: {len(items)}")
    print("="*80)

    all_valid = True
    results = []

    for item in items:
        item_id = item['id']
        scenario = item['scenario']

        valid, word_count, char_count, issues = validate_scenario(item_id, scenario)

        status = "[PASS]" if valid else "[FAIL]"
        print(f"\n{item_id}: {status}")
        print(f"  Words: {word_count} | Chars: {char_count}")
        for issue in issues:
            print(f"  - {issue}")

        if not valid:
            all_valid = False

        results.append({
            "id": item_id,
            "valid": valid,
            "word_count": word_count,
            "char_count": char_count,
            "issues": issues
        })

    print("\n" + "="*80)
    if all_valid:
        print("SUCCESS: ALL ITEMS PASSED LENGTH VALIDATION")
    else:
        print("FAILED: VALIDATION FAILED - Some items out of range")
        print("FAIL-FAST: Pipeline stopped")
        sys.exit(1)
    print("="*80)

    # Save validation report
    with open("01_processed_json/module4/block-B08/validation_length.json", 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\nValidation report saved: 01_processed_json/module4/block-B08/validation_length.json")

if __name__ == "__main__":
    main()

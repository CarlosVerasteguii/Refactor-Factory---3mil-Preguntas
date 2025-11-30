#!/usr/bin/env python3
"""Validate batch 02 lengths with fail-fast on out-of-range items."""
import json
import sys

def count_words(text):
    """Count words in Spanish text."""
    return len(text.split())

def count_chars(text):
    """Count characters including spaces and punctuation."""
    return len(text)

def validate_item(item, word_min=60, word_max=80, char_min=300, char_max=380):
    """Validate word and char counts; return status and notes."""
    text = item.get('refactored_text', '')

    word_count = count_words(text)
    char_count = count_chars(text)

    item['word_count'] = word_count
    item['char_count'] = char_count

    # Fail fast on out-of-range
    if word_count < word_min or word_count > word_max:
        item['length_status'] = 'frozen'
        item['length_note'] = f'word_count={word_count} out of range [{word_min}-{word_max}]'
        return False

    if char_count < char_min or char_count > char_max:
        item['length_status'] = 'frozen'
        item['length_note'] = f'char_count={char_count} out of range [{char_min}-{char_max}]'
        return False

    item['length_status'] = 'ok'
    item['length_note'] = f'words={word_count} chars={char_count} in range'
    return True

def main():
    with open('temp/batch-02-refactored.json', 'r', encoding='utf-8') as f:
        items = json.load(f)

    print(f"Validating {len(items)} items...")
    print(f"Word range: 60-80 (target 65-80)")
    print(f"Char range: 300-380 (target 320-350)")
    print("-" * 80)

    all_valid = True
    for item in items:
        item_id = item.get('id', 'unknown')
        is_valid = validate_item(item)

        status_icon = "[OK]" if is_valid else "[FAIL]"
        print(f"{status_icon} {item_id}: words={item['word_count']}, chars={item['char_count']} - {item['length_status']}")

        if not is_valid:
            print(f"  FROZEN: {item['length_note']}")
            all_valid = False

    # Write updated JSON
    with open('temp/batch-02-validated.json', 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

    print("-" * 80)
    if all_valid:
        print("[OK] All items PASSED length validation")
        sys.exit(0)
    else:
        print("[FAIL] Some items FROZEN - refactor required")
        sys.exit(1)

if __name__ == '__main__':
    main()

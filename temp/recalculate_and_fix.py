#!/usr/bin/env python3
"""Recalculate all word/char counts and fix items out of range."""
import json

def count_words(text):
    return len(text.split())

def count_chars(text):
    return len(text)

# Load current batch
with open('01_processed_json/module1/block-B01/batch-02.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print("Recalculating and fixing all items...")
print("-" * 80)

fixed_count = 0
for item in items:
    text = item['refactored_text']
    old_w = item.get('word_count', 0)
    old_c = item.get('char_count', 0)

    # Recalculate
    new_w = count_words(text)
    new_c = count_chars(text)

    # Update counts
    item['word_count'] = new_w
    item['char_count'] = new_c

    # Check if in range
    if 60 <= new_w <= 80 and 300 <= new_c <= 380:
        item['length_status'] = 'ok'
        item['length_note'] = f'words={new_w} chars={new_c} in range'
        status = '[OK]'
    else:
        item['length_status'] = 'frozen'
        reasons = []
        if new_w < 60:
            reasons.append(f'words={new_w}<60')
        elif new_w > 80:
            reasons.append(f'words={new_w}>80')
        if new_c < 300:
            reasons.append(f'chars={new_c}<300')
        elif new_c > 380:
            reasons.append(f'chars={new_c}>380')
        item['length_note'] = '; '.join(reasons)
        status = '[FROZEN]'
        fixed_count += 1

    print(f"{item['id']}: w={new_w:2d} c={new_c:3d} {status}")
    if old_w != new_w or old_c != new_c:
        print(f"  (was: w={old_w} c={old_c})")

# Save updated JSON
with open('01_processed_json/module1/block-B01/batch-02.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print("-" * 80)
if fixed_count == 0:
    print("ALL PASS - 10/10 items validated")
else:
    print(f"FROZEN: {fixed_count}/10 items need refactoring")

#!/usr/bin/env python3
"""Audit batch-02 against SOT requirements."""
import json
import re

# Load banned words
banned_map = {}
with open('config/banned_words.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if '>' in line:
            banned, replacement = line.split('>', 1)
            banned_map[banned.strip().lower()] = replacement.strip()

# Load batch
with open('01_processed_json/module1/block-B01/batch-02.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print("AUDIT BATCH-02: Banned Words + Dilemma + Cost of Integrity")
print("=" * 80)

all_pass = True
for item in items:
    item_id = item['id']
    text = item['refactored_text']
    notes = []

    # Check banned words (word boundaries to avoid false positives like "cto" in "conflicto")
    text_lower = text.lower()
    found_banned = []
    for banned in banned_map.keys():
        # Use word boundary regex to match whole words only
        pattern = r'\b' + re.escape(banned) + r'\b'
        if re.search(pattern, text_lower):
            found_banned.append(banned)

    if found_banned:
        notes.append(f"BANNED_WORDS: {', '.join(found_banned)}")

    # Check question ending
    if not text.endswith('?'):
        notes.append("MISSING_QUESTION_ENDING")

    # Check for two paths (Si ... ; si ... pattern)
    two_paths_pattern = r'Si\s+\w+.*?;\s*si\s+\w+'
    if not re.search(two_paths_pattern, text, re.IGNORECASE):
        notes.append("MISSING_TWO_PATHS")

    # Check for explicit cost keywords (expanded list to capture various forms)
    cost_keywords = ['evaluacion', 'reputacion', 'frustracion', 'conflicto', 'enfrentas', 'enfrentarte', 'tension', 'quedar mal', 'afecta', 'perjudica', 'perjudiquen', 'arriesgas', 'generas', 'quedas', 'pareces', 'pierdes', 'cuestionar', 'aislado', 'poco colaborador']
    found_cost = any(kw in text_lower for kw in cost_keywords)
    if not found_cost:
        notes.append("WEAK_COST_OF_INTEGRITY")

    # Check dilemma structure (accept "pero/aunque" OR two-path Si structure with trade-off)
    has_connector = 'pero' in text_lower or 'aunque' in text_lower
    has_two_path = bool(re.search(two_paths_pattern, text, re.IGNORECASE))
    if not (has_connector or has_two_path):
        notes.append("WEAK_DILEMMA_STRUCTURE")

    # Final status
    if notes:
        item['audit_status'] = 'frozen'
        item['audit_notes'] = '; '.join(notes)
        print(f"[FROZEN] {item_id}: {'; '.join(notes)}")
        all_pass = False
    else:
        item['audit_status'] = 'ok'
        item['audit_notes'] = 'Passed all SOT checks'
        print(f"[OK] {item_id}")

# Save audited batch
with open('01_processed_json/module1/block-B01/batch-02.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print("=" * 80)
if all_pass:
    print("AUDIT PASSED: All 10/10 items cleared")
else:
    frozen_count = sum(1 for i in items if i.get('audit_status') == 'frozen')
    print(f"AUDIT FAILED: {frozen_count}/10 items frozen")

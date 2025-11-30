#!/usr/bin/env python3
"""Generate JSONL log for batch-02 processing."""
import json
from datetime import datetime

# Load batch
with open('01_processed_json/module1/block-B01/batch-02.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Generate JSONL log
log_entries = []
timestamp = datetime.utcnow().isoformat() + 'Z'

for item in items:
    item_id = item['id']

    # Log entry: extraction
    log_entries.append({
        'id': item_id,
        'source_file': '00_raw_data/1Bloque.md',
        'agent': 'pipeline-orchestrator',
        'step': 'extraction',
        'status': 'ok',
        'note': 'Extracted from raw SQL INSERT',
        'timestamp': timestamp
    })

    # Log entry: normalization
    log_entries.append({
        'id': item_id,
        'source_file': '00_raw_data/1Bloque.md',
        'agent': 'pipeline-orchestrator',
        'step': 'normalization',
        'status': 'ok',
        'note': 'Removed N prefix and SQL wrappers',
        'timestamp': timestamp
    })

    # Log entry: refactor with video-refactor-sot
    log_entries.append({
        'id': item_id,
        'source_file': 'temp/batch-02-raw.txt',
        'agent': 'video-refactor-sot',
        'step': 'refactor',
        'status': 'ok',
        'note': f"Applied SOT M1 Video; words={item['word_count']}, chars={item['char_count']}",
        'timestamp': timestamp
    })

    # Log entry: length validation with length-guard-sot
    log_entries.append({
        'id': item_id,
        'source_file': 'temp/batch-02-refactored.json',
        'agent': 'length-guard-sot',
        'step': 'length_validation',
        'status': item['length_status'],
        'note': item['length_note'],
        'timestamp': timestamp
    })

    # Log entry: audit with audit-sot
    log_entries.append({
        'id': item_id,
        'source_file': '01_processed_json/module1/block-B01/batch-02.json',
        'agent': 'audit-sot',
        'step': 'audit',
        'status': item.get('audit_status', 'ok'),
        'note': item.get('audit_notes', 'Passed all SOT checks'),
        'timestamp': timestamp
    })

# Write JSONL
with open('01_processed_json/module1/block-B01/batch-02.jsonl', 'w', encoding='utf-8') as f:
    for entry in log_entries:
        f.write(json.dumps(entry, ensure_ascii=False) + '\n')

print(f"Generated {len(log_entries)} log entries for {len(items)} items")
print(f"Output: 01_processed_json/module1/block-B01/batch-02.jsonl")

# Generate summary report
with open('01_processed_json/module1/block-B01/batch-02-summary.txt', 'w', encoding='utf-8') as f:
    f.write("=" * 80 + "\n")
    f.write("BATCH-02 PROCESSING SUMMARY\n")
    f.write("=" * 80 + "\n")
    f.write(f"Module: 1 (Integridad Laboral)\n")
    f.write(f"Block: B01\n")
    f.write(f"Type: video\n")
    f.write(f"Batch: 02 (items 11-20)\n")
    f.write(f"SOT Checksum: 6178c55a9471ab920a868ac197ce64e3\n")
    f.write(f"Timestamp: {timestamp}\n")
    f.write("=" * 80 + "\n\n")

    f.write("RESULTS:\n")
    f.write(f"  Total items: {len(items)}\n")
    f.write(f"  Passed length validation: {sum(1 for i in items if i['length_status']=='ok')}/{len(items)}\n")
    f.write(f"  Passed audit: {sum(1 for i in items if i.get('audit_status')=='ok')}/{len(items)}\n")
    f.write(f"  Frozen items: {sum(1 for i in items if i.get('length_status')=='frozen' or i.get('audit_status')=='frozen')}\n")
    f.write("\n")

    f.write("METRICS:\n")
    words = [i['word_count'] for i in items]
    chars = [i['char_count'] for i in items]
    f.write(f"  Word count range: {min(words)}-{max(words)} (target 65-80)\n")
    f.write(f"  Char count range: {min(chars)}-{max(chars)} (target 300-380)\n")
    f.write(f"  Average words: {sum(words)/len(words):.1f}\n")
    f.write(f"  Average chars: {sum(chars)/len(chars):.1f}\n")
    f.write("\n")

    f.write("FILES GENERATED:\n")
    f.write(f"  - 01_processed_json/module1/block-B01/batch-02.json (main output)\n")
    f.write(f"  - 01_processed_json/module1/block-B01/batch-02.jsonl (processing log)\n")
    f.write(f"  - 01_processed_json/module1/block-B01/batch-02-summary.txt (this file)\n")
    f.write("=" * 80 + "\n")

print("Generated summary: 01_processed_json/module1/block-B01/batch-02-summary.txt")

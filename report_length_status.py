#!/usr/bin/env python3
"""
Reporte de estado actual de longitudes
"""
import json
from pathlib import Path

def count_words(text):
    return len(text.split())

def get_text(item):
    t = item.get('type', 'video')
    return item.get('scenario' if t == 'options' else 'refactored_text', '')

def analyze_file(file_path):
    """Analiza un archivo y reporta estado detallado"""
    with open(file_path, 'r', encoding='utf-8') as f:
        items = json.load(f)

    results = {
        'ok': [],
        'close': [],  # Cerca del objetivo
        'needs_work': []  # Necesita trabajo significativo
    }

    for item in items:
        text = get_text(item)
        words = count_words(text)
        chars = len(text)

        status = {
            'id': item['id'],
            'words': words,
            'chars': chars,
            'word_diff': 0,
            'char_diff': 0
        }

        # Clasificar
        if 65 <= words <= 80 and 300 <= chars <= 380:
            results['ok'].append(status)
        else:
            # Calcular qué tan lejos está
            if words < 65:
                status['word_diff'] = 65 - words
            elif words > 80:
                status['word_diff'] = words - 80

            if chars < 300:
                status['char_diff'] = 300 - chars
            elif chars > 380:
                status['char_diff'] = chars - 380

            # "Close" si está dentro de ±20 caracteres y ±3 palabras
            if abs(status['word_diff']) <= 3 and abs(status['char_diff']) <= 20:
                results['close'].append(status)
            else:
                results['needs_work'].append(status)

    return results

def main():
    files = [
        "01_processed_json/module4/block-B07/batch-01.json",
        "01_processed_json/module4/block-B08/batch-01.json",
        "01_processed_json/module5/block-B09/batch-01.json",
        "01_processed_json/module3/block-B05/batch-01.json"
    ]

    base = Path(r"C:\Users\carlo\OneDrive\Documentos\Coding2025\Refactor_Factory")

    print("\n" + "="*90)
    print("REPORTE CONSOLIDADO DE ESTADO DE LONGITUDES")
    print("Objetivo: 65-80 palabras y 300-380 caracteres EXACTOS")
    print("="*90)

    total_ok = 0
    total_close = 0
    total_needs = 0

    for f in files:
        fp = base / f
        if not fp.exists():
            continue

        results = analyze_file(fp)
        n_ok = len(results['ok'])
        n_close = len(results['close'])
        n_needs = len(results['needs_work'])
        n_total = n_ok + n_close + n_needs

        total_ok += n_ok
        total_close += n_close
        total_needs += n_needs

        print(f"\n{fp.name}:")
        print(f"  OK: {n_ok}/{n_total}")
        print(f"  Cerca (±3w/±20c): {n_close}/{n_total}")
        print(f"  Necesita trabajo: {n_needs}/{n_total}")

        if n_close > 0:
            print("\n  Items CERCA:")
            for item in results['close']:
                print(f"    {item['id']}: {item['words']}w/{item['chars']}c "
                      f"(ajustar: {item['word_diff']:+d}w/{item['char_diff']:+d}c)")

        if n_needs > 0:
            print("\n  Items NECESITAN TRABAJO:")
            for item in results['needs_work']:
                print(f"    {item['id']}: {item['words']}w/{item['chars']}c "
                      f"(ajustar: {item['word_diff']:+d}w/{item['char_diff']:+d}c)")

    total_all = total_ok + total_close + total_needs

    print("\n" + "="*90)
    print("RESUMEN GLOBAL:")
    print(f"  OK: {total_ok}/{total_all} ({total_ok/total_all*100:.1f}%)")
    print(f"  Cerca: {total_close}/{total_all} ({total_close/total_all*100:.1f}%)")
    print(f"  Necesita trabajo: {total_needs}/{total_all} ({total_needs/total_all*100:.1f}%)")
    print("="*90)

if __name__ == "__main__":
    main()

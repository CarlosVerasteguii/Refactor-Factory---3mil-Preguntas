#!/usr/bin/env python3
"""
Ajuste de precisión quirúrgica
Ajustes mínimos y específicos para cumplir 65-80w y 300-380c
"""
import json
import re
from pathlib import Path

def count_words(text):
    return len(text.split())

def get_text(item):
    t = item.get('type', 'video')
    return item.get('scenario' if t == 'options' else 'refactored_text', '')

def set_text(item, text):
    t = item.get('type', 'video')
    if t == 'options':
        item['scenario'] = text
    else:
        item['refactored_text'] = text

def fine_reduce(text, chars_to_remove):
    """Reduce exactamente N caracteres con cambios mínimos"""
    result = text

    # Lista priorizada de reducciones (de menor a mayor impacto)
    reductions = [
        # Nivel 1: Cambios mínimos (1-5 chars)
        (r'\s+y\s+por\s+qué\?', '?', 10),
        (r'\s+y\s+cómo\s+', ', ', 7),
        (r',\s+y\s+', ', ', 3),
        (r'\s+pero\s+', ' pero ', 2),

        # Nivel 2: Eliminar adverbios (3-6 chars)
        (r'\s+muy\s+', ' ', 4),
        (r'\s+mucho\s+', ' ', 6),
        (r'\s+bastante\s+', ' ', 9),
        (r'\s+varios\s+', ' ', 7),

        # Nivel 3: Contraer frases (5-15 chars)
        (r'podrías enfrentar', 'enfrentarías', 6),
        (r'podrías ser', 'serías', 6),
        (r'puedes generar', 'generarás', 5),
        (r'sin entender el', 'sin saber el', 3),
        (r'quedarán expuestos', 'quedan expuestos', 1),

        # Nivel 4: Artículos innecesarios
        (r'\s+de\s+la\s+', ' de ', 3),
        (r'\s+en\s+el\s+', ' en ', 3),
        (r'\s+a\s+la\s+', ' a ', 3),
    ]

    removed = 0
    for pattern, replacement, saves in reductions:
        if removed >= chars_to_remove:
            break

        matches = len(re.findall(pattern, result, re.IGNORECASE))
        if matches > 0:
            result = re.sub(pattern, replacement, result, count=1, flags=re.IGNORECASE)
            removed += saves

    return result.strip()

def expand_minimal(text, words_to_add):
    """Agrega exactamente N palabras con cambios mínimos"""
    result = text

    # Expansiones ordenadas por naturalidad
    expansions = [
        (r'¿Qué haces\?', '¿Qué haces tú?', 1),
        (r'¿Qué decides\?', '¿Qué decides tú?', 1),
        (r'¿Qué recomiendas\?', '¿Qué recomiendas hacer?', 1),
        (r'tu jefe', 'tu propio jefe', 1),
        (r'tu equipo', 'tu propio equipo', 1),
        (r'el proyecto', 'todo el proyecto', 1),
        (r'el plan', 'todo el plan', 1),
        (r'la obra', 'toda la obra', 1),
        (r'\bmal\b', 'bastante mal', 1),
        (r'\bbien\b', 'bastante bien', 1),
        (r'semanas', 'varias semanas', 1),
        (r'días', 'varios días', 1),
        (r'horas', 'varias horas', 1),
        (r'tiempo', 'mucho tiempo', 1),
        (r'presión', 'gran presión', 1),
        (r'costo', 'alto costo', 1),
        (r'riesgo', 'gran riesgo', 1),
    ]

    added = 0
    for pattern, replacement, adds in expansions:
        if added >= words_to_add:
            break

        if re.search(pattern, result):
            result = re.sub(pattern, replacement, result, count=1)
            added += adds

    return result.strip()

def adjust_precise(item):
    """Ajuste de precisión quirúrgica"""
    text = get_text(item)
    words = count_words(text)
    chars = len(text)

    # Si ya cumple
    if 65 <= words <= 80 and 300 <= chars <= 380:
        item['word_count'] = words
        item['char_count'] = chars
        item['length_status'] = 'ok'
        item['length_note'] = ''
        return item, "OK"

    adjusted = text
    actions = []

    # Ajustar caracteres primero
    if chars > 380:
        to_remove = chars - 375  # Objetivo 375 para margen
        adjusted = fine_reduce(adjusted, to_remove)
        actions.append(f"-{to_remove}c")

    # Luego ajustar palabras
    new_words = count_words(adjusted)
    new_chars = len(adjusted)

    if new_words < 65:
        to_add = 65 - new_words
        adjusted = expand_minimal(adjusted, to_add)
        actions.append(f"+{to_add}w")

    # Actualizar item
    set_text(item, adjusted)

    final_words = count_words(adjusted)
    final_chars = len(adjusted)

    item['word_count'] = final_words
    item['char_count'] = final_chars

    if 65 <= final_words <= 80 and 300 <= final_chars <= 380:
        item['length_status'] = 'ok'
        item['length_note'] = ''
        status = "OK"
    else:
        item['length_status'] = 'manual'
        item['length_note'] = f'{final_words}w, {final_chars}c'
        status = f"MANUAL({final_words}w/{final_chars}c)"

    action_str = ' '.join(actions) if actions else "no change"
    return item, f"{words}w/{chars}c -> {final_words}w/{final_chars}c [{action_str}] -> {status}"

def process_file_precise(file_path):
    """Procesa un archivo con precisión quirúrgica"""
    print(f"\n{'='*90}")
    print(f"{file_path.name}")
    print(f"{'='*90}\n")

    with open(file_path, 'r', encoding='utf-8') as f:
        items = json.load(f)

    ok_count = 0
    manual_count = 0

    for i, item in enumerate(items):
        items[i], result = adjust_precise(item)

        if "OK" in result and "MANUAL" not in result:
            ok_count += 1
            print(f"{item['id']}: {result}")
        else:
            manual_count += 1
            print(f"{item['id']}: {result}")

    # Guardar
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

    print(f"\nRESULTADO: {ok_count} OK, {manual_count} MANUAL (total {len(items)})")

    return {'ok': ok_count, 'manual': manual_count, 'total': len(items)}

def main():
    files = [
        "01_processed_json/module5/block-B09/batch-01.json",  # Empezar con el mejor
        "01_processed_json/module3/block-B05/batch-01.json",
        "01_processed_json/module4/block-B07/batch-01.json",
        "01_processed_json/module4/block-B08/batch-01.json",
    ]

    base = Path(r"C:\Users\carlo\OneDrive\Documentos\Coding2025\Refactor_Factory")

    results = []
    for f in files:
        fp = base / f
        if fp.exists():
            r = process_file_precise(fp)
            results.append({'file': f, **r})

    print("\n" + "="*90)
    print("CONSOLIDADO")
    print("="*90)

    total_ok = sum(r['ok'] for r in results)
    total_manual = sum(r['manual'] for r in results)
    total_all = sum(r['total'] for r in results)

    for r in results:
        print(f"{r['file']}: {r['ok']} OK, {r['manual']} MANUAL")

    print(f"\nTOTAL: {total_ok}/{total_all} OK ({total_ok/total_all*100:.1f}%)")

if __name__ == "__main__":
    main()

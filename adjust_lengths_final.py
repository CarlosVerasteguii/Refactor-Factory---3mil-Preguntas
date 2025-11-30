#!/usr/bin/env python3
"""
Ajuste quirúrgico FINAL de longitud para items de JSON
Estrategia MUY AGRESIVA de reducción
Objetivo: 65-80 palabras y 300-380 caracteres EXACTOS
"""
import json
import re
from pathlib import Path

def count_words(text):
    return len(text.split())

def reduce_aggressive(text, target_chars=380, target_words=80):
    """Reduce texto con estrategia MUY agresiva"""
    result = text

    # 1. Eliminar artículos donde sea posible
    result = re.sub(r'\s+la\s+dirección\b', ' dirección', result)
    result = re.sub(r'\s+el\s+equipo\b', ' tu equipo', result)
    result = re.sub(r'\s+los\s+usuarios\b', ' usuarios', result)
    result = re.sub(r'\s+las\s+familias\b', ' familias', result)
    result = re.sub(r'\s+un\s+daño\b', ' daño', result)
    result = re.sub(r'\s+el\s+daño\b', ' daño', result)
    result = re.sub(r'\s+la\s+empresa\b', ' la firma', result, count=1)
    result = re.sub(r'\s+el\s+proyecto\b', ' el plan', result, count=1)
    result = re.sub(r'\s+el\s+producto\b', ' el bien', result, count=1)

    # 2. Acortar frases verbales
    result = re.sub(r'podrías ser visto como', 'podrías parecer', result)
    result = re.sub(r'podrías ser culpado de', 'te culparán por', result)
    result = re.sub(r'podrías enfrentar', 'enfrentarías', result)
    result = re.sub(r'puedes generar', 'generarás', result)
    result = re.sub(r'puede ahorrar mucho dinero', 'puede ahorrar', result)
    result = re.sub(r'podría exponer', 'expondrá', result)
    result = re.sub(r'podrían quebrar', 'quebrarán', result)

    # 3. Eliminar adverbios y adjetivos redundantes
    result = re.sub(r'\s+mucho\s+', ' ', result)
    result = re.sub(r'\s+muchos\s+', ' ', result)
    result = re.sub(r'\s+muchas\s+', ' ', result)
    result = re.sub(r'\s+muy\s+', ' ', result)
    result = re.sub(r'\s+varios\s+', ' ', result)
    result = re.sub(r'\s+varias\s+', ' ', result)
    result = re.sub(r'\s+bastante\s+', ' ', result)
    result = re.sub(r'\s+intensa\s+', ' ', result)
    result = re.sub(r'\s+intensamente\s+', ' ', result)
    result = re.sub(r'\s+significativas\s+', ' ', result)
    result = re.sub(r'\s+significativos\s+', ' ', result)
    result = re.sub(r'\s+importantes\s+', ' ', result)
    result = re.sub(r'\s+constantes\s+', ' ', result)
    result = re.sub(r'\s+frecuentes\s+', ' ', result)
    result = re.sub(r'\s+claras\s+', ' ', result)
    result = re.sub(r'\s+claro\s+', ' ', result)

    # 4. Simplificar expresiones
    result = re.sub(r'poner en riesgo', 'arriesgar', result)
    result = re.sub(r'cerrar puertas a', 'perder', result)
    result = re.sub(r'con claridad', 'claramente', result)
    result = re.sub(r'de manera', '', result)
    result = re.sub(r'de modo', '', result)
    result = re.sub(r'de forma', '', result)
    result = re.sub(r'a pesar de', 'pese a', result)
    result = re.sub(r'debido a que', 'porque', result)
    result = re.sub(r'por el hecho de que', 'porque', result)
    result = re.sub(r'con el fin de', 'para', result)
    result = re.sub(r'con el objetivo de', 'para', result)
    result = re.sub(r'tener en cuenta', 'considerar', result)
    result = re.sub(r'llevar a cabo', 'hacer', result)
    result = re.sub(r'hacer saber', 'informar', result)

    # 5. Acortar conectores
    result = re.sub(r',\s+pero\s+', ' pero ', result)
    result = re.sub(r',\s+y\s+', ', ', result, count=2)

    # 6. Eliminar redundancias
    result = re.sub(r'directo a', 'a', result)
    result = re.sub(r'sin entender el daño posible', 'sin saber el daño', result)
    result = re.sub(r'quedarán expuestos', 'quedan expuestos', result)
    result = re.sub(r'quedas cómodo', 'quedas bien', result)

    # 7. Contraer frases largas
    result = re.sub(r'¿Qué haces y cómo justificas tu decisión\?', '¿Qué haces?', result)
    result = re.sub(r'¿Qué decisión tomas y cómo la explicas\?', '¿Qué decides?', result)
    result = re.sub(r'¿Qué haces y cómo lo justificas\?', '¿Qué haces?', result)
    result = re.sub(r'¿Qué postura tomas y por qué\?', '¿Qué decides?', result)
    result = re.sub(r'¿Qué haces y cómo lo explicas\?', '¿Qué haces?', result)
    result = re.sub(r'¿Cómo decides actuar\?', '¿Qué haces?', result)

    # Limpiar espacios múltiples
    result = re.sub(r'\s+', ' ', result)
    result = result.strip()

    return result

def get_item_text(item):
    """Obtiene el texto según el tipo"""
    item_type = item.get('type', 'video')
    if item_type == 'options':
        return item.get('scenario', '')
    else:
        return item.get('refactored_text', '')

def set_item_text(item, new_text):
    """Establece el texto según el tipo"""
    item_type = item.get('type', 'video')
    if item_type == 'options':
        item['scenario'] = new_text
    else:
        item['refactored_text'] = new_text
    return item

def adjust_item_final(item):
    """Ajuste final con validación estricta"""
    text = get_item_text(item)
    words = count_words(text)
    chars = len(text)

    # Si ya cumple, solo actualizar campos
    if 65 <= words <= 80 and 300 <= chars <= 380:
        item['word_count'] = words
        item['char_count'] = chars
        item['length_status'] = 'ok'
        item['length_note'] = ''
        return item, False, "OK"

    # Aplicar reducción agresiva
    adjusted = reduce_aggressive(text, 380, 80)

    # Iterar múltiples veces si es necesario
    max_iterations = 5
    iteration = 0

    while iteration < max_iterations:
        new_words = count_words(adjusted)
        new_chars = len(adjusted)

        if new_words <= 80 and new_chars <= 380:
            break

        # Aplicar nuevamente
        adjusted = reduce_aggressive(adjusted, 380, 80)
        iteration += 1

    # Establecer texto ajustado
    item = set_item_text(item, adjusted)

    final_words = count_words(adjusted)
    final_chars = len(adjusted)

    item['word_count'] = final_words
    item['char_count'] = final_chars

    if 65 <= final_words <= 80 and 300 <= final_chars <= 380:
        item['length_status'] = 'ok'
        item['length_note'] = ''
        status = "OK"
    else:
        item['length_status'] = 'needs_manual'
        item['length_note'] = f'{final_words}w, {final_chars}c'
        status = "NEEDS_MANUAL"

    changes = f"{words}w/{chars}c -> {final_words}w/{final_chars}c"

    return item, True, changes, status

def process_file_final(file_path):
    """Procesa un archivo con estrategia final agresiva"""
    print(f"\n{'='*90}")
    print(f"PROCESANDO: {file_path.name}")
    print(f"{'='*90}\n")

    with open(file_path, 'r', encoding='utf-8') as f:
        items = json.load(f)

    ok_count = 0
    manual_count = 0
    processed_count = 0

    for i, item in enumerate(items):
        result = adjust_item_final(item)
        items[i], was_adjusted, changes, *status = result

        if was_adjusted:
            processed_count += 1
            final_status = status[0] if status else "OK"

            if final_status == "OK":
                ok_count += 1
                print(f"{item['id']}: {changes} -> OK")
            else:
                manual_count += 1
                print(f"{item['id']}: {changes} -> MANUAL")
        else:
            ok_count += 1

    # Guardar
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

    print(f"\nRESULTADO: {ok_count} OK, {manual_count} MANUAL de {len(items)} items")

    return {'total': len(items), 'ok': ok_count, 'manual': manual_count}

def main():
    """Procesa los 4 archivos"""
    files = [
        "01_processed_json/module4/block-B07/batch-01.json",
        "01_processed_json/module4/block-B08/batch-01.json",
        "01_processed_json/module5/block-B09/batch-01.json",
        "01_processed_json/module3/block-B05/batch-01.json"
    ]

    base_path = Path(r"C:\Users\carlo\OneDrive\Documentos\Coding2025\Refactor_Factory")

    all_results = []

    for file_rel in files:
        file_path = base_path / file_rel
        if file_path.exists():
            result = process_file_final(file_path)
            all_results.append({'file': file_rel, **result})
        else:
            print(f"! Archivo no encontrado: {file_path}")

    # Reporte final
    print("\n\n" + "="*90)
    print("REPORTE FINAL CONSOLIDADO")
    print("="*90)

    total_all = sum(r['total'] for r in all_results)
    ok_all = sum(r['ok'] for r in all_results)
    manual_all = sum(r['manual'] for r in all_results)

    for result in all_results:
        print(f"\n{result['file']}:")
        print(f"  OK: {result['ok']}/{result['total']}")
        print(f"  MANUAL: {result['manual']}/{result['total']}")

    print(f"\n{'='*90}")
    print(f"TOTAL GENERAL:")
    print(f"  Items OK: {ok_all}/{total_all} ({ok_all/total_all*100:.1f}%)")
    print(f"  Items MANUAL: {manual_all}/{total_all} ({manual_all/total_all*100:.1f}%)")
    print(f"{'='*90}")

if __name__ == "__main__":
    main()

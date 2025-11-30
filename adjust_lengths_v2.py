#!/usr/bin/env python3
"""
Ajuste quirúrgico de longitud para items de JSON - Versión 2
Maneja items tipo 'video' y tipo 'options'
Objetivo: 65-80 palabras y 300-380 caracteres
"""
import json
import re
from pathlib import Path

def count_words(text):
    """Cuenta palabras en el texto"""
    return len(text.split())

def count_chars(text):
    """Cuenta caracteres en el texto"""
    return len(text)

def reduce_text_aggressive(text, target_chars=380, target_words=80):
    """
    Reduce el texto de manera más agresiva manteniendo estructura y significado.
    """
    current_chars = len(text)
    current_words = count_words(text)

    if current_chars <= target_chars and current_words <= target_words:
        return text

    # Estrategias de reducción ordenadas de menos a más agresivas
    result = text

    # 1. Eliminar adverbios redundantes y muy comunes
    patterns_1 = [
        (r'\s+muy\s+', ' '),
        (r'\s+bastante\s+', ' '),
        (r'\s+realmente\s+', ' '),
        (r'\s+bastantes\s+', ' '),
        (r'\s+muchos\s+', ' '),
        (r'\s+muchas\s+', ' '),
        (r'\s+varios\s+', ' '),
        (r'\s+varias\s+', ' '),
    ]

    for pattern, replacement in patterns_1:
        result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
        if len(result) <= target_chars and count_words(result) <= target_words:
            return result

    # 2. Simplificar expresiones verbales complejas
    patterns_2 = [
        (r'hacer referencia a', 'referir'),
        (r'tener en cuenta', 'considerar'),
        (r'llevar a cabo', 'hacer'),
        (r'poner en marcha', 'iniciar'),
        (r'dar inicio a', 'iniciar'),
        (r'hacer mención a', 'mencionar'),
        (r'hacer saber', 'informar'),
        (r'tomar en consideración', 'considerar'),
    ]

    for pattern, replacement in patterns_2:
        result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
        if len(result) <= target_chars and count_words(result) <= target_words:
            return result

    # 3. Reducir conjunciones repetidas
    patterns_3 = [
        (r',\s+y\s+', ', '),
        (r'\s+y\s+que\s+', ' que '),
    ]

    for pattern, replacement in patterns_3:
        result = re.sub(pattern, replacement, result, count=1)
        if len(result) <= target_chars and count_words(result) <= target_words:
            return result

    # 4. Acortar frases conectoras
    patterns_4 = [
        (r'aunque', 'pero'),
        (r'sin embargo', 'pero'),
        (r'no obstante', 'pero'),
        (r'a pesar de', 'pese a'),
        (r'debido a que', 'porque'),
        (r'por el hecho de que', 'porque'),
        (r'con el fin de', 'para'),
        (r'con el objetivo de', 'para'),
        (r'de manera', 'de modo'),
        (r'de forma', 'de modo'),
    ]

    for pattern, replacement in patterns_4:
        result = re.sub(pattern, replacement, result, flags=re.IGNORECASE, count=1)
        if len(result) <= target_chars and count_words(result) <= target_words:
            return result

    # 5. Reducir adjetivos redundantes en series
    patterns_5 = [
        (r'intensa\s+', ''),
        (r'significativas\s+', ''),
        (r'significativos\s+', ''),
        (r'importantes\s+', ''),
        (r'constantes\s+', ''),
        (r'frecuentes\s+', ''),
    ]

    for pattern, replacement in patterns_5:
        result = re.sub(pattern, replacement, result, count=1)
        if len(result) <= target_chars and count_words(result) <= target_words:
            return result

    # 6. Eliminar palabras de relleno
    patterns_6 = [
        (r'\s+cada pocas\s+', ' cada '),
        (r'\s+de modo\s+', ' '),
        (r'\s+de manera\s+', ' '),
    ]

    for pattern, replacement in patterns_6:
        result = re.sub(pattern, replacement, result, count=1)
        if len(result) <= target_chars and count_words(result) <= target_words:
            return result

    return result

def expand_text_minimal(text, target_words=65):
    """
    Expande el texto mínimamente para alcanzar target_words
    """
    current_words = count_words(text)
    if current_words >= target_words:
        return text

    # Por ahora retornar texto original
    # La expansión requiere análisis semántico más complejo
    return text

def get_item_text(item):
    """Obtiene el texto a analizar según el tipo de item"""
    item_type = item.get('type', 'video')
    if item_type == 'options':
        return item.get('scenario', '')
    else:
        return item.get('refactored_text', '')

def set_item_text(item, new_text):
    """Establece el texto ajustado según el tipo de item"""
    item_type = item.get('type', 'video')
    if item_type == 'options':
        item['scenario'] = new_text
    else:
        item['refactored_text'] = new_text
    return item

def analyze_item(item):
    """Analiza un item y retorna estadísticas"""
    text = get_item_text(item)
    words = count_words(text)
    chars = count_chars(text)

    needs_adjustment = False
    reason = []

    if words < 65:
        needs_adjustment = True
        reason.append(f"palabras {words}/65-80")
    elif words > 80:
        needs_adjustment = True
        reason.append(f"palabras {words}/65-80")

    if chars < 300:
        needs_adjustment = True
        reason.append(f"chars {chars}/300-380")
    elif chars > 380:
        needs_adjustment = True
        reason.append(f"chars {chars}/300-380")
        excess_pct = ((chars - 380) / chars) * 100
        reason.append(f"exceso {excess_pct:.1f}%")

    return {
        'words': words,
        'chars': chars,
        'needs_adjustment': needs_adjustment,
        'reason': ', '.join(reason) if reason else 'OK',
        'type': item.get('type', 'video')
    }

def adjust_item(item):
    """Ajusta un item para cumplir con los rangos objetivo"""
    text = get_item_text(item)
    stats = analyze_item(item)

    if not stats['needs_adjustment']:
        # Agregar campos de validación
        item['word_count'] = stats['words']
        item['char_count'] = stats['chars']
        item['length_status'] = 'ok'
        item['length_note'] = ''
        return item, False, "Ya cumple rangos"

    adjusted_text = text
    changes_made = []

    # Ajustar caracteres primero (más crítico)
    if stats['chars'] > 380 or stats['words'] > 80:
        adjusted_text = reduce_text_aggressive(adjusted_text, 380, 80)
        changes_made.append(f"Reducido: {stats['chars']}c/{stats['words']}w -> {len(adjusted_text)}c/{count_words(adjusted_text)}w")

    # Ajustar palabras si es necesario
    new_words = count_words(adjusted_text)
    if new_words < 65:
        adjusted_text = expand_text_minimal(adjusted_text, 65)
        changes_made.append(f"Expandido: {new_words}w -> {count_words(adjusted_text)}w")

    # Actualizar el item
    item = set_item_text(item, adjusted_text)

    # Agregar campos de validación
    final_words = count_words(adjusted_text)
    final_chars = count_chars(adjusted_text)

    item['word_count'] = final_words
    item['char_count'] = final_chars

    if 65 <= final_words <= 80 and 300 <= final_chars <= 380:
        item['length_status'] = 'ok'
        item['length_note'] = ''
    else:
        item['length_status'] = 'needs_manual_review'
        item['length_note'] = f'{final_words}w, {final_chars}c'

    return item, True, '; '.join(changes_made)

def process_file(file_path):
    """Procesa un archivo JSON completo"""
    print(f"\n{'='*90}")
    print(f"Procesando: {file_path}")
    print(f"{'='*90}\n")

    # Leer archivo
    with open(file_path, 'r', encoding='utf-8') as f:
        items = json.load(f)

    # Analizar todos los items primero
    print("ANALISIS INICIAL:")
    print(f"{'ID':<20} {'Tipo':<8} {'Palabras':<10} {'Caracteres':<10} {'Estado'}")
    print("-" * 90)

    for item in items:
        stats = analyze_item(item)
        status = "!" if stats['needs_adjustment'] else "OK"
        print(f"{item['id']:<20} {stats['type']:<8} {stats['words']:<10} {stats['chars']:<10} {status:<4} {stats['reason']}")

    # Procesar ajustes
    print("\n\nAJUSTES REALIZADOS:")
    print("-" * 90)

    adjusted_count = 0
    compliant_count = 0
    needs_review_count = 0

    for i, item in enumerate(items):
        adjusted_item, was_adjusted, changes = adjust_item(item)
        items[i] = adjusted_item

        if was_adjusted:
            adjusted_count += 1
            print(f"\n{item['id']} ({item.get('type', 'video')}):")
            print(f"  {changes}")
            print(f"  Final: {item['word_count']}w, {item['char_count']}c -> {item.get('length_status', 'N/A')}")

        # Contar estados finales
        if item.get('length_status') == 'ok':
            compliant_count += 1
        elif 'needs' in item.get('length_status', ''):
            needs_review_count += 1

    # Guardar archivo actualizado
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

    # Reporte final
    print(f"\n\n{'='*90}")
    print("REPORTE FINAL:")
    print(f"{'='*90}")
    print(f"Total items: {len(items)}")
    print(f"Items ajustados: {adjusted_count}/{len(items)}")
    print(f"Items OK: {compliant_count}/{len(items)}")
    print(f"Items para revision manual: {needs_review_count}/{len(items)}")
    print(f"Archivo guardado: {file_path}")
    print(f"{'='*90}\n")

    return {
        'total': len(items),
        'adjusted': adjusted_count,
        'compliant': compliant_count,
        'needs_review': needs_review_count
    }

def main():
    """Procesa los 4 archivos en orden"""
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
            result = process_file(file_path)
            all_results.append({'file': file_rel, **result})
        else:
            print(f"! Archivo no encontrado: {file_path}")

    # Reporte consolidado
    print("\n\n" + "="*90)
    print("REPORTE CONSOLIDADO DE TODOS LOS ARCHIVOS")
    print("="*90)

    total_all = 0
    adjusted_all = 0
    compliant_all = 0
    review_all = 0

    for result in all_results:
        print(f"\n{result['file']}:")
        print(f"  Items ajustados: {result['adjusted']}/{result['total']}")
        print(f"  Items OK: {result['compliant']}/{result['total']}")
        print(f"  Items para revision: {result['needs_review']}/{result['total']}")

        total_all += result['total']
        adjusted_all += result['adjusted']
        compliant_all += result['compliant']
        review_all += result['needs_review']

    print(f"\n{'='*90}")
    print("TOTALES:")
    print(f"  Items totales: {total_all}")
    print(f"  Items ajustados: {adjusted_all}")
    print(f"  Items OK: {compliant_all}")
    print(f"  Items para revision manual: {review_all}")
    print(f"{'='*90}")

if __name__ == "__main__":
    main()

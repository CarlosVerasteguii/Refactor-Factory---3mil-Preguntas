#!/usr/bin/env python3
"""
Ajuste quirúrgico de longitud para items de JSON
Objetivo: 65-80 palabras y 300-380 caracteres
"""
import json
import re
from pathlib import Path

def count_words(text):
    """Cuenta palabras en el texto"""
    words = text.split()
    return len(words)

def count_chars(text):
    """Cuenta caracteres en el texto"""
    return len(text)

def analyze_item(item):
    """Analiza un item y retorna estadísticas"""
    text = item.get('refactored_text', '')
    words = count_words(text)
    chars = count_chars(text)

    needs_adjustment = False
    reason = []

    if words < 65:
        needs_adjustment = True
        reason.append(f"palabras insuficientes ({words}/65-80)")
    elif words > 80:
        needs_adjustment = True
        reason.append(f"palabras excesivas ({words}/65-80)")

    if chars < 300:
        needs_adjustment = True
        reason.append(f"caracteres insuficientes ({chars}/300-380)")
    elif chars > 380:
        needs_adjustment = True
        reason.append(f"caracteres excesivos ({chars}/300-380)")
        # Calcular porcentaje de exceso
        excess_pct = ((chars - 380) / chars) * 100
        reason.append(f"exceso: {excess_pct:.1f}%")

    return {
        'words': words,
        'chars': chars,
        'needs_adjustment': needs_adjustment,
        'reason': ', '.join(reason) if reason else 'OK'
    }

def adjust_text_reduce(text, target_chars=380):
    """
    Reduce el texto manteniendo estructura y significado.
    Estrategia: eliminar palabras redundantes, simplificar frases
    """
    current_chars = len(text)
    if current_chars <= target_chars:
        return text

    # Calcular reducción necesaria
    reduction_pct = ((current_chars - target_chars) / current_chars)

    # Estrategias de reducción (de menos a más agresivas)

    # 1. Eliminar palabras redundantes comunes
    redundant_patterns = [
        (r'\s+muy\s+', ' '),
        (r'\s+bastante\s+', ' '),
        (r'\s+realmente\s+', ' '),
        (r'\s+en realidad\s+', ' '),
        (r'\s+de verdad\s+', ' '),
    ]

    # 2. Simplificar expresiones comunes
    simplifications = [
        (r'todo el mundo', 'todos'),
        (r'cada uno de', 'cada'),
        (r'en este momento', 'ahora'),
        (r'en la actualidad', 'ahora'),
        (r'por el hecho de que', 'porque'),
        (r'debido a que', 'porque'),
        (r'a pesar de que', 'aunque'),
        (r'con el fin de', 'para'),
        (r'hacer referencia a', 'referir'),
        (r'tener en cuenta', 'considerar'),
        (r'llevar a cabo', 'hacer'),
        (r'poner en marcha', 'iniciar'),
    ]

    result = text

    # Aplicar reducciones gradualmente
    for pattern, replacement in redundant_patterns + simplifications:
        result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
        if len(result) <= target_chars:
            return result

    # Si aún es muy largo, reducir conectores y artículos donde sea posible
    if len(result) > target_chars:
        # Reducir "y" repetidas
        result = re.sub(r',\s+y\s+', ', ', result)

    return result

def adjust_text_expand(text, target_words=65):
    """
    Expande el texto manteniendo coherencia.
    Estrategia: agregar detalles contextuales relevantes
    """
    current_words = count_words(text)
    if current_words >= target_words:
        return text

    # Necesitamos agregar palabras estratégicamente
    # Por ahora, retornar el texto original
    # (La expansión requiere análisis semántico más profundo)
    return text

def adjust_item(item):
    """Ajusta un item para cumplir con los rangos objetivo"""
    text = item.get('refactored_text', '')
    stats = analyze_item(item)

    if not stats['needs_adjustment']:
        return item, False, "Ya cumple rangos"

    adjusted_text = text
    changes_made = []

    # Primero ajustar caracteres (más crítico)
    if stats['chars'] > 380:
        adjusted_text = adjust_text_reduce(adjusted_text, 380)
        changes_made.append(f"Reducido de {stats['chars']} a {len(adjusted_text)} chars")

    # Luego verificar palabras
    new_words = count_words(adjusted_text)
    new_chars = count_chars(adjusted_text)

    if new_words < 65:
        adjusted_text = adjust_text_expand(adjusted_text, 65)
        changes_made.append(f"Expandido de {new_words} a {count_words(adjusted_text)} palabras")

    # Actualizar el item
    item['refactored_text'] = adjusted_text

    # Agregar campos de validación si no existen
    item['word_count'] = count_words(adjusted_text)
    item['char_count'] = count_chars(adjusted_text)

    # Verificar si ahora cumple
    final_words = item['word_count']
    final_chars = item['char_count']

    if 65 <= final_words <= 80 and 300 <= final_chars <= 380:
        item['length_status'] = 'ok'
        item['length_note'] = ''
    else:
        item['length_status'] = 'needs_review'
        item['length_note'] = f'Palabras: {final_words}, Caracteres: {final_chars}'

    return item, True, '; '.join(changes_made)

def process_file(file_path):
    """Procesa un archivo JSON completo"""
    print(f"\n{'='*80}")
    print(f"Procesando: {file_path}")
    print(f"{'='*80}\n")

    # Leer archivo
    with open(file_path, 'r', encoding='utf-8') as f:
        items = json.load(f)

    # Analizar todos los items primero
    print("ANÁLISIS INICIAL:")
    print(f"{'ID':<20} {'Palabras':<12} {'Caracteres':<12} {'Estado'}")
    print("-" * 80)

    for item in items:
        stats = analyze_item(item)
        status_icon = "!" if stats['needs_adjustment'] else "OK"
        print(f"{item['id']:<20} {stats['words']:<12} {stats['chars']:<12} {status_icon:<4} {stats['reason']}")

    # Procesar ajustes
    print("\n\nAJUSTES REALIZADOS:")
    print("-" * 80)

    adjusted_count = 0
    compliant_count = 0
    needs_review_count = 0

    for i, item in enumerate(items):
        adjusted_item, was_adjusted, changes = adjust_item(item)
        items[i] = adjusted_item

        if was_adjusted:
            adjusted_count += 1
            print(f"\n{item['id']}:")
            print(f"  {changes}")
            print(f"  Final: {item['word_count']} palabras, {item['char_count']} caracteres")
            print(f"  Estado: {item.get('length_status', 'N/A')}")

        # Contar estados finales
        if item.get('length_status') == 'ok':
            compliant_count += 1
        elif item.get('length_status') == 'needs_review':
            needs_review_count += 1

    # Guardar archivo actualizado
    output_path = file_path
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

    # Reporte final
    print(f"\n\n{'='*80}")
    print("REPORTE FINAL:")
    print(f"{'='*80}")
    print(f"Total de items: {len(items)}")
    print(f"Items ajustados: {adjusted_count}/{len(items)}")
    print(f"Items que cumplen: {compliant_count}/{len(items)}")
    print(f"Items que necesitan revisión: {needs_review_count}/{len(items)}")
    print(f"Archivo guardado: {output_path}")
    print(f"{'='*80}\n")

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
    print("\n\n" + "="*80)
    print("REPORTE CONSOLIDADO DE TODOS LOS ARCHIVOS")
    print("="*80)

    for result in all_results:
        print(f"\n{result['file']}:")
        print(f"  Items ajustados: {result['adjusted']}/{result['total']}")
        print(f"  Items que cumplen: {result['compliant']}/{result['total']}")
        print(f"  Items que necesitan revisión: {result['needs_review']}/{result['total']}")

if __name__ == "__main__":
    main()

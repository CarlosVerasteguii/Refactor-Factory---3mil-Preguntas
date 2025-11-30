#!/usr/bin/env python3
"""Add minimal words to frozen items to reach 60-80 range."""
import json

# Load current batch
with open('01_processed_json/module1/block-B01/batch-02.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Surgical fixes for each frozen item
fixes = {
    'block-B01-q012': {
        'old': 'Puedes usar un descuento especial de la empresa para obtener beneficio economico personal; no esta prohibido de modo claro y varios compañeros lo usan sin ver consecuencias.',
        'new': 'Puedes usar un descuento especial de la empresa para obtener beneficio economico personal importante; no esta prohibido de modo claro y varios compañeros lo usan sin ver consecuencias visibles.'
    },
    'block-B01-q013': {
        'old': 'Al revisar equipos ves que puedes usarlos fuera de horario para proyecto personal que te daria un ingreso extra notable; no hay regla clara y tu supervisor no esta.',
        'new': 'Al revisar equipos de la empresa ves que puedes usarlos fuera de horario para proyecto personal que te daria un ingreso extra notable; no hay regla clara y tu supervisor no esta.'
    },
    'block-B01-q015': {
        'old': 'Te asignan revisar datos confidenciales de situacion donde esta involucrada persona cercana a ti; tu supervisor sabe de la relacion pero insiste porque confia en tu criterio y no hay tiempo para reasignar.',
        'new': 'Te asignan revisar datos confidenciales de una situacion delicada donde esta involucrada una persona cercana a ti; tu supervisor sabe de la relacion pero insiste porque confia en tu criterio y no hay tiempo para reasignar.'
    },
    'block-B01-q016': {
        'old': 'Al revisar como se registran los gastos ves una forma de reportarlos que sin mentir hace que parezcan mas justificados de lo real; varios compañeros ya lo usan sin que nadie intervenga.',
        'new': 'Al revisar como se registran los gastos ves una forma de reportarlos que sin mentir directamente hace que parezcan mas justificados de lo real; varios compañeros ya lo usan sin que nadie intervenga.'
    },
    'block-B01-q017': {
        'old': 'Al preparar un reporte para la direccion ves que los datos se pueden presentar mostrando toda la dificultad o suavizandola resaltando solo lo positivo; el plazo es ajustado y tu supervisor no esta.',
        'new': 'Al preparar un reporte de resultados para la direccion ves que los datos se pueden presentar mostrando toda la dificultad o suavizandola resaltando solo lo positivo; el plazo es ajustado y tu supervisor no esta.'
    },
    'block-B01-q018': {
        'old': 'Te piden repartir un presupuesto entre dos proyectos:',
        'new': 'Te piden repartir un presupuesto limitado entre dos proyectos:'
    },
    'block-B01-q020': {
        'old': 'Te piden repartir carga haciendo que algunos reciban',
        'new': 'Te piden repartir carga de trabajo haciendo que algunos reciban'
    }
}

# Apply fixes
for item in items:
    item_id = item['id']
    if item_id in fixes:
        fix = fixes[item_id]
        old_text = item['refactored_text']
        new_text = old_text.replace(fix['old'], fix['new'])

        if new_text != old_text:
            item['refactored_text'] = new_text
            # Recalculate
            item['word_count'] = len(new_text.split())
            item['char_count'] = len(new_text)

            # Update status
            if 60 <= item['word_count'] <= 80 and 300 <= item['char_count'] <= 380:
                item['length_status'] = 'ok'
                item['length_note'] = f"words={item['word_count']} chars={item['char_count']} in range"
                item['notes'] = f"Fixed - added words to reach 60"
                print(f"[FIXED] {item_id}: w={item['word_count']} c={item['char_count']}")
            else:
                print(f"[STILL FROZEN] {item_id}: w={item['word_count']} c={item['char_count']}")
        else:
            print(f"[NO CHANGE] {item_id}: pattern not found")

# Save
with open('01_processed_json/module1/block-B01/batch-02.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

# Final validation
frozen = sum(1 for i in items if i['length_status'] == 'frozen')
print("-" * 60)
if frozen == 0:
    print("SUCCESS: All 10/10 items validated!")
else:
    print(f"INCOMPLETE: {frozen}/10 still frozen")

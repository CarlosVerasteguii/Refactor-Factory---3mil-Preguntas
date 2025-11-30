import json

def count_stats(text):
    return len(text.split()), len(text)

items_data = [
    {
        "id": "block-B05-q001",
        "base": "En las pruebas finales detectas una falla de seguridad rara que expondrá datos de clientes. Si pausas el lanzamiento para corregirla, el plan se retrasará semanas, tu jefe se enfadará y te culparán por frenar las metas. Si la minimizas, el producto saldrá a tiempo y quedarás bien, pero los usuarios estarán en riesgo.",
        "endings": [
            "¿Asumes el costo de frenar todo o proteges tu imagen?",
            "¿Priorizas la seguridad del usuario o tu propia reputación?",
            "¿Qué decides: proteger al usuario o cumplir la meta?"
        ]
    },
    {
        "id": "block-B05-q002",
        "base": "Tu empresa abrirá una planta que dará empleo pero aumentará la contaminación local cumpliendo la ley. Te piden hablar con la comunidad. Si explicas los riesgos reales, generarás rechazo, retrasarás la obra y arriesgarás tu evaluación. Si repites solo el discurso positivo, el plan avanza sin ruido pero las familias decidirán sin entender el daño posible.",
        "endings": [
            "¿Dices toda la verdad o aseguras el éxito del proyecto?",
            "¿Priorizas la transparencia o proteges tu carrera?",
            "¿Qué decides: honestidad total o cumplir con la empresa?"
        ]
    },
    {
        "id": "block-B05-q003",
        "base": "Tu jefe sugiere contratar a una candidata de grupo minoritario por diversidad. Está calificada pero tiene menos experiencia que otro. Si la eliges, dirán que no fue la mejor y enfrentarás duras críticas. Si eliges al experto, quedas bien pero pierdes la chance de corregir un sesgo.",
        "endings": [
            "¿Asumes el riesgo por la diversidad o vas a lo seguro?",
            "¿Qué priorizas: la equidad o evitarte problemas?",
            "¿Decides corregir el sesgo o proteger tu reputación?"
        ]
    },
    {
        "id": "block-B05-q004",
        "base": "La empresa ahorraría cambiando a un proveedor que usa trabajo infantil legal en su país, pero contrario a tus valores. Si te opones y buscas otra opción, parecerás ingenuo, frenarás el ahorro y perderás ascensos. Si apoyas al proveedor por cumplir la ley local, el presupuesto mejora pero avalas el daño a esos niños.",
        "endings": [
            "¿Defiendes tus valores o aseguras el resultado financiero?",
            "¿Qué decides: ética global o beneficio económico?",
            "¿Te opones al ahorro o aceptas el costo ético?"
        ]
    },
    {
        "id": "block-B05-q005",
        "base": "Implementas un sistema que causará despidos. La regla pide avisar dos semanas antes. Si propones un plan gradual, retrasas todo, generas costos y molestas a tu jefe. Si ejecutas rápido, cumples con dirección, pero tu equipo se sentirá traicionado al enterarse tarde.",
        "endings": [
            "¿Proteges a tu equipo o cumples la orden de arriba?",
            "¿Qué priorizas: la lealtad al equipo o la eficiencia?",
            "¿Asumes el conflicto o ejecutas la orden directa?"
        ]
    },
    {
        "id": "block-B05-q006",
        "base": "La empresa descontinuará un producto clave para clientes pequeños. La orden es esperar para comunicar la noticia y no perder ventas. Si avisas en privado, incumples la directiva y afectas tu bono. Si callas y vendes, cumples metas, pero los dejas sin tiempo para reaccionar y tendrán serios problemas.",
        "endings": [
            "¿Rompes la regla para ayudar o proteges tu bono?",
            "¿Qué decides: lealtad al cliente o a la empresa?",
            "¿Avisas a riesgo de tu bono o callas para cumplir?"
        ]
    },
    {
        "id": "block-B05-q007",
        "base": "Marketing propone una campaña que exagera beneficios. Es legal, pero los clientes lo tomarán como promesa literal. Si exiges ajustar el mensaje, retrasas el lanzamiento, chocas con marketing y afectas tus metas. Si la apruebas, impulsas las cifras y la imagen de éxito, pero aceptas que los clientes se sientan engañados.",
        "endings": [
            "¿Frenas la campaña o aceptas el engaño por la meta?",
            "¿Qué priorizas: la verdad o el éxito comercial?",
            "¿Defiendes al cliente o aseguras tus resultados?"
        ]
    },
    {
        "id": "block-B05-q008",
        "base": "Un nuevo empleado te ofrece planes confidenciales de su antigua empresa para demostrar lealtad. La política lo prohíbe, pero a tu jefe le interesa. Si rechazas y reportas, tensas el ambiente y pareces rígido. Si aceptas el archivo en silencio, obtienes una ventaja clave, pero cruzas una línea ética clara.",
        "endings": [
            "¿Sigues la regla o aprovechas la ventaja sucia?",
            "¿Qué decides: integridad o ventaja competitiva?",
            "¿Rechazas la info o la usas para ganar?"
        ]
    },
    {
        "id": "block-B05-q009",
        "base": "Tu empresa y un competidor planean producir juntos para reducir costos. Es legal, pero crearía un monopolio con precios más altos. Si te opones, frenas un ahorro clave e irritas a la dirección. Si apoyas el acuerdo, mejoras los números hoy, pero contribuyes a un mercado injusto para los clientes.",
        "endings": [
            "¿Te opones al monopolio o aseguras el ahorro?",
            "¿Qué priorizas: mercado justo o beneficio interno?",
            "¿Frenas el acuerdo o impulsas los números?"
        ]
    },
    {
        "id": "block-B05-q010",
        "base": "En tu farmacéutica, un estudio interno sugiere riesgos graves de un medicamento. La política es esperar a los reguladores. Si presionas para advertir ya, enfrentas represalias y arriesgas tu puesto. Si callas y sigues el protocolo, proteges tu carrera hoy, pero mantienes a los pacientes expuestos al riesgo sin saberlo.",
        "endings": [
            "¿Arriesgas tu puesto por la seguridad o callas?",
            "¿Qué decides: proteger pacientes o tu carrera?",
            "¿Rompes el protocolo o te proteges a ti mismo?"
        ]
    }
]

def generate_best_options():
    final_items = []
    
    # Load original to keep metadata
    try:
        with open("01_processed_json/module3/block-B05/batch-01.json", 'r', encoding='utf-8') as f:
            originals = {item['id']: item for item in json.load(f)}
    except:
        originals = {}

    print(f"{'ID':<15} {'Words':<5} {'Chars':<5} {'Text'}")
    print("-" * 80)

    for item_data in items_data:
        best_text = None
        best_stats = None
        
        # Try endings
        for ending in item_data['endings']:
            text = f"{item_data['base']} {ending}"
            w, c = count_stats(text)
            
            if 65 <= w <= 80 and 300 <= c <= 380:
                best_text = text
                best_stats = (w, c)
                break # Found a valid one
        
        # If no ending worked, try to adjust base slightly (manual fallback logic would go here, 
        # but for this script we just pick the closest if none match, or the first valid one)
        
        if not best_text:
             # Fallback: pick the first one and print warning
             text = f"{item_data['base']} {item_data['endings'][0]}"
             w, c = count_stats(text)
             best_text = text
             best_stats = (w, c)
             print(f"WARNING: {item_data['id']} out of range: {w}w, {c}c")

        print(f"{item_data['id']:<15} {best_stats[0]:<5} {best_stats[1]:<5} {best_text[:50]}...")
        
        # Construct item
        orig = originals.get(item_data['id'], {})
        new_item = orig.copy()
        new_item.update({
            "id": item_data['id'],
            "module_id": 3,
            "block_id": "B05",
            "type": "video",
            "refactored_text": best_text,
            "word_count": best_stats[0],
            "char_count": best_stats[1],
            "length_status": "ok" if (65 <= best_stats[0] <= 80 and 300 <= best_stats[1] <= 380) else "manual",
            "length_note": "" if (65 <= best_stats[0] <= 80 and 300 <= best_stats[1] <= 380) else f"{best_stats[0]}w, {best_stats[1]}c",
            "audit_status": "ok",
            "audit_notes": "Refactored for naturalness and length."
        })
        final_items.append(new_item)

    # Write output
    with open("01_processed_json/module3/block-B05/batch-01.json", 'w', encoding='utf-8') as f:
        json.dump(final_items, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    generate_best_options()

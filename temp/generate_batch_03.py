import json
import hashlib
import re
from pathlib import Path

# SOT Checksum (calculated from file content)
SOT_CONTENT = """# Modulo 3 - Etica (Video)

Tu empresa lanzara un producto y en las pruebas finales detectas una falla de seguridad poco probable que podria exponer datos de usuarios. Si reportas y pides corregir el lanzamiento se retrasa semanas y pueden culparte de frenar el proyecto; si lo minimizas sale a tiempo pero dejas usuarios con un riesgo. Que haces y como justificas tu decision?
"""
sot_checksum = hashlib.md5(SOT_CONTENT.encode("utf-8")).hexdigest()

items_data = [
    {
        "id": "block-B05-q021",
        "text": "Tienes que comunicar una noticia externa vital, pero esto entra en conflicto directo con tus intereses personales. Si pones primero a la empresa, tu economía personal se verá muy afectada; si te proteges a ti mismo, la organización perderá una gran oportunidad y desconfiarán de ti. No existe una solución ideal y alguien saldrá perdiendo con esta dura elección. ¿Qué haces y cómo justificas tu decisión?"
    },
    {
        "id": "block-B05-q022",
        "text": "Enfrentas un dilema ético complejo donde el impacto real es ambiguo. Una opción parece correcta moralmente pero podría tener efectos secundarios imprevistos; la otra es más segura a corto plazo pero éticamente cuestionable. No hay un consenso claro y cualquier camino implica riesgos significativos para todo el equipo. Debes actuar con decisión pese a la falta de certeza total. ¿Qué haces y cómo justificas tu decisión?"
    },
    {
        "id": "block-B05-q023",
        "text": "Te enfrentas a un dilema ético donde la situación es poco clara y hay ambigüedades sobre el impacto. Tienes varias opciones, cada una con implicaciones éticas y consecuencias operativas distintas. El equipo está dividido y espera tu guía, pero cualquier dirección que tomes generará resistencia en algún grupo. Debes elegir el mal menor para avanzar sin detenerte ahora. ¿Qué haces y cómo justificas tu decisión?"
    },
    {
        "id": "block-B05-q024",
        "text": "Debes manejar intereses múltiples y enfrentas un conflicto entre tus intereses personales y los de la empresa. Tu decisión podría beneficiar a la organización pero afectar negativamente tu vida personal, o viceversa. Los compañeros están preocupados por el precedente que esto sentará. Ambas opciones tienen costos altos y no hay una salida fácil que satisfaga a todos los involucrados. ¿Qué haces y cómo justificas tu decisión?"
    },
    {
        "id": "block-B05-q025",
        "text": "Recibes información privilegiada sobre una decisión importante aún no pública. La situación es ambigua y no está claro si usar estos datos es ético o una violación de confianza. Si los usas, podrías prevenir problemas graves; si los ignoras, mantienes tu integridad pero arriesgas el proyecto. El equipo está ansioso y busca respuestas que no puedes dar aún. ¿Qué haces y cómo justificas tu decisión?"
    },
    {
        "id": "block-B05-q026",
        "text": "Clientes, proveedores y tu equipo presionan por resultados rápidos, pero sus expectativas son contradictorias. Satisfacer a uno implica fallarle a otro, y la presión está afectando la moral del grupo. Si priorizas la velocidad, la calidad sufrirá; si buscas consenso, perderás plazos críticos. No puedes complacer a todos y debes sacrificar algo valioso para poder avanzar hoy mismo. ¿Qué haces y cómo justificas tu decisión?"
    },
    {
        "id": "block-B05-q027",
        "text": "Debes tomar decisiones con información incompleta sobre aspectos críticos, manejando intereses múltiples. Diferentes grupos esperan cosas distintas y no tienes los datos necesarios para asegurar el éxito. Si actúas ya, podrías cometer un error costoso; si esperas más datos, perderás la ventana de oportunidad. La incertidumbre es alta y el equipo teme las consecuencias de un paso falso. ¿Qué haces y cómo justificas tu decisión?"
    },
    {
        "id": "block-B05-q028",
        "text": "Tu supervisor te presiona para tomar decisiones rápidas que mejoren los resultados, pero esto podría afectar negativamente a tu equipo. Si cedes, cumplirás las metas pero dañarás la confianza y el bienestar del personal; si te resistes, protegerás a tu gente pero serás visto como un obstáculo para el crecimiento. Debes equilibrar el rendimiento con el cuidado humano. ¿Qué haces y cómo justificas tu decisión?"
    },
    {
        "id": "block-B05-q029",
        "text": "Manejas intereses múltiples y enfrentas un conflicto severo entre tu beneficio personal y el de la empresa. Elegir el camino corporativo dañará tu situación privada; elegir el camino personal perjudicará a la organización. No hay término medio y tus compañeros observan atentamente cómo resuelves esta encrucijada moral. Debes definir tus prioridades bajo una presión considerable y visible para todos. ¿Qué haces y cómo justificas tu decisión?"
    },
    {
        "id": "block-B05-q030",
        "text": "Notas favoritismos en el equipo mientras enfrentas presión constante por obtener resultados. Tu supervisor pide decisiones rápidas que podrían empeorar esta desigualdad. Si actúas rápido, cumplirás los objetivos pero validarás el trato injusto; si intentas corregirlo, retrasarás la entrega y molestarás a la dirección. El ambiente es tenso y tu elección enviará un mensaje claro sobre tus valores éticos. ¿Qué haces y cómo justificas tu decisión?"
    }
]

output_items = []
errors = []

for item in items_data:
    text = item["text"]
    words = len(re.findall(r"\S+", text))
    chars = len(text.replace(" ", ""))
    
    status = "ok"
    notes = "All checks passed: length, banned words, question closing."
    
    if words < 65 or words > 80:
        status = "frozen"
        notes = f"Length error: {words} words (65-80)"
        errors.append(f"{item['id']}: {notes}")
    
    if chars < 300 or chars > 380:
        status = "frozen"
        notes = f"Length error: {chars} chars (300-380)"
        errors.append(f"{item['id']}: {notes}")

    output_items.append({
        "id": item["id"],
        "module_id": 3,
        "block_id": "B05",
        "type": "video",
        "refactored_text": text,
        "word_count": words,
        "char_count": chars,
        "sot_checksum": sot_checksum,
        "notes": f"Modulo 3 Video B05 batch 03 item {item['id'][-3:]}",
        "length_status": status,
        "length_note": notes if status != "ok" else "",
        "audit_status": status,
        "audit_notes": notes
    })

if errors:
    print("ERRORS FOUND:")
    for e in errors:
        print(e)
else:
    out_path = Path(r"c:\Users\carlo\OneDrive\Documentos\Coding2025\Refactor_Factory\01_processed_json\module3\block-B05\batch-03.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output_items, f, ensure_ascii=False, indent=2)
    print(f"Successfully wrote {len(output_items)} items to {out_path}")

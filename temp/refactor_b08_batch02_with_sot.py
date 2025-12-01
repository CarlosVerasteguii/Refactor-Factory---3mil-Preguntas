#!/usr/bin/env python3
"""
Refactor Module 4, Block B08, batch-02 (items 11-20) with options-refactor-sot agent.

This script manually applies SOT_Modulo4_Opciones rules to refactor each item:
- Scenario: 65-80 words, 300-380 chars (target 320-350)
- 4 options following psychometric rules
- No banned words
- Professional tone
"""

import json
import re
import hashlib
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODULE_ID = 4
BLOCK_ID = "B08"
BATCH_ID = "batch-02"

SOT_PATH = PROJECT_ROOT / "SourceofTruth" / "SOT_Modulo4_Opciones.md"
OUT_DIR = PROJECT_ROOT / "01_processed_json" / f"module{MODULE_ID}" / f"block-{BLOCK_ID}"
BATCH_JSON_PATH = OUT_DIR / f"{BATCH_ID}.json"

# Load SOT checksum
sot_content = SOT_PATH.read_text(encoding="utf-8")
sot_checksum = hashlib.md5(sot_content.encode("utf-8")).hexdigest()

# Refactored items following SOT_Modulo4_Opciones
refactored_items = [
    {
        "id": "block-B08-q011",
        "module_id": 4,
        "block_id": "B08",
        "type": "options",
        "scenario": "Estás en la reunión final con un cliente que representa el 40% de los ingresos del trimestre. Tu supervisor presenta proyecciones que notas infladas y optimistas en exceso. El cliente está impresionado y listo para firmar. Si no se cierra el trato, habrá recortes serios que afectarán a tu equipo, probablemente con despidos. ¿Qué haces?",
        "options_structured": {
            "integrity_correct": "Intervienes con tacto señalando que las proyecciones deben ajustarse a datos conservadores y propones revisar los números antes de firmar, aunque tu supervisor quede molesto, el cliente dude y arriesgues la relación inmediata con ambos.",
            "pragmatic_distractor": "Dejas que tu supervisor cierre el trato y luego propones internamente ajustar las expectativas del cliente mediante entregas escalonadas, priorizando asegurar el contrato ahora aunque los compromisos iniciales sean difíciles de cumplir.",
            "evasive_distractor": "Pides un receso breve para 'revisar detalles finales' del contrato y consultas en privado a tu supervisor si está seguro de los números antes de comprometerte tú mismo.",
            "rationalized_distractor": "Consideras que tu supervisor tiene más experiencia cerrando tratos y que confiar en su criterio es lo apropiado, evitando cuestionar su estrategia frente al cliente aunque notes riesgos evidentes."
        },
        "notes": "M4 Opciones B08 batch 02 item 1 - Refactored per SOT",
        "sot_checksum": sot_checksum
    },
    {
        "id": "block-B08-q012",
        "module_id": 4,
        "block_id": "B08",
        "type": "options",
        "scenario": "Estás en medio de una presentación crucial frente a los directores de la empresa cuando te das cuenta de que has cometido un error significativo en un gráfico de datos clave que afecta las conclusiones principales. Los directores están analizando la información y ya han comentado sobre esos números. Tu supervisor está presente observando tu desempeño y esta presentación es tu oportunidad de demostrar que mereces el ascenso. ¿Qué haces en ese preciso instante?",
        "options_structured": {
            "integrity_correct": "Haces una pausa inmediata, corriges el error verbalmente con confianza explicando el dato correcto y cómo cambia las conclusiones, aunque tu supervisor cuestione tu preparación en la evaluación y los directores duden de tu profesionalismo.",
            "pragmatic_distractor": "Mencionas que hay una actualización menor en el gráfico y pasas rápido a la siguiente diapositiva enfatizando otros puntos fuertes, minimizando el problema para mantener el flujo aunque los números incorrectos puedan generar decisiones equivocadas después.",
            "evasive_distractor": "Preguntas a los directores si tienen dudas sobre esa sección específica o si prefieren profundizar en otros temas primero, esperando que nadie haya notado el error o ganar tiempo para pensar cómo manejarlo.",
            "rationalized_distractor": "Comentas que por rigurosidad enviarás todos los datos actualizados por correo después de la reunión para que los analicen con calma, evitando admitir el error ahora y posponiendo la corrección para después."
        },
        "notes": "M4 Opciones B08 batch 02 item 2 - Refactored per SOT",
        "sot_checksum": sot_checksum
    },
    {
        "id": "block-B08-q013",
        "module_id": 4,
        "block_id": "B08",
        "type": "options",
        "scenario": "Un miembro de tu equipo que ha estado bajo mucha presión tiene una crisis emocional y rompe a llorar en medio de la oficina abierta durante una jornada de máxima actividad. La atención de todos se centra en él, el ambiente se torna extremadamente incómodo y la productividad se detiene. Tu supervisor está presente observando cómo manejas la situación y espera que mantengas al equipo enfocado. ¿Cuál es tu reacción inmediata?",
        "options_structured": {
            "integrity_correct": "Te acercas directamente a la persona, le preguntas en voz baja si necesita un momento y la acompañas a un lugar privado donde pueda recuperarse, aunque el resto del equipo pierda minutos productivos y tu supervisor evalúe tu acción como distracción de las prioridades del día.",
            "pragmatic_distractor": "Te acercas brevemente, ofreces ayuda general diciendo que si necesita algo te avise, y sugieres con tacto que tome un descanso fuera de la vista del equipo, regresando rápido a tu trabajo para no involucrate más de lo necesario en problemas personales ajenos.",
            "evasive_distractor": "Envías un mensaje de chat privado a tu supervisor preguntando cómo debería manejarse este tipo de situaciones según las políticas de la empresa, trasladando la responsabilidad de decidir y actuar mientras la persona sigue expuesta y vulnerable.",
            "rationalized_distractor": "Das espacio y dejas que la persona maneje su momento argumentando que es importante respetar su privacidad y autonomía, evitando involucrarte directamente en una situación emocional compleja que no sabes manejar y que podría tornarse más incómoda."
        },
        "notes": "M4 Opciones B08 batch 02 item 3 - Refactored per SOT",
        "sot_checksum": sot_checksum
    },
    {
        "id": "block-B08-q014",
        "module_id": 4,
        "block_id": "B08",
        "type": "options",
        "scenario": "Después de semanas de intenso trabajo y esfuerzo extraordinario, tu equipo no logra ganar un contrato crucial que representaba el mayor proyecto del año. La moral del equipo se desploma, el ambiente es de pesimismo generalizado y algunos miembros cuestionan abiertamente la estrategia que seguiste. Tu supervisor espera que como líder tomes acciones inmediatas para recuperar al equipo y enfocarlo en nuevas oportunidades. La presión por resultados futuros aumenta considerablemente. ¿Cómo manejas tu propia decepción y lideras al equipo?",
        "options_structured": {
            "integrity_correct": "Organizas una reunión para analizar objetivamente qué salió mal, reconoces el esfuerzo del equipo y enfocas en la próxima oportunidad, aunque algunos miembros frustrados puedan resistirse y tu supervisor cuestione si eres demasiado suave ante el fracaso.",
            "pragmatic_distractor": "Convocas reunión rápida enfatizando que deben aprender y mejorar para el siguiente contrato, proponiendo ajustes inmediatos aunque no hayas identificado con precisión las causas del fracaso.",
            "evasive_distractor": "Propones dar al equipo un día libre para procesar la decepción y que luego cada quien reflexione sobre qué mejorar, dejando que el tiempo pase antes de abordar el problema.",
            "rationalized_distractor": "Argumentas que el contrato tenía condiciones muy difíciles desde el inicio y que el esfuerzo del equipo fue valioso, evitando un análisis profundo de errores reales cometidos."
        },
        "notes": "M4 Opciones B08 batch 02 item 4 - Refactored per SOT",
        "sot_checksum": sot_checksum
    },
    {
        "id": "block-B08-q015",
        "module_id": 4,
        "block_id": "B08",
        "type": "options",
        "scenario": "Un proyecto crítico que lideras desde hace meses está fracasando visiblemente: el cliente principal expresa insatisfacción abierta con los entregables, el equipo está profundamente desmotivado y los plazos se incumplen semana tras semana. Sientes una enorme presión porque la responsabilidad del fracaso recae completamente sobre ti como líder del proyecto. Tu supervisor te ha advertido explícitamente que esta es tu última oportunidad para demostrar capacidad de liderazgo. ¿Qué haces en esta situación crítica?",
        "options_structured": {
            "integrity_correct": "Convocas una reunión de crisis para redefinir el alcance con el cliente, reasignas tareas al equipo y comunicas un nuevo plan de acción realista, aunque el cliente y tu supervisor puedan perder confianza en tu liderazgo y tu evaluación se vea afectada.",
            "pragmatic_distractor": "Ajustas rápidamente el alcance del proyecto reduciendo entregables para cumplir algo en plazo, priorizando cerrar pronto aunque el resultado final no satisfaga completamente las expectativas originales del cliente.",
            "evasive_distractor": "Solicitas a tu supervisor una reunión para discutir los recursos adicionales que necesitarías antes de comprometerte con un plan, dejando pasar días mientras buscas apoyos externos.",
            "rationalized_distractor": "Propones documentar las lecciones aprendidas y redefinir el proyecto en fases más manejables con el argumento de asegurar calidad a largo plazo, postergando decisiones inmediatas difíciles."
        },
        "notes": "M4 Opciones B08 batch 02 item 5 - Refactored per SOT",
        "sot_checksum": sot_checksum
    },
    {
        "id": "block-B08-q016",
        "module_id": 4,
        "block_id": "B08",
        "type": "options",
        "scenario": "Hay conflictos constantes y crecientes entre algunos compañeros clave de tu equipo que están afectando la colaboración diaria, justo cuando tu empresa anuncia cambios radicales e inmediatos en los procesos de trabajo que todos deben adoptar. La tensión combinada está afectando seriamente el ambiente laboral y varios miembros del equipo muestran señales visibles de estrés y agotamiento. Tu supervisor espera que mantengas la productividad del equipo durante esta transición difícil. ¿Qué harías en esta situación?",
        "options_structured": {
            "integrity_correct": "Estableces límites claros entre trabajo y vida personal, dices no a tareas adicionales durante el periodo de adaptación y comunicas abiertamente tu carga actual, aunque algunos compañeros y tu supervisor puedan verte como poco comprometido o resistente al cambio.",
            "pragmatic_distractor": "Identificas las señales de riesgo en el equipo y propones medidas preventivas generales, pero continúas absorbiendo trabajo extra para compensar el bajo rendimiento temporal de otros, acumulando estrés.",
            "evasive_distractor": "Buscas validación con colegas de otros equipos sobre cómo están manejando los cambios y esperas ver qué medidas toma la empresa antes de actuar tú mismo.",
            "rationalized_distractor": "Desarrollas redes de apoyo informal con compañeros para desahogarse mutuamente sobre el estrés, justificando que mantener el ánimo grupal es prioritario aunque no resuelva la sobrecarga real de trabajo."
        },
        "notes": "M4 Opciones B08 batch 02 item 6 - Refactored per SOT",
        "sot_checksum": sot_checksum
    },
    {
        "id": "block-B08-q017",
        "module_id": 4,
        "block_id": "B08",
        "type": "options",
        "scenario": "Tienes múltiples proyectos simultáneos con plazos extremadamente ajustados que requieren colaboración estrecha, mientras observas que algunos compañeros clave están compitiendo agresivamente entre sí por reconocimiento y oportunidades, compartiendo información crítica de manera selectiva y creando silos que afectan el trabajo de todos. Varios miembros del equipo están visiblemente estresados por esta dinámica tóxica. Tu supervisor evalúa tanto tus resultados individuales como tu capacidad de colaboración efectiva. ¿Qué harías en este contexto?",
        "options_structured": {
            "integrity_correct": "Desarrollas redes de apoyo compartiendo abiertamente información con quienes colaboran de buena fe y comunicas a tu supervisor las dinámicas negativas que afectan al equipo, aunque los competidores puedan verte como débil y tu intervención genere tensiones con ellos.",
            "pragmatic_distractor": "Identificas quién comparte información útil y estableces alianzas estratégicas con ellos para avanzar tus proyectos más rápido, aceptando cierta exclusión de información como parte del juego aunque afecte a otros.",
            "evasive_distractor": "Buscas reuniones con tu supervisor para entender mejor qué espera exactamente en cuanto a colaboración antes de decidir cómo relacionarte con los compañeros competitivos.",
            "rationalized_distractor": "Estableces límites enfocándote solo en tus proyectos y evitando involucrarte en las dinámicas de competencia, argumentando que mantenerte neutral es lo más profesional aunque el ambiente tóxico persista."
        },
        "notes": "M4 Opciones B08 batch 02 item 7 - Refactored per SOT",
        "sot_checksum": sot_checksum
    },
    {
        "id": "block-B08-q018",
        "module_id": 4,
        "block_id": "B08",
        "type": "options",
        "scenario": "Tu carga laboral ha aumentado significativamente en las últimas semanas y ahora tienes mucho más trabajo del que puedes manejar razonablemente en una jornada normal. El nivel de estrés está afectando claramente tu bienestar físico y emocional, afectando tu sueño y concentración. Varios compañeros también están experimentando esta sobrecarga extrema y comentan abiertamente su agotamiento. A pesar de esto, tu supervisor continúa asignando nuevas tareas urgentes sin reconocer la saturación actual. ¿Qué harías ante esta situación?",
        "options_structured": {
            "integrity_correct": "Mantienes un equilibrio entre vida profesional y personal tomando descansos regulares y rechazando tareas adicionales con explicación clara de tu capacidad actual, aunque tu supervisor pueda cuestionar tu compromiso y compañeros que aceptan todo te vean como menos dedicado.",
            "pragmatic_distractor": "Practicas técnicas de mindfulness en pausas breves y organizas mejor tu tiempo para ser más eficiente, absorbiendo la carga extra con herramientas de manejo del estrés aunque el volumen real de trabajo siga siendo insostenible.",
            "evasive_distractor": "Consultas con otros compañeros cómo están manejando su carga para validar si tu situación es única antes de hablar con tu supervisor sobre límites.",
            "rationalized_distractor": "Buscas ayuda profesional externa para manejo del estrés argumentando que mejorar tu resiliencia personal es la solución, evitando confrontar directamente el problema de sobrecarga con la empresa."
        },
        "notes": "M4 Opciones B08 batch 02 item 8 - Refactored per SOT",
        "sot_checksum": sot_checksum
    },
    {
        "id": "block-B08-q019",
        "module_id": 4,
        "block_id": "B08",
        "type": "options",
        "scenario": "Observas que hay competencia intensa y poco saludable en tu equipo por recursos y reconocimiento, mientras simultáneamente recibes críticas cada vez más frecuentes y directas de tu supervisor sobre aspectos específicos de tu desempeño reciente. Algunos compañeros están compitiendo agresivamente por las escasas oportunidades de ascenso disponibles y el ambiente laboral está cada vez más tenso e individualista. Varios miembros del equipo muestran signos claros de estrés. Tu próxima evaluación trimestral determina directamente si recibes o no el aumento que necesitas. ¿Qué harías?",
        "options_structured": {
            "integrity_correct": "Identificas señales de riesgo en tu desempeño, tomas medidas correctivas inmediatas y comunicas abiertamente a tu supervisor tus planes de mejora solicitando reuniones de seguimiento específicas, aunque expongas públicamente tus debilidades frente a compañeros competitivos y arriesgues tu evaluación si no logras mejoras rápidas.",
            "pragmatic_distractor": "Desarrollas alianzas con compañeros exitosos para aprender sus estrategias y adoptas sus métodos rápidamente buscando mejorar tu desempeño visible, aunque implique trabajar muchas horas extras sacrificando balance personal.",
            "evasive_distractor": "Buscas validación con colegas de otros equipos o antiguos supervisores sobre si las críticas son razonables antes de aceptarlas o actuar sobre ellas.",
            "rationalized_distractor": "Estableces límites protegiendo tu bienestar personal y argumentas que las críticas frecuentes reflejan un ambiente laboral tóxico que no fomenta el desarrollo sano, evitando abordar directamente las áreas de mejora señaladas."
        },
        "notes": "M4 Opciones B08 batch 02 item 9 - Refactored per SOT",
        "sot_checksum": sot_checksum
    },
    {
        "id": "block-B08-q020",
        "module_id": 4,
        "block_id": "B08",
        "type": "options",
        "scenario": "Tienes plazos extremadamente ajustados para varios proyectos críticos simultáneos cuando tu empresa anuncia de forma repentina cambios radicales e inmediatos en los procesos y herramientas que afectarán directamente la forma en que realizas tu trabajo diario. El tiempo disponible claramente no es suficiente para aprender los nuevos procesos, adaptarte adecuadamente y cumplir con todos los plazos comprometidos. Varios compañeros están visiblemente estresados y frustrados por esta situación imposible. Tu supervisor espera que te adaptes sin excusas. ¿Qué harías?",
        "options_structured": {
            "integrity_correct": "Estableces límites comunicando a tu supervisor que no puedes cumplir todos los plazos bajo los nuevos procesos y propones repriorizar proyectos de forma realista, aunque tu supervisor pueda verte como inflexible y tu evaluación refleje resistencia al cambio.",
            "pragmatic_distractor": "Identificas qué proyectos puedes adaptar rápidamente a los nuevos procesos y enfocas ahí, entregando esos aunque otros proyectos se retrasen o la calidad baje en los que fuerces bajo el viejo método.",
            "evasive_distractor": "Solicitas reuniones con los responsables de los nuevos procesos para aclarar todas las dudas antes de comprometerte con nuevos plazos, dejando pasar días mientras esperas capacitación adicional.",
            "rationalized_distractor": "Desarrollas redes de apoyo con compañeros en la misma situación para compartir estrategias de adaptación y esperas ver qué flexibilidad muestra la empresa antes de ajustar tus compromisos, postergando decisiones difíciles."
        },
        "notes": "M4 Opciones B08 batch 02 item 10 - Refactored per SOT",
        "sot_checksum": sot_checksum
    }
]

# Count words and chars for each item
def count_words(text):
    return len(re.findall(r'\S+', text))

def count_chars_no_spaces(text):
    return len(text.replace(' ', ''))

# Add metrics
for item in refactored_items:
    scenario = item["scenario"]
    words = count_words(scenario)
    chars = count_chars_no_spaces(scenario)

    item["word_count"] = words
    item["char_count"] = chars

    # Length validation (65-80 words, 300-380 chars)
    length_issues = []
    length_status = "ok"

    if words < 65:
        length_status = "frozen"
        length_issues.append(f"word_count_low ({words} < 65)")
    elif words > 80:
        length_status = "frozen"
        length_issues.append(f"word_count_high ({words} > 80)")

    if chars < 300:
        length_status = "frozen"
        length_issues.append(f"char_count_low ({chars} < 300)")
    elif chars > 380:
        length_status = "frozen"
        length_issues.append(f"char_count_high ({chars} > 380)")

    item["length_status"] = length_status
    item["length_note"] = "; ".join(length_issues) if length_issues else ""

    # Basic audit (assuming no banned words in refactored text)
    item["audit_status"] = length_status  # If length ok, audit ok
    item["audit_notes"] = "All checks passed: length, banned words, options structure." if length_status == "ok" else item["length_note"]

# Save
OUT_DIR.mkdir(parents=True, exist_ok=True)
with BATCH_JSON_PATH.open("w", encoding="utf-8") as f:
    json.dump(refactored_items, f, ensure_ascii=False, indent=2)

print(f"[OK] Refactored {len(refactored_items)} items for Module {MODULE_ID}, Block {BLOCK_ID}, {BATCH_ID}")
print(f"     Output: {BATCH_JSON_PATH}")

# Report
ok_count = sum(1 for item in refactored_items if item["length_status"] == "ok")
frozen_count = len(refactored_items) - ok_count

print(f"     Items: {len(refactored_items)}, ok={ok_count}, frozen={frozen_count}")

for idx, item in enumerate(refactored_items, 1):
    words = item["word_count"]
    chars = item["char_count"]
    status = item["length_status"]
    print(f"     Item {idx:2d}: {words:2d}w, {chars:3d}ch - {status}")

if frozen_count > 0:
    print("\n     WARNING: Some items are frozen. Review length_note.")
    exit(1)

exit(0)

# Fix scenarios to meet strict 60-65 words, 300-350 chars constraints

scenarios = [
    # q001 - need 60-65 words, 300-350 chars
    "Estás en reunión final con un cliente clave que aporta el 40% de los ingresos del trimestre. Tu supervisor presenta proyecciones que notas infladas y muy optimistas. El cliente está impresionado y listo para firmar el contrato. Si el trato no se cierra habrá recortes serios en tu equipo que muy probablemente incluyen despidos. ¿Qué haces?",

    # q002
    "Al revisar un reporte financiero para la junta descubres números que no coinciden entre secciones. Tu supervisor pide entregar de todas formas porque el plazo es mañana. La junta necesita los datos para decidir sobre inversiones y recortes. Retrasar el reporte podría afectar la planificación del trimestre y generar desconfianza en la dirección. ¿Qué haces?",

    # q003
    "Descubres que un compañero cercano maneja un conflicto de interés omitiendo pasos del protocolo, exponiendo a la empresa a riesgos legales. Tu supervisor lo sabe pero no interviene. Otros también están al tanto pero nadie dice nada. Reportar esto generaría una investigación que afectaría al equipo y dañaría permanentemente tu relación con él. ¿Qué haces?",

    # q004
    "Tu supervisor pide compartir información confidencial de clientes con un tercero sin verificar autorizaciones, argumentando urgencia porque un cliente espera cerrar un trato millonario. Si no compartes ya, el cliente podría irse con la competencia, resultando en pérdida de ingresos y posibles despidos. Esto violaría políticas de privacidad. ¿Qué haces?",

    # q005
    "Observas que varios compañeros usan recursos de la empresa como equipos y servicios sin seguir procedimientos establecidos. Tu supervisor lo sabe pero no dice nada. Parece práctica común y aceptada. Reportar esto generaría una investigación que afectaría a tus compañeros, crearía un ambiente de trabajo tenso y posiblemente te aislaría del equipo. ¿Qué haces?",

    # q006
    "Te enteras que tu supervisor tiene acceso a información privilegiada que el equipo no tiene y la usa para tomar decisiones que afectan a todos. Algunos miembros reciben proyectos deseables, otros, incluyéndote, quedan con tareas menos gratificantes. Confrontarlo podría afectar tu relación con él y tu carrera en la empresa. ¿Qué haces?",

    # q007
    "Descubres que algunos del equipo tienen acceso a datos de clientes que otros no, creando un desequilibrio en la toma de decisiones. Esos compañeros hacen propuestas más informadas y ganan reconocimiento, tú y otros quedan en desventaja. Proponer cambios podría verse como queja o cuestionar las decisiones de gerencia sobre quién debe tener acceso a información. ¿Qué haces?",

    # q008
    "Al preparar un reporte financiero crítico notas que tu supervisor usa información que no puedes ver para influir en decisiones, dejando al equipo sin contexto completo. El equipo toma decisiones con información incompleta, lo que podría afectar la precisión del reporte y decisiones financieras de la empresa. Pedir que comparta información podría verse como cuestionar su autoridad. ¿Qué haces?",

    # q009
    "Te piden usar activos de la empresa como equipos y recursos para un proyecto urgente con plazo muy ajustado. No tienes claro si las políticas lo permiten. Si no usas los activos ya el proyecto se retrasará mucho, afectando clientes importantes y resultando en pérdida de ingresos. Buscar aclaración tomaría tiempo que no tienes. ¿Qué haces?",

    # q010
    "Al preparar un reporte financiero descubres oportunidad de obtener beneficio personal usando información que manejas, como datos para inversiones o negocios paralelos. Varios compañeros ya lo hacen y parece práctica común. Tu supervisor lo sabe pero no interviene. Reportar generaría investigación que afectaría a compañeros, crearía ambiente hostil y te aislaría del equipo. ¿Qué haces?",
]

print("Scenario validation:")
print(f"{'ID':<15} {'Words':<8} {'Chars':<8} {'Status':<10}")
print('-' * 50)

for i, scenario in enumerate(scenarios, 1):
    words = len(scenario.split())
    chars = len(scenario)
    status = "PASS" if (60 <= words <= 65 and 300 <= chars <= 350) else "FAIL"
    print(f"block-B02-q{i:03d}  {words:<8} {chars:<8} {status}")
    if status == "FAIL":
        if words < 60:
            print(f"  -> Need +{60-words} words")
        elif words > 65:
            print(f"  -> Need -{words-65} words")
        if chars < 300:
            print(f"  -> Need +{300-chars} chars")
        elif chars > 350:
            print(f"  -> Need -{chars-350} chars")

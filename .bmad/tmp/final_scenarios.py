# Final scenarios adjusted to 60-65 words, 300-350 chars

scenarios = [
    # q001 - current: 56w, 340c -> need +4w (total 60w)
    "Estás en reunión final con un cliente clave que aporta 40% de los ingresos del trimestre. Tu supervisor presenta proyecciones que notas infladas y muy optimistas. El cliente está impresionado y listo para firmar el contrato ya. Si el trato no se cierra habrá recortes serios en tu equipo que muy probablemente incluyen despidos. ¿Qué haces?",

    # q002 - current: 55w, 358c -> need +5w, -8c (total 60w, 350c)
    "Al revisar un reporte financiero para la junta descubres números que no coinciden entre secciones. Tu supervisor pide entregar ya porque el plazo es mañana. La junta necesita los datos para decidir sobre inversiones y recortes. Retrasar el reporte afectaría la planificación del trimestre y generaría desconfianza en la dirección. ¿Qué haces?",

    # q003 - current: 55w, 356c -> need +5w, -6c (total 60w, 350c)
    "Descubres que un compañero cercano maneja un conflicto de interés omitiendo pasos del protocolo, exponiendo a la empresa a riesgos legales. Tu supervisor lo sabe pero no interviene. Otros también lo saben pero nadie dice nada. Reportar esto generaría una investigación que afectaría al equipo y dañaría permanentemente tu relación con él. ¿Qué haces?",

    # q004 - current: 50w, 354c -> need +10w, -4c (total 60w, 350c)
    "Tu supervisor te pide compartir información confidencial de clientes con un tercero sin verificar autorizaciones, argumentando urgencia porque un cliente importante espera cerrar un trato millonario. Si no compartes ya mismo, el cliente podría irse con la competencia, resultando en pérdida de ingresos y posibles despidos. Esto violaría políticas de privacidad. ¿Qué haces?",

    # q005 - current: 54w, 360c -> need +6w, -10c (total 60w, 350c)
    "Observas que varios compañeros usan recursos de la empresa como equipos y servicios sin seguir procedimientos establecidos. Tu supervisor lo sabe pero no dice nada. Parece una práctica común y aceptada. Reportar generaría una investigación que afectaría a tus compañeros, crearía ambiente de trabajo tenso y posiblemente te aislaría del equipo. ¿Qué haces?",

    # q006 - current: 52w, 336c -> need +8w (total 60w)
    "Te enteras que tu supervisor tiene acceso a información privilegiada que el equipo no tiene y la usa para tomar decisiones que afectan a todos en el área. Algunos miembros reciben proyectos deseables, otros, incluyéndote, quedan con tareas menos gratificantes. Confrontarlo podría afectar tu relación con él y tu carrera en la empresa. ¿Qué haces?",

    # q007 - current: 58w, 374c -> need +2w, -24c (total 60w, 350c)
    "Descubres que algunos del equipo tienen acceso a datos de clientes que otros no, creando desequilibrio en la toma de decisiones. Esos compañeros hacen propuestas más informadas y ganan reconocimiento, tú y otros quedan en desventaja. Proponer cambios podría verse como queja o cuestionar las decisiones de gerencia sobre acceso a información. ¿Qué haces?",

    # q008 - current: 59w, 395c -> need +1w, -45c (total 60w, 350c)
    "Al preparar un reporte financiero crítico notas que tu supervisor usa información que no puedes ver para influir en decisiones, dejando al equipo sin contexto completo. El equipo toma decisiones con información incompleta, afectando la precisión del reporte y decisiones financieras de la empresa. Pedir que comparta información podría verse como cuestionar su autoridad. ¿Qué haces?",

    # q009 - current: 56w, 340c -> need +4w (total 60w)
    "Te piden usar activos de la empresa como equipos y recursos para un proyecto urgente con plazo muy ajustado. No tienes claro si las políticas lo permiten. Si no usas los activos ya el proyecto se retrasará mucho, afectando a clientes importantes y resultando en pérdida de ingresos. Buscar aclaración tomaría tiempo que no tienes. ¿Qué haces?",

    # q010 - current: 55w, 387c -> need +5w, -37c (total 60w, 350c)
    "Al preparar un reporte financiero descubres oportunidad de obtener beneficio personal usando información que manejas, como datos para inversiones o negocios paralelos. Varios compañeros ya lo hacen y parece práctica común. Tu supervisor lo sabe pero no interviene. Reportar generaría investigación que afectaría a compañeros, crearía ambiente hostil y te aislaría del equipo. ¿Qué haces?",
]

print("Final scenario validation:")
print(f"{'ID':<15} {'Words':<8} {'Chars':<8} {'Status':<10}")
print('-' * 50)

all_pass = True
for i, scenario in enumerate(scenarios, 1):
    words = len(scenario.split())
    chars = len(scenario)
    status = "PASS" if (60 <= words <= 65 and 300 <= chars <= 350) else "FAIL"
    all_pass = all_pass and (status == "PASS")
    print(f"block-B02-q{i:03d}  {words:<8} {chars:<8} {status}")

print("\n" + "=" * 50)
print("ALL PASS" if all_pass else "SOME FAILED - CONTINUE ADJUSTING")

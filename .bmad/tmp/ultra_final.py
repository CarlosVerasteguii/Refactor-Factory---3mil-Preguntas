# Ultra-precise final adjustment for 60-65 words, 300-350 chars

scenarios = [
    # q001 - need exactly 60 words within 300-350 chars
    "Estás en reunión final con un cliente clave que aporta 40% de los ingresos del trimestre. Tu supervisor presenta proyecciones que notas claramente infladas y muy optimistas. El cliente está impresionado y listo para firmar el contrato ahora. Si el trato no se cierra habrá recortes serios en tu equipo que muy probablemente incluyen despidos. ¿Qué haces?",

    # q002
    "Al revisar un reporte financiero para la junta descubres números que no coinciden entre secciones. Tu supervisor pide entregar ya porque el plazo es mañana. La junta necesita estos datos para decidir sobre inversiones y recortes. Retrasar el reporte afectaría la planificación del trimestre actual y generaría desconfianza en la dirección. ¿Qué haces?",

    # q003
    "Descubres que un compañero cercano maneja un conflicto de interés omitiendo pasos del protocolo, exponiendo a la empresa a riesgos legales. Tu supervisor lo sabe pero no interviene. Otros también lo saben pero nadie dice nada. Reportar esto generaría investigación que afectaría al equipo y dañaría permanentemente tu relación con él. ¿Qué haces?",

    # q004
    "Tu supervisor te pide compartir información confidencial de clientes con un tercero sin verificar autorizaciones, argumentando urgencia porque un cliente importante espera cerrar un trato millonario. Si no compartes ahora mismo, el cliente podría irse con la competencia, resultando en pérdida de ingresos y posibles despidos. Esto violaría políticas de privacidad. ¿Qué haces?",

    # q005
    "Observas que varios compañeros usan recursos de la empresa como equipos y servicios sin seguir procedimientos establecidos. Tu supervisor lo sabe pero no dice nada. Parece una práctica común y aceptada. Reportar esto generaría una investigación que afectaría a tus compañeros, crearía ambiente de trabajo muy tenso y posiblemente te aislaría del equipo. ¿Qué haces?",

    # q006
    "Te enteras que tu supervisor tiene acceso a información privilegiada que el equipo no tiene y la usa para tomar decisiones que afectan a todos en el área. Algunos miembros reciben proyectos más deseables, otros, incluyéndote, quedan con tareas menos gratificantes. Confrontarlo podría afectar tu relación con él y tu carrera en la empresa. ¿Qué haces?",

    # q007
    "Descubres que algunos del equipo tienen acceso a datos de clientes que otros no, creando desequilibrio en toma de decisiones. Esos compañeros hacen propuestas más informadas y ganan reconocimiento, tú y otros quedan en desventaja. Proponer cambios podría verse como queja o cuestionar decisiones de gerencia sobre acceso a información. ¿Qué haces?",

    # q008
    "Al preparar un reporte financiero crítico notas que tu supervisor usa información que no puedes ver para influir decisiones, dejando al equipo sin contexto completo. El equipo toma decisiones con información incompleta, afectando precisión del reporte y decisiones financieras. Pedir que comparta información podría verse como cuestionar su autoridad. ¿Qué haces?",

    # q009
    "Te piden usar activos de la empresa como equipos y recursos para un proyecto urgente con plazo muy ajustado. No tienes claro si las políticas lo permiten. Si no usas los activos ahora el proyecto se retrasará mucho, afectando a clientes importantes y resultando en pérdida de ingresos. Buscar aclaración tomaría tiempo que no tienes. ¿Qué haces?",

    # q010
    "Al preparar reporte financiero descubres oportunidad de obtener beneficio personal usando información que manejas, como datos para inversiones o negocios paralelos. Varios compañeros ya lo hacen y parece práctica común. Tu supervisor lo sabe pero no interviene. Reportar generaría investigación que afectaría compañeros, crearía ambiente hostil y te aislaría del equipo. ¿Qué haces?",
]

print("ULTRA-PRECISE validation (target: 60-65 words, 300-350 chars):")
print(f"{'ID':<15} {'Words':<8} {'Chars':<8} {'Status':<15} {'Action'}")
print('-' * 80)

all_pass = True
for i, scenario in enumerate(scenarios, 1):
    words = len(scenario.split())
    chars = len(scenario)
    word_ok = 60 <= words <= 65
    char_ok = 300 <= chars <= 350
    status = "PASS" if (word_ok and char_ok) else "FAIL"

    action = ""
    if not word_ok:
        if words < 60:
            action += f"+{60-words}w "
        else:
            action += f"-{words-65}w "
    if not char_ok:
        if chars < 300:
            action += f"+{300-chars}c"
        else:
            action += f"-{chars-350}c"

    all_pass = all_pass and (status == "PASS")
    print(f"block-B02-q{i:03d}  {words:<8} {chars:<8} {status:<15} {action}")

print("\n" + "=" * 80)
if all_pass:
    print("✓ ALL SCENARIOS PASS - READY TO COMMIT")
else:
    print("✗ SOME FAILED - NEEDS MORE ITERATION")

# Show which are closest to passing
print("\nSummary:")
for i, scenario in enumerate(scenarios, 1):
    w, c = len(scenario.split()), len(scenario)
    if 60 <= w <= 65 and 300 <= c <= 350:
        print(f"  q{i:03d}: PASS")

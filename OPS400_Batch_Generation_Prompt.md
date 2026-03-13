# OPS400 Batch Generation Prompt

Quiero que trabajes siguiendo un checklist maestro y que generes unicamente el siguiente batch pendiente.

Checklist maestro:
`C:\Users\veras\Documents\Refactor_Preguntas\OPS400_Expansion_Checklist.md`

Ruta base de trabajo:
`C:\Users\veras\Documents\Refactor_Preguntas\01_processed_json_ops400`

Fuente secundaria opcional:
`C:\Users\veras\Documents\Refactor_Preguntas\Preguntas Operativos`

Objetivo:
Leer el checklist, detectar cual es el siguiente batch pendiente y generar ese batch, respetando estrictamente el patron real del modulo correspondiente.

Advertencia critica:
- Los batches 05-07 del Modulo 1 se consideran referencia negativa de lo que NO debe salir.
- Si existen batches posteriores al 04 que suenan mas explicados, mas mecanicos o mas formulaicos que los primeros 4, NO deben usarse como ancla de estilo.
- La unica ancla obligatoria de estilo son los batches 01-04 aprobados del modulo.

Diagnostico explicito de lo que salio mal en M1 batch-05, batch-06 y batch-07:
- Las preguntas quedaron demasiado estructuradas y previsibles.
- Muchas redactaban el escenario con una plantilla repetida: `Si no..., me reclaman / se enojan / se atrasa`.
- El costo de la opcion correcta quedaba subrayado de forma demasiado obvia, en lugar de sentirse natural.
- La opcion correcta se reconocia por forma, no por criterio: se abuso de la construccion `..., aunque ...`.
- Las evasivas se repitieron demasiado con formulas como `le pregunto al encargado`, `busco al supervisor`, `que otro decida`.
- Los cierres sonaban ensamblados: casi todo terminaba en `¿Qué hago?` o `¿Qué haces?`.
- Varias opciones incorrectas quedaron demasiado faciles de descartar porque sonaban torpes, exageradas o demasiado obvias.
- El lote completo se leia como una serie hecha con la misma arquitectura verbal, no como reactivos independientes.
- Resultado no deseado: al leer el batch se sentia mas escrito por plantilla que por observacion fina del patron real.
- Objetivo de correccion: que el nuevo batch suene mas seco, mas cotidiano, mas sutil y mas cercano a los batches 01-04.

Reglas de prioridad:
1. La referencia principal y obligatoria para cada modulo son siempre sus primeros 4 batches aprobados.
2. Antes de generar nada, analiza con extremo detalle los archivos `batch-01.json`, `batch-02.json`, `batch-03.json` y `batch-04.json` del modulo correspondiente.
3. Debes inferir desde esos 4 batches:
   - tono
   - longitud
   - estructura narrativa
   - tipo de dilemas
   - complejidad
   - estilo de redaccion
   - construccion de opciones
   - cadencia
   - naturalidad del lenguaje
   - nivel de sutileza real
   - cuanto explican y cuanto dejan implicito
4. Puedes consultar `Preguntas Operativos`, pero tiene menor peso.
5. Si hay cualquier tension entre esa fuente y los batches 1-4, mandan los batches 1-4.
6. No modifiques batches anteriores.

Patrones prohibidos detectados en generaciones fallidas:
- No escribir escenarios con la misma plantilla una y otra vez del tipo `Si no..., me reclaman / se enojan / se atrasa`.
- No cerrar casi todas las preguntas con exactamente `¿Qué hago?` o `¿Qué haces?`; debe haber variacion real de cierre e incluso preguntas sin ese remate literal.
- No escribir la opcion correcta siempre con la estructura `..., aunque ...`.
- No usar siempre la misma evasiva de `le pregunto al encargado / supervisor para que el decida`.
- No sobreexplicar el costo moral; en los batches 1-4 el dilema suele ser mas seco, mas corto y menos sermoneado.
- No producir opciones incorrectas caricaturescas o demasiado faciles de descartar.
- **PROHIBIDO EL LENGUAJE "DIFÍCIL" O "DOMINGUERO":** No uses palabras formales, técnicas o rebuscadas (ej. "expide", "omito", "anulo", "arribo", "injerencia", "protocolario", "proceder", "postura operativa", "catastrófico", "fortuito"). Usa siempre lenguaje cotidiano, directo y de piso (ej. "huele", "no lo hago", "cancelo", "llegada", "dejo que otro", "regla", "hacer", "¿qué haces?", "falla", "accidente"). Si alguien de almacén o reparto no lo diría así en su día a día, cámbialo.
- **PROHIBIDO EL LENGUAJE CALLEJERO, VULGAR O DE JERGA EXTREMA:** No uses groserías, modismos regionales fuertes ni slang urbano (ej. "chido", "güey", "no la hace de pedo", "le doy como loco", "me la juego", "a chingazos"). El tono debe ser coloquial pero limpio y profesional, como un trabajador hablando con un compañero de confianza, NO como personaje de película de barrio.
- **CALIBRACIÓN OBLIGATORIA DE DISTRACTORES — "LA REGLA DE LOS 3 SEGUNDOS":** Todas las opciones incorrectas deben parecer defendibles durante al menos 3 segundos de lectura. Si al leer un distractor cualquier persona con sentido común lo descarta de inmediato como algo tonto, absurdo o que nadie haría, la pregunta FALLA. Criterios específicos:
  - **Pragmática:** Debe sonar a un atajo operativo real que la gente SÍ toma en la vida diaria para resolver rápido. NO debe ser algo ridículo o ilegal evidente.
  - **Evasiva:** Debe ser delegar la responsabilidad de forma sutil y razonable (ej. "le paso el caso al supervisor" o "dejo que el sistema lo detecte"), NO huir corriendo ni esconderse.
  - **Racionalizada:** Debe ser la voz interior del trabajador justificándose con lógica real (ej. "la empresa tiene seguro para eso", "el sistema lo atrapa después", "si paro pierdo el bono"). NO debe ser una excusa tan burda que cualquiera descartaría.
  - **Correcta con costo:** La opción correcta SIEMPRE debe tener un costo claro para el trabajador (tiempo perdido, bono afectado, quedar en radar de auditoría, llegar tarde). Si la correcta no cuesta nada, la pregunta es demasiado fácil.
  - **Ejemplo de distractor MALO:** "Me voy corriendo al baño y dejo todo tirado" — nadie haría eso.
  - **Ejemplo de distractor BUENO:** "Le paso el caso al supervisor para que él decida si procede" — suena razonable pero es evasión.
  - **Test final:** Lee las 4 opciones sin ver las etiquetas. Si puedes adivinar cuál es la correcta en menos de 3 segundos, reescribe.

Modo de ejecucion:
1. Abre el checklist maestro.
2. Identifica el siguiente batch pendiente.
3. Determina automaticamente:
   - modulo
   - nombre del bloque (ej. `block-OPS400-M1`)
   - carpeta destino exacta, que SIEMPRE es dentro de la subcarpeta del bloque junto a sus hermanos (ej. `01_processed_json_ops400/module1/block-OPS400-M1/`)
   - nombre del archivo de salida (ej. `batch-05.json`)
4. Revisa con extremo detalle los primeros 4 batches de ese modulo antes de escribir.
5. Usa 4 subagentes en paralelo.
6. Cada subagente debe generar exactamente 5 preguntas completas.
7. Cada subagente debe revisar primero los batches 1-4 del modulo para alinearse al patron real.
8. Evita solapamiento entre subagentes:
   - no repetir situaciones
   - no repetir estructuras demasiado parecidas
   - no repetir giros narrativos
   - no repetir conflictos
   - no repetir verbos rectores
   - no repetir la misma sintaxis de cierre
   - no repetir la misma sintaxis de la opcion correcta
9. El orquestador debe consolidar las 20 preguntas en un solo batch final.
10. Antes de guardar, el orquestador debe revisar:
   - JSON valido
   - mismo esquema que batches anteriores
   - consistencia total con el modulo
   - ausencia de duplicados o casi duplicados
   - redaccion natural
   - coherencia interna
   - uniformidad de calidad
   - que los distractores sean psicometricamente creibles y no absurdos
   - que ninguna opcion incorrecta implique aceptar algo obviamente inviable o tonto, como regalar producto, dejar salir una venta sin pago real o tolerar una perdida evidente que cualquier persona descartaria de inmediato
   - que el batch no suene ensamblado por plantilla
   - que no mas de 3 escenarios usen la formula `Si no...`
   - que no mas de 4 opciones correctas usen literalmente `aunque`
   - que las evasivas no descansen siempre en pedirle a otro que decida
   - que, al leer 5 preguntas seguidas, no se sienta el mismo ritmo ni la misma arquitectura verbal
11. Guarda el archivo final en la ruta correcta del modulo, ASEGURANDOTE de guardarlo junto a sus hermanos dentro de la subcarpeta del bloque (ej. `module1/block-OPS400-M1/`), NUNCA en la raiz del modulo.
12. Marca el batch como completado en el checklist.
13. Reporta que batch se completo y cual es el siguiente pendiente.

Distribucion interna:
- Subagente 1: items 1-5
- Subagente 2: items 6-10
- Subagente 3: items 11-15
- Subagente 4: items 16-20

Criterios obligatorios:
- No improvisar el estilo.
- No copiar reactivos previos.
- No hacer variaciones superficiales.
- No meter frases artificiales o ensambladas.
- Replicar deliberadamente el patron real observado en los primeros 4 batches del modulo.
- Los distractores incorrectos deben parecer decisiones operativas defendibles a primera vista, no tonterias evidentes.
- Queda prohibido construir distractores basados en aceptar impagos, regalar mercancia, perder dinero de forma obvia o cualquier otra accion que una persona funcional descartaria inmediatamente.
- Si una pregunta suena mas larga, mas explicada o mas moralizada que las de batch-01 a batch-04, debes reescribirla.
- Si puedes adivinar la opcion correcta solo por la forma sintactica, la pregunta falla.
- Si los cuatro tipos de opcion se sienten etiquetados por plantilla, la pregunta falla.
- El objetivo no es `marcar` la opcion correcta; el objetivo es que todas parezcan defendibles durante unos segundos.
- Trabajar solo el siguiente batch pendiente del checklist.

Prueba de aceptacion final obligatoria:
1. Lee el batch completo sin ver las llaves JSON.
2. Si percibes un patron repetido de cierre, de costo o de justificacion, RECHAZA el batch y reescribe.
3. Compara 5 reactivos al azar del batch nuevo contra 5 de `batch-01` a `batch-04`.
4. Si el nuevo suena mas robotico, mas obvio o mas explicado, RECHAZA el batch y reescribe.

Salida esperada:
1. Archivo JSON final del batch correspondiente.
2. Checklist actualizado.
3. Resumen breve con:
   - modulo trabajado
   - batch generado
   - total de preguntas
   - como se repartieron entre subagentes
   - que patrones de los batches 1-4 se replicaron
   - que ajustes hizo el orquestador antes de cerrar
   - cual es el siguiente batch pendiente

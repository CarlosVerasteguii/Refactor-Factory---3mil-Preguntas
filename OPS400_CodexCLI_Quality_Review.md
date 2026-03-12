# OPS400 Codex CLI Quality Review

## Objetivo
Analizar:

- `OPS400_Expansion_Checklist.md`
- `OPS400_Batch_Generation_Prompt.md`

y contrastarlos contra:

- la estructura real de `OPS400`
- la referencia secundaria de `Preguntas Operativos`
- documentación oficial reciente sobre Codex CLI, multi-agents, handoffs, guardrails, tracing, evals y prompting

Fecha de revisión: 2026-03-12

---

## Veredicto corto

Lo que hiciste va en la dirección correcta:

- anclas la generación a batches aprobados
- fuerzas secuenciación por batch
- limitas el alcance al siguiente pendiente
- introduces paralelismo controlado

Pero todavía no está endurecido para ejecución confiable en Codex CLI.

Las brechas principales son:

1. el prompt no fija un contrato de salida suficientemente estricto
2. no define un protocolo claro de handoff entre subagentes
3. no incorpora validaciones medibles ni un loop formal de rechazo/reintento
4. no usa explícitamente la jerarquía de instrucciones que Codex CLI ya soporta con `AGENTS.md`
5. mezcla bien la idea de "golden samples" con poca formalización de fuente de verdad, trazabilidad y auditoría

---

## Lo Que Sí Está Bien

### 1. Usar los primeros 4 batches como referencia dominante
Esto es correcto para mantener continuidad estilística.

En tu checklist:

- `OPS400_Expansion_Checklist.md`: líneas 4-7

En tu prompt:

- `OPS400_Batch_Generation_Prompt.md`: líneas 17-32

Eso reduce deriva de estilo mejor que depender solo de reglas genéricas.

### 2. Forzar una unidad de trabajo pequeña
También es correcto:

- un batch a la vez
- 20 preguntas por batch
- 4 subagentes x 5 preguntas

Eso es consistente con la recomendación general de partir trabajo complejo en unidades separables.

### 3. Consolidación central
Tu prompt ya reconoce que los subagentes no deben escribir el resultado final directamente; debe existir un orquestador que consolide y revise.

Eso es una base sana.

---

## Hallazgos Críticos

### 1. El prompt deja implícito el esquema JSON real

El batch real de `OPS400` no es "cualquier JSON válido". Tiene un esquema observable muy concreto:

- `id`
- `module_id`
- `block_id`
- `type`
- `scenario`
- `options_structured`
- `notes`
- `sot_checksum`

Y `options_structured` tiene exactamente estas claves:

- `integrity_correct`
- `pragmatic_distractor`
- `evasive_distractor`
- `rationalized_distractor`

Tu prompt solo dice "mismo esquema que batches anteriores", pero no lo fija de forma operativa.

Riesgo:

- un subagente cambia nombres de campos
- altera orden o estructura
- omite `block_id` o `sot_checksum`
- produce texto válido pero no compatible con tu pipeline

### 2. Falta una jerarquía explícita de fuente de verdad

Tu prompt prioriza batches 1-4, lo cual es correcto, pero no resuelve formalmente este orden:

1. checklist operativo del batch
2. esquema y estilo observable de batches 1-4 del módulo
3. `Preguntas Operativos` como apoyo secundario
4. cualquier documentación genérica del repo solo si no contradice el patrón aprobado del módulo

Además, los datos aprobados de `OPS400` no siguen exactamente los rangos genéricos de 65-80 palabras del estándar global.

Observación local:

- M1 batches 1-4: promedio de `scenario` ~26.6 palabras
- M3 batches 1-4: promedio de `scenario` ~38.8 palabras

Conclusión:

- para `OPS400`, el verdadero estándar operativo hoy es el patrón de los batches aprobados
- `Preguntas Operativos` puede servir como referencia auxiliar
- la documentación genérica del repo no debe gobernar este flujo si pertenece a otras familias de preguntas

### 3. El prompt no define un protocolo de handoff

Actualmente dices:

- usar 4 subagentes en paralelo
- cada uno genera 5 preguntas
- cada uno revise los batches 1-4

Pero no defines qué información recibe exactamente cada subagente.

Eso es una brecha importante porque en sistemas multi-agent modernos el handoff debe controlar:

- qué contexto se pasa
- qué no se pasa
- qué salida se espera
- cómo se valida

Sin ese contrato, aparecen tres fallas típicas:

- contaminación de contexto
- duplicación temática
- drift entre trabajadores

### 4. Falta una auditoría medible, no solo cualitativa

El prompt dice:

- JSON válido
- consistencia total
- ausencia de duplicados
- redacción natural

Eso es correcto, pero insuficiente para ejecución confiable.

Faltan chequeos binarios del tipo:

- exactamente 20 items
- `type` = `options`
- `block_id` corresponde al módulo
- IDs consecutivos y únicos
- ninguna palabra o giro que rompa el patrón lingüístico observado del módulo
- ninguna opción vacía
- `integrity_correct` con costo personal explícito
- distractores plausibles y no caricaturescos
- similitud léxica y semántica bajo umbral contra batches 1-4 y contra el batch nuevo
- longitud dentro de rango observado del módulo

### 5. No hay loop formal de rechazo y reintento

Tu prompt no fija un comportamiento fail-closed.

Debería decir algo como:

- si un subagente entrega un item rechazado, ese item no pasa
- si el orquestador detecta incumplimiento, regenera solo los items fallidos
- máximo N reintentos
- si persiste la falla, abortar sin guardar ni marcar checklist

Sin eso, el sistema tiende a "pasar con warnings".

### 6. Hay riesgo de ruta incorrecta en entorno Codex CLI/WSL

Tu prompt reutilizable usa rutas Windows:

- `C:\Users\veras\Documents\Refactor_Preguntas\...`

Pero en este entorno la ruta activa es:

- `/mnt/c/Users/veras/Documents/Refactor_Preguntas`

Si corres Codex CLI desde WSL o bash, esas rutas de Windows pueden ser una fuente de fricción.

Para Codex CLI conviene:

- usar rutas relativas al repo, o
- usar rutas POSIX si el agente corre en WSL

### 7. Estás usando un prompt reutilizable para algo que Codex ya sabe cargar con `AGENTS.md`

Esto es importante.

Codex CLI ya soporta instrucciones por proyecto y por subdirectorio usando `AGENTS.md` y `AGENTS.override.md`.

Eso significa que muchas reglas estables no deberían vivir dentro del prompt operativo.

Deberían moverse a:

- `AGENTS.md` del repo
- o un `AGENTS.override.md` cerca del directorio OPS400 si quieres reglas más específicas

Y dejar el prompt reutilizable solo para:

- seleccionar el siguiente batch
- disparar la ejecución
- resumir resultados

Nota importante:

- esto no implica heredar a OPS400 reglas genéricas de `doc_standards`, `banned_words` o SOT si pertenecen a otros flujos
- implica mover solo reglas estables que sí apliquen a OPS400

---

## Qué Dice La Documentación Actual

### 1. Codex CLI ya tiene soporte nativo para multi-agent

La documentación oficial de Codex indica que el modo multi-agent es experimental y puede habilitarse en la configuración. También explica que Codex puede lanzar agentes especializados en paralelo y consolidar resultados.

Implicación práctica para ti:

- tu diseño de 4 subagentes sí encaja con la plataforma
- pero debes endurecer roles, contexto, salida y consolidación

Fuente:

- https://developers.openai.com/codex/multi-agent

### 2. Codex CLI ya tiene una jerarquía de instrucciones con `AGENTS.md`

Codex lee `AGENTS.md` antes de trabajar y combina guía global con guía del proyecto y overrides por carpeta.

Implicación práctica:

- no metas toda la política estable dentro del prompt reutilizable
- deja en `AGENTS.md` lo permanente
- deja en el prompt solo lo dinámico del batch actual

Fuente:

- https://developers.openai.com/codex/guides/agents-md

### 3. OpenAI Agents SDK recomienda handoffs con descripción, input controlado y filtros

La documentación de handoffs muestra que:

- los handoffs son parte explícita del diseño
- cada handoff puede tener descripción
- puedes definir `input_type`
- puedes filtrar el historial con `input_filter`

Implicación:

- no basta con "usa 4 subagentes"
- necesitas definir el payload de entrada para cada uno

Fuente:

- https://openai.github.io/openai-agents-python/handoffs/

### 4. Guardrails no cubren automáticamente toda cadena multi-agent

La documentación de guardrails es clara:

- input guardrails aplican al primer agente
- output guardrails al agente final
- para validar cada llamada o etapa necesitas checks más explícitos

Implicación:

- si quieres calidad por subagente, no basta una sola revisión final general
- necesitas validación por worker y validación final

Fuente:

- https://openai.github.io/openai-agents-python/guardrails/

### 5. Tracing es clave para workflows de varios agentes

La documentación de tracing recomienda usar trazas y spans para agrupar ejecuciones relacionadas.

Implicación:

- si luego automatizas esto vía SDK, registra por batch:
  - módulo
  - batch
  - subagente
  - ítems asignados
  - validaciones pasadas/fallidas

Fuente:

- https://openai.github.io/openai-agents-python/tracing/

### 6. Structured Outputs es la recomendación fuerte para salidas robustas

OpenAI documenta que `strict: true` con schema reduce radicalmente la deriva de formato.

Implicación:

- cada subagente no debería devolver prosa libre
- debería devolver un arreglo tipado de exactamente 5 items con el esquema exacto
- el orquestador debería consolidar sobre estructuras, no sobre texto libre

Fuentes:

- https://openai.com/index/introducing-structured-outputs-in-the-api/
- https://developers.openai.com/api/docs/guides/structured-outputs

### 7. Evals y criterios de prueba deben correr cada vez que cambias el prompt

OpenAI recomienda versionar prompts, compararlos y rerunear evals al publicar nuevas versiones.

Implicación:

- tu prompt reutilizable debe tratarse como artefacto versionado
- cada ajuste al prompt debería compararse contra un pequeño set de batches de prueba

Fuente:

- https://developers.openai.com/api/docs/guides/evals
- https://developers.openai.com/api/docs/guides/prompting

### 8. El prompting moderno para agentes exige instrucciones claras, tool semantics y ejemplos

La guía de Codex y la de prompting de Anthropic coinciden en lo importante:

- instrucciones claras y directas
- herramientas con nombres semánticos
- ejemplos buenos
- prompts enfocados por tarea

Implicación:

- tu prompt debe incluir ejemplos concretos de "salida válida" y "salida inválida"
- también debe fijar cuándo el worker debe rechazar una idea antes de convertirla en item final

Fuentes:

- https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

### 9. La documentación de subagents de Claude coincide en el patrón correcto

Aunque no es Codex, es útil como confirmación cruzada:

- subagentes enfocados en una sola tarea
- descripciones detalladas
- acceso limitado a herramientas

Implicación:

- evita subagentes genéricos y ambiguos
- define trabajadores muy concretos

Fuente:

- https://code.claude.com/docs/en/sub-agents

---

## Recomendación Operativa Para Tu Caso

### Arquitectura mínima recomendada

#### Capa 1: Instrucciones estables en `AGENTS.md`
Mover aquí:

- prioridad de golden samples
- regla de no modificar batches previos
- reglas de esquema JSON
- reglas lingüísticas válidas para OPS400
- reglas psicométricas
- política de auditoría

#### Capa 2: Checklist como estado
Dejar en `OPS400_Expansion_Checklist.md` solo:

- batches pendientes/completos
- reglas operativas del orden de ejecución

#### Capa 3: Prompt reutilizable como launcher
Dejar en `OPS400_Batch_Generation_Prompt.md` solo:

- abre checklist
- toma siguiente pendiente
- carga módulo correcto
- lanza subagentes
- consolida
- audita
- guarda
- actualiza checklist

---

## Contrato Recomendado Para Subagentes

Cada subagente debería recibir:

- módulo
- batch destino
- rango exacto de 5 items
- resumen sintético del patrón observado en batches 1-4
- lista de temas o giros ya ocupados por otros workers
- esquema JSON exacto esperado
- criterios de rechazo obligatorios

Cada subagente debería devolver:

- `items`: arreglo de exactamente 5 objetos válidos
- `self_check`: lista corta de validaciones binarias
- `risk_flags`: vacía o con incidencias

El orquestador debería:

1. unir los 20 items
2. correr validación de esquema
3. correr validación léxica
4. correr validación psicométrica
5. regenerar solo items rechazados
6. guardar únicamente si todo pasa

---

## Reglas Que Te Faltan Escribir En El Prompt

Estas son las más importantes:

1. Si no puedes producir exactamente 20 items válidos, no guardes nada.
2. Si cualquier item falla el esquema, regenera solo ese item.
3. Si cualquier item mete vocabulario ajeno al patrón operativo real del módulo, regenera.
4. Si `integrity_correct` no implica costo personal explícito, rechazar.
5. Si dos escenarios son casi duplicados, rechazar ambos y regenerar.
6. Si el estilo de longitud sale del rango observado del módulo, revisar antes de aceptar.
7. No marcar checklist hasta que el batch esté validado y persistido.
8. El resumen final debe distinguir:
   - items aceptados sin cambios
   - items corregidos por el orquestador
   - items regenerados

---

## Riesgos Específicos De Tu Diseño Actual

### Riesgo 1: clones estilísticos
Como los 4 workers reciben la misma instrucción general, tenderán a converger en aperturas, verbos y estructura.

Mitigación:

- asignar a cada worker un "espacio negativo" distinto
- pasar lista de temas ya reservados

### Riesgo 2: cumplimiento aparente pero no psicométrico
Un item puede verse limpio y aun así ser fácil de responder.

Mitigación:

- agregar un chequeo explícito de "dolor real" en la opción correcta
- agregar un crítico final o grader

### Riesgo 3: drift de esquema

Mitigación:

- structured output estricto
- validación automática antes de guardar

### Riesgo 4: rutas frágiles

Mitigación:

- usar rutas relativas o POSIX si operas desde WSL/Codex CLI

### Riesgo 5: checklist marcado antes de estar realmente aprobado

Mitigación:

- el update del checklist debe ser el último paso, nunca antes

---

## Prioridad De Cambios

### Prioridad alta

1. fijar esquema JSON exacto en el prompt
2. definir precedencia formal de fuentes
3. agregar auditoría binaria y fail-closed
4. cambiar rutas a relativas o POSIX
5. mover reglas permanentes a `AGENTS.md`

### Prioridad media

1. definir payload de handoff por subagente
2. registrar trazabilidad por batch
3. versionar el prompt y comparar variantes

### Prioridad opcional pero valiosa

1. agregar grader/critic separado
2. automatizar deduplicación semántica
3. convertir el flujo a `spawn_agents_on_csv` o pipeline programático si escalas volumen

---

## Conclusión

Tu diseño ya tiene el instinto correcto:

- usar golden samples reales
- limitar alcance
- paralelizar
- consolidar

Lo que le falta no es "más creatividad", sino endurecimiento de sistema:

- contrato exacto
- handoff explícito
- validación medible
- rechazo/reintento
- mejor uso de `AGENTS.md`

Si conviertes esos puntos en `v2`, la calidad de ejecución en Codex CLI debería subir mucho más que con simples retoques de redacción al prompt.

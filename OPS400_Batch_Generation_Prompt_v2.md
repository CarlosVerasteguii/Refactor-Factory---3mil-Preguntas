# OPS400 Batch Generation Prompt v2

Trabaja solo sobre el siguiente batch pendiente de OPS400 y no hagas cambios fuera de ese alcance.

## Rutas de trabajo

- Checklist maestro: `./OPS400_Expansion_Checklist.md`
- Base OPS400: `./01_processed_json_ops400`
- Fuente secundaria opcional: `./Preguntas Operativos`
- Documentación genérica del repo: usar solo si no contradice el patrón aprobado de OPS400

## Objetivo

1. Abrir el checklist maestro.
2. Detectar el siguiente batch pendiente.
3. Generar únicamente ese batch.
4. Guardarlo en la carpeta correcta.
5. Actualizar el checklist solo si el batch quedó validado.
6. Reportar qué batch se completó y cuál sigue.

## Precedencia de fuentes

Usa este orden de prioridad exacto:

1. Esquema y patrón observable de `batch-01.json` a `batch-04.json` del módulo correspondiente.
2. `Preguntas Operativos` solo como apoyo secundario.
3. Reglas estables específicas de OPS400 definidas en `AGENTS.md` o `AGENTS.override.md`.
4. Cualquier documentación genérica del repo solo si no contradice el patrón aprobado del módulo.

Si hay conflicto entre fuentes, mandan los batches aprobados del módulo.

## Alcance y restricciones

- Trabaja un solo batch por ejecución.
- No modifiques batches previos.
- Cada batch nuevo debe contener exactamente 20 preguntas.
- La distribución fija es 4 subagentes x 5 preguntas.
- Este flujo debe respetar el patrón real de OPS400, no imponer a la fuerza el estándar genérico si contradice a los batches aprobados.
- Si no puedes producir un batch completamente válido, no guardes nada y no actualices el checklist.

## Confirmación del esquema real antes de generar

Antes de lanzar subagentes, inspecciona los primeros 4 batches del módulo y fija el esquema exacto del módulo.

Para OPS400, el esquema esperado debe conservar estas claves por item:

```json
{
  "id": "block-OPS400-M1-q001",
  "module_id": 1,
  "block_id": "OPS400-M1",
  "type": "options",
  "scenario": "...",
  "options_structured": {
    "integrity_correct": "...",
    "pragmatic_distractor": "...",
    "evasive_distractor": "...",
    "rationalized_distractor": "..."
  },
  "notes": "...",
  "sot_checksum": "..."
}
```

No alteres nombres de campos, estructura ni tipo.

## Fase 1: análisis del módulo

Antes de escribir, analiza `batch-01.json` a `batch-04.json` del módulo correspondiente y sintetiza:

- tono real
- longitud real observada
- estructura de `scenario`
- densidad y complejidad del lenguaje
- tipo de presión o conflicto
- forma en que aparece el costo personal
- patrón de distractores
- aperturas frecuentes e infrecuentes
- cierres y cadencia
- verbos rectores ya demasiado usados
- temas ya muy repetidos

Produce un resumen operativo breve para los workers. Ese resumen debe servir para alinear, no para reemplazar los archivos de referencia.

## Fase 2: asignación de subagentes

Usa exactamente 4 subagentes en paralelo.

Asignación:

- Subagente 1: items 1-5
- Subagente 2: items 6-10
- Subagente 3: items 11-15
- Subagente 4: items 16-20

Cada subagente debe recibir:

- módulo
- batch destino
- rango de IDs asignado
- resumen operativo del patrón del módulo
- lista de temas, verbos y giros ya reservados para evitar solapamiento
- esquema JSON exacto esperado
- criterios obligatorios de rechazo

No pases contexto irrelevante.

## Contrato obligatorio para cada subagente

Cada subagente debe:

1. Revisar primero los 4 batches aprobados del módulo.
2. Generar exactamente 5 items.
3. Devolver solo salida estructurada compatible con el esquema acordado.
4. Evitar:
   - situaciones repetidas
   - aperturas clónicas
   - verbos rectores repetidos
   - mismo tipo de conflicto más de una vez
   - distractores caricaturescos
5. Hacer autocheck antes de devolver.

Cada item debe:

- sonar natural
- parecer del mismo módulo
- mantener consistencia con OPS400
- evitar vocabulario ajeno al patrón operativo real del módulo
- tener distractores plausibles
- hacer que la opción correcta implique costo personal explícito

## Regla psicométrica crítica

Rechaza cualquier item si:

- `integrity_correct` no duele de verdad
- el costo personal no es claro
- algún distractor es demasiado obvio
- la respuesta correcta es demasiado fácil de detectar
- el escenario parece artificial o ensamblado

## Fase 3: consolidación del orquestador

El orquestador debe unir los 20 items y luego validar, en este orden:

1. hay exactamente 20 items
2. IDs únicos y consistentes con el módulo y batch
3. `block_id` correcto
4. `type` correcto
5. estructura JSON válida
6. claves completas en cada `options_structured`
7. sin vocabulario claramente ajeno al patrón operativo del módulo
8. sin duplicados ni casi duplicados
9. consistencia estilística con los 4 batches aprobados
10. costo personal explícito en `integrity_correct`
11. distractores plausibles y no triviales
12. redacción natural y uniforme

## Fail-Closed

Aplica estas reglas sin excepción:

- Si falla un item, no lo aceptes.
- Si falla un item, regenera solo ese item.
- Si falla la estructura, corrige antes de continuar.
- Si el lote completo no pasa la auditoría, no lo guardes.
- No actualices el checklist hasta que el archivo final exista y esté validado.

## Criterios de no regresión

El batch nuevo debe parecer una continuación real del módulo. No debe:

- sentirse más genérico que los batches 1-4
- copiar reactivos previos
- usar variaciones superficiales
- introducir vocabulario ajeno al patrón del módulo
- sobrecargar de palabras el escenario si el módulo usa escenarios más cortos

## Formato de salida interna recomendado para workers

Cada worker debe devolver un arreglo JSON de 5 objetos, sin texto adicional.

## Pasos finales

1. Guardar el batch final en la ruta correcta del módulo.
2. Verificar que el archivo se escribió correctamente.
3. Marcar ese batch como completado en el checklist.
4. Reportar:
   - módulo trabajado
   - batch generado
   - total de preguntas
   - distribución por subagente
   - patrones replicados desde batches 1-4
   - items regenerados o corregidos
   - validaciones ejecutadas
   - siguiente batch pendiente

## Condición de seguridad

Si hay duda entre "terminar rápido" y "mantener fidelidad al patrón aprobado", prioriza fidelidad al patrón aprobado.

# OPS400 - Handoff para mañana

Fecha: 2026-03-29

## Estado actual

- Se revisaron y corrigieron los hallazgos bloqueantes de `batch-28`, `batch-29` y `batch-30`.
- Hay dos commits locales nuevos:
  - `bf12186` `r`
  - `415499b` `s`
- El repo local esta divergido respecto a `origin/main`:
  - `ahead 2`
  - `behind 2`
- La divergencia viene de que el remoto trae un archivo invalido para Windows llamado `nul`, asi que no conviene empujar a `main` desde esta copia.

## Objetivo de mañana

No generar mas batches por ahora.

La tarea siguiente es hacer una auditoria **read-only** sobre los `batch-20` a `batch-27` para los 5 modulos, y sacar un reporte de:

- `HIGH`
- `MEDIUM`
- `LOW`

La idea es detectar si de `20+` para arriba sigue habiendo:

- palabras vetadas
- anglicismos
- tono corporativo
- distractores que suenan correctos
- duplicados entre batches
- plantillas verbales repetidas

## Que hacer mañana en la PC de la oficina

1. Abrir este repo.
2. Revisar este archivo primero.
3. Abrir Copilot CLI o la herramienta que vayas a usar con `fleet`.
4. Pegar el prompt completo de abajo.
5. Esperar el reporte consolidado.
6. Verificar que el agente **no** repita la auditoria vieja de 2 items (`q574` y `q549`).
7. Verificar que el alcance sea **solo** `batch-20` a `batch-27`.
8. No corregir nada todavia. Primero obtener el reporte.

## Prompt listo para pegar

```text
/fleet Haz una auditoría read-only de OPS400 sobre batch-20 a batch-27 en los 5 módulos.

Objetivo:
- auditar M1 batch-20, 21, 22, 24, 25, 26 y 27
- auditar M2 batch-20, 21, 22, 24, 25, 26 y 27
- auditar M3 batch-20, 21, 22, 24, 25, 26 y 27
- auditar M4 batch-20, 21, 22, 24, 25, 26 y 27
- auditar M5 batch-20, 21, 22, 24, 25, 26 y 27

Instrucciones:
- no edites archivos
- no corrijas JSON
- no toques OPS400_Expansion_Checklist.md
- no toques ningún checklist
- usa como ancla batch-01 a batch-04 del mismo módulo dentro de 01_processed_json_ops400
- divide la revisión por módulo y por bloques de 5 items
- prioriza:
  - palabras vetadas
  - anglicismos
  - tono corporativo o poco natural
  - integrity_correct sin costo personal claro
  - pragmatic_distractor poco plausible
  - evasive_distractor duplicada
  - rationalized_distractor demasiado obvia o que suena correcta
  - duplicados o casi duplicados entre batches 20-27
  - plantillas verbales repetidas

Formato de salida:
- resumen global
- hallazgos HIGH / MEDIUM / LOW
- módulo, batch, item, campo afectado
- razón concreta
- indicar si conviene corregir antes de commit o si puede pasar

Importante:
- no me repitas la verificación de q574 y q549
- no audites batch-28, 29 ni 30
- enfócate solo en batch-20 a batch-27
- si falta algún batch en local o remoto, dilo explícitamente
```

## Criterio de aceptacion de la corrida

La corrida de mañana sirve solo si cumple esto:

- audita `20-27`, no `28-30`
- no reescribe archivos
- no toca checklists
- entrega resumen por severidad
- identifica items concretos y el campo afectado

Si no cumple eso, hay que volver a lanzar el prompt con el alcance corregido.

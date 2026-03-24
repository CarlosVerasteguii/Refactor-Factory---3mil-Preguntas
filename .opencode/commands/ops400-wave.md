---
description: Genera una ola multi-modulo OPS400 para un batch fijo, la audita, corrige REWRITE y reaudita antes de cerrar.
agent: ops400-wave-orchestrator
---

Usa `BATCH_OBJETIVO = $ARGUMENTS`.

Corre una ola multi-modulo de OPS400 con estas reglas:

- lanza 5 workers en paralelo, uno por modulo
- genera solo:
  - M1 batch-BATCH_OBJETIVO
  - M2 batch-BATCH_OBJETIVO
  - M3 batch-BATCH_OBJETIVO
  - M4 batch-BATCH_OBJETIVO
  - M5 batch-BATCH_OBJETIVO
- cada worker usa `@ops400-batch-orchestrator`
- cada worker se calibra solo contra `batch-01.json` a `batch-04.json` de su propio modulo
- no uses batches posteriores como ancla de estilo
- no toques `OPS400_Expansion_Checklist.md` durante la generacion
- cuando termine la generacion, audita esos mismos 5 batches con `@ops400-rationalized-audit-orchestrator`
- enfocate en `rationalized_distractor` demasiado obvia, autopermiso explicito, fraude o falsificacion demasiado frontal, baja plausibilidad, plantilla verbal y tono fuera de modulo
- si hay `REWRITE`, corrige solo esos items
- reaudita solo los items corregidos
- actualiza `OPS400_Expansion_Checklist.md` solo al final y solo para modulos que ya no queden en `REWRITE`
- devuelve resumen por modulo con archivo escrito, auditoria inicial, correcciones, reauditoria y estado final

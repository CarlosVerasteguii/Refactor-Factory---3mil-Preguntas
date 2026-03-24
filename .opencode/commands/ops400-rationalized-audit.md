---
description: Audita batches OPS400 existentes en modo read-only, enfocandose en distractores rationalized.
agent: ops400-rationalized-audit-orchestrator
---

Audita de forma read-only los distractores `rationalized` para: $ARGUMENTS

Reglas:

- no edites archivos
- no corrijas JSON
- no toques `OPS400_Expansion_Checklist.md`
- usa como ancla `batch-01.json` a `batch-04.json` del mismo modulo
- divide cada batch en subagentes por bloques de 5 items
- usa `@ops400-option-auditor` en modo auditoria read-only
- enfocate en `rationalized_distractor` demasiado obvia, autopermiso explicito, baja plausibilidad y plantilla verbal
- entrega un reporte final con `KEEP`, `BORDERLINE` y `REWRITE` por item

# OPS400 Batch Generation Prompt

Usa este prompt en Codex CLI para trabajar con el contrato más nuevo de OPS400, sin reinventar el flujo.

## Lectura obligatoria antes de actuar

1. `AGENTS.md`
2. `01_processed_json_ops400/AGENTS.md`
3. `.opencode/agents/ops400-batch-orchestrator.md`
4. `.opencode/agents/ops400-five-pack-generator.md`
5. `.opencode/agents/ops400-option-auditor.md`

Las copias de `.github/agents/` se pueden usar como espejo, pero si hay diferencia manda `.opencode/agents/`.

## Prompt base para un batch

```text
Lee AGENTS.md y 01_processed_json_ops400/AGENTS.md.
Trabaja como el agente definido en .opencode/agents/ops400-batch-orchestrator.md.
Usa .opencode/agents/ops400-five-pack-generator.md y .opencode/agents/ops400-option-auditor.md como contratos de worker.

Genera exactamente un batch de OPS400.
Si no te especifico batch, toma el primer [ ] de OPS400_Expansion_Checklist.md.
Si te especifico modulo y batch, trabaja solo ese objetivo.

Reglas:
- trabaja solo dentro de 01_processed_json_ops400
- usa como ancla batch-01.json a batch-04.json del modulo correspondiente
- no uses batches posteriores como ancla salvo instruccion explicita
- no modifiques batches previos
- no guardes nada si el batch no pasa validacion
- actualiza OPS400_Expansion_Checklist.md solo si el archivo final queda escrito y releido
```

## Prompt base para una ola multi-modulo

```text
Lee AGENTS.md y 01_processed_json_ops400/AGENTS.md.
Trabaja como el agente definido en .opencode/agents/ops400-wave-orchestrator.md.
Usa .opencode/agents/ops400-batch-orchestrator.md como worker por modulo.
Usa .opencode/agents/ops400-rationalized-audit-orchestrator.md para la auditoria posterior.

Corre una sola ola multi-modulo de OPS400 para batch-N.
Lanza un worker por modulo.
Ningun worker debe editar OPS400_Expansion_Checklist.md.
Actualiza OPS400_Expansion_Checklist.md solo despues de auditoria, correccion y reauditoria.
```

## Nota operativa

La inteligencia para elegir el siguiente pendiente y revisar el checklist debe venir del modelo leyendo `OPS400_Expansion_Checklist.md` directamente. No dependas de scripts auxiliares para ese paso salvo que el usuario los pida.

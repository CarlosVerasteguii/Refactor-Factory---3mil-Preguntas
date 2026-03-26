# OPS400 en Codex CLI

Este repo ya tenía contratos de agentes para Copilot y OpenCode. Para Codex CLI, la referencia canónica ahora es la familia de agentes de `.opencode/agents/`, con `.github/agents/` como espejo.

## Qué agente usar

- Un solo batch: `.opencode/agents/ops400-batch-orchestrator.md`
- Una ola multi-módulo: `.opencode/agents/ops400-wave-orchestrator.md`
- Auditoría read-only de `rationalized_distractor`: `.opencode/agents/ops400-rationalized-audit-orchestrator.md`
- Workers de apoyo:
  - `.opencode/agents/ops400-five-pack-generator.md`
  - `.opencode/agents/ops400-option-auditor.md`

## Cómo correr un batch en Codex

Abre `codex` en la raíz del repo y usa un prompt como este:

```text
Lee AGENTS.md y 01_processed_json_ops400/AGENTS.md.
Trabaja como el agente definido en .opencode/agents/ops400-batch-orchestrator.md.
Usa .opencode/agents/ops400-five-pack-generator.md y .opencode/agents/ops400-option-auditor.md como contratos de worker.

Genera exactamente un batch de OPS400.
Si no te especifico batch, toma el primer [ ] de OPS400_Expansion_Checklist.md.
Trabaja solo dentro de 01_processed_json_ops400.
Usa como ancla batch-01.json a batch-04.json del modulo correspondiente.
No modifiques batches previos.
Actualiza OPS400_Expansion_Checklist.md solo si el batch final queda valido y releido.
```

## Cómo correr un batch específico

```text
Lee AGENTS.md y 01_processed_json_ops400/AGENTS.md.
Trabaja como el agente definido en .opencode/agents/ops400-batch-orchestrator.md.

Genera OPS400 M3 batch-19.
Trabaja solo ese batch.
Usa como ancla batch-01.json a batch-04.json del modulo 3.
Trabaja solo dentro de 01_processed_json_ops400.
No modifiques batches previos.
Actualiza OPS400_Expansion_Checklist.md solo si el batch final queda valido y releido.
```

## Cómo correr una ola completa

Usa la versión más nueva del orquestador de ola, que ya incluye auditoría y reauditoría antes del checklist:

```text
Lee AGENTS.md y 01_processed_json_ops400/AGENTS.md.
Trabaja como el agente definido en .opencode/agents/ops400-wave-orchestrator.md.
Usa .opencode/agents/ops400-batch-orchestrator.md como worker por modulo.
Usa .opencode/agents/ops400-rationalized-audit-orchestrator.md para la auditoria posterior.

Corre una sola ola multi-modulo de OPS400 para batch-19.
Lanza un worker por modulo.
Ningun worker debe tocar OPS400_Expansion_Checklist.md.
Actualiza OPS400_Expansion_Checklist.md solo despues de auditoria, correccion y reauditoria.
```

## Criterio operativo

- Codex no necesita scripts auxiliares para decidir el siguiente batch. Debe leer el checklist directamente.
- La lógica estable vive en `AGENTS.md`, `01_processed_json_ops400/AGENTS.md` y en los contratos de `.opencode/agents/`.
- Si alguna copia de `.github/agents/` y `.opencode/agents/` diverge, prioriza `.opencode/agents/`.

# OPS400 en OpenCode

Esta configuracion deja listo el repo para correr el flujo OPS400 dentro de OpenCode con subagentes.

## Archivos agregados

- `opencode.json`
- `.opencode/agents/ops400-wave-orchestrator.md`
- `.opencode/agents/ops400-batch-orchestrator.md`
- `.opencode/agents/ops400-five-pack-generator.md`
- `.opencode/agents/ops400-option-auditor.md`
- `.opencode/agents/ops400-rationalized-audit-orchestrator.md`
- `.opencode/commands/ops400-wave.md`
- `.opencode/commands/ops400-rationalized-audit.md`

## Que hace cada agente

- `ops400-wave-orchestrator`
  - coordina la ola multi-modulo
  - lanza un worker por modulo
  - dispara auditoria y reauditoria
  - actualiza checklist solo al final

- `ops400-batch-orchestrator`
  - genera un batch de un modulo
  - divide internamente en 4 bloques de 5
  - usa generador y auditor

- `ops400-five-pack-generator`
  - genera 5 reactivos

- `ops400-option-auditor`
  - audita items o bloques
  - soporta modo correccion y modo read-only

- `ops400-rationalized-audit-orchestrator`
  - audita batches existentes
  - se enfoca en `rationalized_distractor`

## Como correr batch-19

En OpenCode, abre el repo y usa este comando:

```text
/ops400-wave 19
```

Eso le indica al orquestador:

- generar `batch-19` para M1 a M5
- auditar esos mismos batches
- corregir solo los `REWRITE`
- reauditar lo corregido
- actualizar checklist solo al final

## Como correr una auditoria read-only

Ejemplo:

```text
/ops400-rationalized-audit "M1 batch-19, M2 batch-19, M3 batch-19, M4 batch-19, M5 batch-19"
```

## Como usarlo sin comandos

Si prefieres invocar al agente directamente, puedes mencionar:

```text
@ops400-wave-orchestrator Corre una ola multi-modulo de OPS400 con BATCH_OBJETIVO=19.
```

## Notas operativas

- La ancla de estilo sigue siendo `batch-01.json` a `batch-04.json` del modulo.
- No se deben usar batches posteriores como ancla salvo instruccion explicita.
- El checklist no debe tocarse durante la generacion paralela.
- Si un modulo queda con `REWRITE`, no debe cerrarse automaticamente.

## Fuentes

- Agents: https://opencode.ai/docs/agents/
- Config: https://opencode.ai/docs/config/
- Commands: https://opencode.ai/docs/commands/
- Permissions: https://opencode.ai/docs/permissions/

# OPS400 Codex CLI Override

This file defines the Codex-native contract for OPS400 batch work.

It applies whenever the task touches:

- `01_processed_json_ops400/`
- `OPS400_Expansion_Checklist.md`
- `OPS400_Batch_Generation_Prompt.md`
- existing OPS400 batches or audits

## Canonical Agent Contracts

Use these files as the source of truth for agent behavior:

1. `.opencode/agents/ops400-batch-orchestrator.md`
2. `.opencode/agents/ops400-wave-orchestrator.md`
3. `.opencode/agents/ops400-five-pack-generator.md`
4. `.opencode/agents/ops400-option-auditor.md`
5. `.opencode/agents/ops400-rationalized-audit-orchestrator.md`

Mirror copies also exist in `.github/agents/`. If there is any discrepancy, prefer `.opencode/agents/` because it is the newer set.

## How Codex Must Behave

- For one batch, operate as `ops400-batch-orchestrator`.
- For one multi-module round, operate as `ops400-wave-orchestrator`.
- For read-only review of existing batches, operate as `ops400-rationalized-audit-orchestrator`.
- Use model reasoning to inspect `OPS400_Expansion_Checklist.md` directly. Do not introduce helper scripts for checklist selection unless the user explicitly asks for automation.

## Non-Negotiable Rules

- Work only one batch or one wave per run.
- Never modify previous batches.
- The style anchor is always `batch-01.json` to `batch-04.json` of the same module.
- Do not use later batches as the style anchor unless the user explicitly asks.
- Work only inside `01_processed_json_ops400` for batch generation.
- Update `OPS400_Expansion_Checklist.md` only after the final file was written and reread successfully.
- Fail closed. If the batch does not pass, do not save it and do not mark the checklist.

## Precedence

Use this order of priority:

1. The relevant canonical OPS400 agent contract in `.opencode/agents/`
2. `batch-01.json` to `batch-04.json` of the same module
3. `OPS400_Expansion_Checklist.md`
4. `Preguntas Operativos` only as secondary support
5. Generic repo docs only if they do not contradict OPS400

## Notes For Codex

- The OpenCode and Copilot agent files are not dead artifacts here. They are the design reference for Codex behavior.
- The newest meaningful delta is in `.opencode/agents/ops400-wave-orchestrator.md`, which adds audit, correction, and re-audit before touching the checklist.
- When in doubt, mirror the agent contract instead of inventing a new workflow.

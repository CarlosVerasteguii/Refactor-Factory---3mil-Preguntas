# Claude Code OPS400 Option Audit

Este paquete deja listo un flujo de auditoría batch por batch para Claude Code, sin scripts externos.

## Archivos

- Comando slash: `.claude/commands/ops400-option-audit.md`
- Subagente: `.claude/agents/ops400-option-auditor.md`
- Checklist: `OPS400_Option_Audit_Checklist.md`

## Cómo funciona

1. El comando slash selecciona un batch objetivo.
2. Lee el checklist de auditoría o usa un batch explícito si se lo pasas como argumento.
3. Carga los batches 01-04 del mismo módulo como ancla.
4. Lanza 4 subagentes en paralelo.
5. Cada subagente revisa 5 reactivos completos.
6. El orquestador consolida, corrige solo lo necesario, guarda y actualiza el checklist.

## Cómo invocarlo en Claude Code

Sin argumentos, toma el siguiente batch pendiente del checklist:

```text
/ops400-option-audit
```

Con batch explícito:

```text
/ops400-option-audit M1 batch-05
```

## Qué se investigó

La estructura está alineada con la documentación oficial de Claude Code:

- Los comandos slash personalizados viven en `.claude/commands/*.md`
- Los subagentes personalizados viven en `.claude/agents/*.md`
- `CLAUDE.md` sirve para memoria persistente, pero aquí no fue necesario tocarlo para el flujo inicial
- Anthropic ya fusionó conceptualmente custom commands dentro de skills, pero los archivos en `.claude/commands/*.md` siguen funcionando y siguen creando comandos invocables con `/...`

## Fuentes oficiales

- Slash commands:
  - https://docs.anthropic.com/en/docs/claude-code/slash-commands
- Subagents:
  - https://docs.anthropic.com/en/docs/claude-code/subagents
- Memory / CLAUDE.md:
  - https://docs.anthropic.com/en/docs/claude-code/memory
- Skills overview:
  - https://code.claude.com/docs/en/skills

## Nota de diseño

Se dejó el flujo como comando slash + subagente porque:

- es invocable directamente
- es fácil de versionar en el repo
- permite paralelismo con subagentes
- evita depender de scripts o parsing externo

# OPS400 en Copilot CLI

Este flujo deja listo el esquema de agentes para correr generacion de batches OPS400 en GitHub Copilot CLI.

## Agentes disponibles

- `.github/agents/ops400-batch-orchestrator.agent.md`
- `.github/agents/ops400-five-pack-generator.agent.md`
- `.github/agents/ops400-option-auditor.agent.md`
- `.github/agents/ops400-wave-orchestrator.agent.md`

## Uso recomendado

### 1. Seleccionar el agente principal

En Copilot CLI puedes usar cualquiera de estas dos formas:

```text
/agent
```

Y luego seleccionar `ops400-batch-orchestrator`.

O iniciar la sesion directamente:

```bash
copilot --agent=ops400-batch-orchestrator
```

### 2. Generar el siguiente batch pendiente

Prompt recomendado:

```text
Genera el siguiente batch pendiente de OPS400. Trabaja solo un batch. Usa como ancla batch-01 a batch-04 del modulo correspondiente dentro de 01_processed_json_ops400. Divide el trabajo en 4 bloques de 5 reactivos, audita cada bloque antes de consolidar, guarda el JSON final y actualiza OPS400_Expansion_Checklist.md solo si el batch final queda valido.
```

### 3. Generar un batch especifico

Prompt recomendado:

```text
Genera OPS400 M3 batch-16. Trabaja solo ese batch. Usa como ancla batch-01 a batch-04 del modulo 3. Divide el trabajo en 4 bloques de 5 reactivos, audita cada bloque antes de consolidar, guarda el JSON final y actualiza OPS400_Expansion_Checklist.md solo si el batch final queda valido.
```

## Uso con `/fleet`

Usa `/fleet` cuando tu instalacion de Copilot CLI lo tenga habilitado y quieras forzar modo de paralelismo para el trabajo divisible.

### Cuándo sí usar `/fleet`

- Cuando el trabajo es naturalmente separable en bloques disjuntos
- Cuando quieres que Copilot intente usar varios subagentes en paralelo
- Cuando el batch ya esta bien definido y solo quieres acelerar ejecucion

### Cuándo no usar `/fleet`

- Cuando aun estas explorando el modulo
- Cuando el prompt es ambiguo
- Cuando hay cambios locales confusos o batches sin consolidar

### Prompt recomendado con `/fleet`

```text
/fleet Usa @ops400-batch-orchestrator para generar OPS400 M3 batch-16.

Instrucciones:
- trabaja solo ese batch
- usa como referencia obligatoria batch-01 a batch-04 del modulo 3
- divide el batch en 4 bloques disjuntos: items 1-5, 6-10, 11-15 y 16-20
- para cada bloque usa @ops400-five-pack-generator y luego @ops400-option-auditor
- consolida un solo archivo final
- guarda solo si el batch completo pasa validacion
- actualiza OPS400_Expansion_Checklist.md solo si el archivo final ya fue escrito y releido
- no modifiques batches previos
```

## Uso para una ola completa por modulos

Si quieres correr el mismo batch en los 5 modulos a la vez, usa `@ops400-wave-orchestrator`.

La idea es:

- un subagente para M1 batch-N
- un subagente para M2 batch-N
- un subagente para M3 batch-N
- un subagente para M4 batch-N
- un subagente para M5 batch-N

Cada uno usa `@ops400-batch-orchestrator` como worker aislado.

### Prompt recomendado para batch-17 en los 5 modulos

```text
/fleet Usa @ops400-wave-orchestrator para correr la ola OPS400 batch-17.

Instrucciones:
- lanza 5 workers en paralelo, uno por modulo
- usa @ops400-batch-orchestrator como worker en cada modulo
- cada worker debe correr solo su modulo:
  - M1 batch-17
  - M2 batch-17
  - M3 batch-17
  - M4 batch-17
  - M5 batch-17
- cada worker debe calibrarse solo contra batch-01 a batch-04 de su propio modulo
- los workers no deben editar OPS400_Expansion_Checklist.md
- cada worker debe guardar su batch final solo si pasa validacion
- al final, consolida resultados y actualiza OPS400_Expansion_Checklist.md de forma centralizada
- no modifiques batches previos
```

### Por qué este patron es mejor

- evita contaminacion de contexto entre modulos
- evita que varios workers compitan por el checklist al mismo tiempo
- deja una sola escritura central del checklist
- fuerza que cada modulo se ancle solo a su propio patron

## Nota operativa importante

Si ya tienes `batch-15.json` locales sin commit y el checklist tambien esta modificado, primero conviene consolidar ese estado antes de lanzar mas batches.

Si no lo haces, varios agentes pueden partir de un estado ambiguo y tratar de pisarse entre `batch-15` y `batch-16`.

## Auditoria read-only de rationalized

Si quieres revisar batches ya existentes sin modificar archivos, usa `@ops400-rationalized-audit-orchestrator`.

### Prompt recomendado para batch-15 y batch-16

```text
/fleet Usa @ops400-rationalized-audit-orchestrator para auditar de forma read-only los distractores rationalized de OPS400.

Objetivo:
- auditar M1 batch-15
- auditar M1 batch-16
- auditar M2 batch-15
- auditar M2 batch-16
- auditar M3 batch-15
- auditar M3 batch-16
- auditar M4 batch-15
- auditar M4 batch-16
- auditar M5 batch-15
- auditar M5 batch-16

Instrucciones:
- no edites archivos
- no corrijas JSON
- no toques OPS400_Expansion_Checklist.md
- usa como ancla batch-01 a batch-04 del mismo modulo
- divide cada batch en subagentes por bloques de 5 items
- usa @ops400-option-auditor en modo auditoria read-only
- enfocate en rationalized_distractor demasiado obvias, autopermiso explicito, baja plausibilidad y plantilla verbal
- entrega un reporte final con KEEP, BORDERLINE y REWRITE por item y prioriza que lotes requieren correccion primero
```

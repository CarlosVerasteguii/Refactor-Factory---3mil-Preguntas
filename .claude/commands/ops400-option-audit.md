---
description: Audita un batch OPS400 ya generado, detecta opciones inválidas y corrige solo las necesarias usando 4 subagentes en paralelo
argument-hint: [opcional: M1 batch-05]
---

Quiero que ejecutes una auditoría estricta de opciones sobre un solo batch de OPS400 ya existente.

## Referencias

- Checklist de auditoría: @OPS400_Option_Audit_Checklist.md
- Base de batches: @01_processed_json_ops400
- Referencia secundaria: @Preguntas Operativos

## Selección del batch

1. Si el usuario pasó argumentos en `$ARGUMENTS`, usa ese batch exacto como objetivo.
2. Si `$ARGUMENTS` está vacío, abre el checklist de auditoría y toma el siguiente batch pendiente.
3. Trabaja solo un batch por ejecución.
4. No toques otros batches.

## Regla maestra

- La única ancla obligatoria de estilo y criterio son los `batch-01.json` a `batch-04.json` del mismo módulo.
- `Preguntas Operativos` puede consultarse como apoyo secundario.
- Si hay conflicto, mandan los batches 01-04 del módulo.

## Lo que debes revisar

Debes leer y entender cada reactivo como una unidad completa:

- `scenario`
- `integrity_correct`
- `pragmatic_distractor`
- `evasive_distractor`
- `rationalized_distractor`

No revises por palabra aislada ni por patrón superficial. Primero entiende qué está pasando en la situación y qué está defendiendo cada opción.

## Prohibición explícita

- No uses Python.
- No uses scripts externos.
- No hagas clasificación automática ciega.
- No decidas por regex sin leer el contenido.

Usa las herramientas de Claude Code para abrir, leer, comparar y editar archivos. La revisión debe ser semántica y psicométrica, no mecánica.

## Foco principal de la auditoría

Busca y corrige especialmente casos donde una opción, sobre todo `rationalized_distractor`, cruza de "error defendible" a algo demasiado obvio, absurdo o directamente improcedente.

Casos típicos que deben disparar revisión:

- tolerar que alguien se lleve mercancía sin pagar
- dejar ir a un cliente sin cobro real con la idea de que "mañana paga"
- inventar, reciclar o falsificar tickets, folios o comprobantes
- quedarse con dinero, sobrantes o diferencias
- usar dinero ajeno para completar compras o "hacer un favor"
- justificar pérdidas porque "la empresa tiene seguro"
- saltarse controles que cualquier trabajador funcional descartaría de inmediato
- aceptar regalos o favores cuando la regla lo prohíbe de forma expresa

## Criterio psicométrico obligatorio

Las 4 opciones deben parecer defendibles durante unos segundos.

Pero la `rationalized_distractor` NO puede convertirse en:

- robo abierto
- fraude abierto
- falsificación abierta
- apropiación evidente de dinero o mercancía
- una decisión tan torpe que el lector la descarte al instante

Debe sonar a autojustificación laboral creíble, no a delito descarado ni a tontería.

## Distribución por subagentes

Usa exactamente 4 subagentes en paralelo, todos del tipo `ops400-option-auditor`.

- Subagente 1: items 1-5
- Subagente 2: items 6-10
- Subagente 3: items 11-15
- Subagente 4: items 16-20

## Instrucción obligatoria para cada subagente

Cada subagente debe:

1. Leer sus 5 reactivos completos.
2. Leer también `batch-01.json` a `batch-04.json` del mismo módulo antes de juzgar.
3. Entender el `scenario` y el rol funcional de las 4 opciones.
4. Detectar si alguna opción falla por:
   - delito demasiado explícito
   - distractor demasiado fácil o absurdo
   - justificación demasiado obvia
   - sintaxis plantillada que revela el rol de la opción
   - lenguaje poco natural para operativos
5. Reescribir solo lo mínimo necesario.
6. Mantener intacto el esquema JSON.
7. Preservar `id`, `module_id`, `block_id`, `type`, `notes` y `sot_checksum`, salvo que exista un error claro.

Cada subagente debe devolver:

- `KEEP` para items que pasan
- `REWRITE` para items que requieren cambio
- el objeto JSON completo corregido para cada item reescrito
- una razón breve y concreta del cambio

Los subagentes no deben escribir el archivo final directamente.

## Reglas de reescritura

- Cambia primero opciones, no escenarios.
- Solo cambia un `scenario` si el escenario obliga a que los distractores queden mal calibrados.
- No moralices.
- No sobreexplique el costo.
- No conviertas la opción correcta en sermón.
- Mantén lenguaje cotidiano, seco y operativo.

## Consolidación del orquestador

Cuando regresen los 4 subagentes:

1. Consolida sus hallazgos.
2. Aplica solo las reescrituras necesarias al batch objetivo.
3. Relee el batch completo ya corregido.
4. Verifica que siga teniendo exactamente 20 preguntas.
5. Verifica que el JSON siga válido.
6. Verifica que ninguna `rationalized_distractor` siga tolerando robo, fraude, falsificación, impago evidente o apropiación de dinero/mercancía.
7. Verifica que las opciones no suenen etiquetadas por plantilla.
8. Verifica que el batch siga sonando como continuación real del módulo.

## Aceptación final

Antes de guardar, lee el batch completo de corrido y recházalo si todavía notas cualquiera de estos problemas:

- una `rationalized_distractor` que normaliza delito o pérdida absurda
- una opción incorrecta tan tonta que se descarta en menos de 3 segundos
- un batch que suena armado por la misma plantilla verbal
- un cambio que ya no respeta el tono real de los batches 01-04

## Checklist

Marca el batch como completado en `@OPS400_Option_Audit_Checklist.md` solo si:

- el archivo quedó guardado
- el batch fue releído completo
- la auditoría final pasó

## Respuesta final

Reporta:

- batch auditado
- módulo
- cuántos items quedaron `KEEP`
- cuántos items se reescribieron
- qué tipo de fallas fueron corregidas
- siguiente batch pendiente del checklist

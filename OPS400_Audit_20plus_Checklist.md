# OPS400 Audit 20+ Checklist

Objetivo:
- auditar y estabilizar los batches `20` a `30` de OPS400
- separar hallazgos `HIGH`, `MEDIUM` y `LOW`
- corregir primero lo critico y despues cerrar por tandas

Reglas:
- usar como ancla `batch-01.json` a `batch-04.json` de cada modulo
- no corregir todo de golpe
- primero auditar en modo read-only
- corregir solo lo marcado como `HIGH`
- reauditar antes de comitear

## Fase 1 - Auditoria Prioritaria
- [ ] Auditar `M1-M5` batch-28
- [ ] Auditar `M1-M5` batch-29
- [ ] Auditar `M1-M5` batch-30
- [ ] Consolidar hallazgos `HIGH / MEDIUM / LOW`
- [ ] Corregir solo `HIGH`
- [ ] Reauditar items corregidos
- [ ] Marcar `28-30` como listos para commit

## Fase 2 - Auditoria de Ola Anterior
- [ ] Auditar `M1-M5` batch-20
- [ ] Auditar `M1-M5` batch-21
- [ ] Auditar `M1-M5` batch-22
- [ ] Auditar `M1-M5` batch-24
- [ ] Auditar `M1-M5` batch-25
- [ ] Auditar `M1-M5` batch-26
- [ ] Auditar `M1-M5` batch-27
- [ ] Consolidar hallazgos `HIGH / MEDIUM / LOW`
- [ ] Corregir solo `HIGH`
- [ ] Reauditar items corregidos

## Fase 3 - Pendientes de Expansion
- [ ] Revisar si `batch-17` falta de verdad o solo en checklist local
- [ ] Revisar si `batch-18` falta de verdad o solo en checklist local
- [ ] Revisar si `batch-19` falta de verdad o solo en checklist local
- [ ] Revisar si `batch-23` falta de verdad o solo en checklist local

## Fase 4 - Pendientes de Auditoria Vieja
- [ ] Auditar `M1 batch-13`
- [ ] Auditar `M1 batch-14`
- [ ] Auditar `M2 batch-13`
- [ ] Auditar `M2 batch-14`
- [ ] Auditar `M3 batch-13`
- [ ] Auditar `M3 batch-14`
- [ ] Auditar `M4 batch-13`
- [ ] Auditar `M4 batch-14`
- [ ] Auditar `M5 batch-13`
- [ ] Auditar `M5 batch-14`

## Criterios de Revision
- [ ] Sin palabras vetadas
- [ ] Sin anglicismos o tono corporativo innecesario
- [ ] `integrity_correct` con costo personal claro
- [ ] `pragmatic_distractor` plausible
- [ ] `evasive_distractor` no duplica otra opcion
- [ ] `rationalized_distractor` no suena correcta ni demasiado obvia
- [ ] Sin duplicados o casi duplicados
- [ ] Sin plantillas verbales demasiado repetidas

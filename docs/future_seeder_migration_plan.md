# Plan futuro: seeders y migraciones para MiraPreguntas

Contexto
- Objetivo final: después de refactorizar los ~3000 reactivos (10 bloques, pares 200, impares 400) consolidar cada módulo/bloque y generar seeders/migraciones para la tabla MiraPreguntas (ver SourceofTruth/MiraPreguntasTable.php).
- Estado actual: refactor en curso con agentes SOT nuevos (`.bmad/custom/agents/*sot*`). Salidas por batch en `01_processed_json/moduleX/block-BYY/batch-zz.json` + logs.

Pendiente al final del refactor
1) Agregar agentes/flujo final:
   - Transformador a seeder: toma los `all.json` consolidados por módulo/bloque, mapea campos a la estructura de `MiraPreguntasTable.php` y produce seeders listos para insertar.
   - Generador de migración: crea la migración (o script equivalente) con los campos exactos requeridos por la tabla.
2) Requisitos de entrada:
   - JSON consolidado limpio por módulo/bloque (sin items frozen).
   - Checksum del SOT usado para cada batch (ya en las salidas).
3) Requisitos de salida:
   - Seeder en formato PHP/JSON/SQL según stack elegido.
   - Migración compatible con la definición en `SourceofTruth/MiraPreguntasTable.php`.
4) Integridad:
   - Validar conteo total por módulo (400/200) y global (~3000).
   - Incluir hash por archivo y resumen de logs de QA.

Nota: este paso se ejecutará al finalizar todos los bloques; no afecta el refactor actual.***

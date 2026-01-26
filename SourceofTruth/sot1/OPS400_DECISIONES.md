# OPS400 — Decisiones y Alcance

## 1) Objetivo
Crear **400** preguntas nuevas para MIRA, diseñadas para población **operativa** (no “oficina/administrativo”), sin modificar las **3000** preguntas ya existentes.

## 2) Tipo de pregunta
- **Solo**: `options` (opción múltiple).
- **No** se generan nuevas preguntas `video` para este set.

## 3) Distribución por módulo
Distribución **equilibrada**:
- Módulo 1: **80** (options)
- Módulo 2: **80** (options)
- Módulo 3: **80** (options)
- Módulo 4: **80** (options)
- Módulo 5: **80** (options)

Total: 5 × 80 = **400**.

## 4) Reglas de contenido (operativo/no administrativo)
- Ambientación típica: ruta/reparto, conducción, caja/ventas, almacén/inventario, atención al cliente, turnos/coberturas, seguridad y cuidado del equipo.
- Evitar marcos “corporativos” repetidos: auditorías, juntas directivas, compras/presupuestos, “áreas” administrativas, proyectos de oficina.
- Español neutro, claro, profesional accesible.
- Cumplir `config/banned_words.txt` (sin términos prohibidos/anglicismos).
- Psicometía: la opción `integrity_correct` **debe** implicar costo personal **explícito** (tiempo, conflicto, dinero, incomodidad, esfuerzo, quedar mal).

## 5) Estructura MCQ (options)
Cada reactivo incluye:
- `scenario`: 2–3 frases y **cierra con pregunta**.
- `options_structured` con las 4 claves exactas:
  - `integrity_correct`
  - `pragmatic_distractor`
  - `evasive_distractor`
  - `rationalized_distractor`

## 6) Seeder (Laravel) — comportamiento
Se crea un **seeder nuevo** específico para estas 400 preguntas (separado del seeder existente de 3000).

Reglas acordadas:
- **No** se ejecuta `truncate`.
- Inserta **solo** 400 filas nuevas en `mira_preguntas`.
- Se asume ejecución **una sola vez** en producción (no se garantiza idempotencia).

Convención propuesta (se puede renombrar libremente):
- Archivo: `MiraPreguntasOps400Seeder.php`
- Clase: `MiraPreguntasOps400Seeder`

Campos a insertar (tabla `mira_preguntas`):
- `modulo` (1–5)
- `tipo` = `'options'`
- `texto` = `scenario`
- `opciones` = JSON string con `{"opciones":[...4 textos...]}` (orden fijo interno)
- `idioma` = `'es'`
- `created_at`, `updated_at` = `now()`

## 7) Output esperado (pipeline)
Este repo genera:
1) JSONs procesados (entrada del pipeline)
2) Consolidados por módulo (02_final_artifacts)
3) Seeder PHP Laravel listo para correr

Nota: el set OPS400 debe mantenerse aislado del dataset original (3000) para no sobreescribir artefactos previos.

Rutas propuestas (aisladas):
- Entrada (procesados): `01_processed_json_ops400/`
- Salida (artefactos): `02_final_artifacts_ops400/`

Bloques (opción B: nuevos block_id por módulo):
- Módulo 1: `OPS400-M1`
- Módulo 2: `OPS400-M2`
- Módulo 3: `OPS400-M3`
- Módulo 4: `OPS400-M4`
- Módulo 5: `OPS400-M5`

## 8) Convenciones de batches e IDs (procesados)
Estructura de carpetas (por módulo):
- `01_processed_json_ops400/module{N}/block-OPS400-M{N}/batch-0X.json`

Cantidad de batches por módulo:
- 4 batches × 20 ítems = 80 ítems por módulo

Rangos por batch (por módulo):
- `batch-01.json`: q001–q020
- `batch-02.json`: q021–q040
- `batch-03.json`: q041–q060
- `batch-04.json`: q061–q080

Formato de `id`:
- `block-OPS400-M{N}-qNNN` (NNN con 3 dígitos; ej. `q001`)

Formato mínimo por ítem (options):
```json
{
  "id": "block-OPS400-M1-q001",
  "module_id": 1,
  "block_id": "OPS400-M1",
  "type": "options",
  "scenario": "...¿...?",
  "options_structured": {
    "integrity_correct": "...",
    "pragmatic_distractor": "...",
    "evasive_distractor": "...",
    "rationalized_distractor": "..."
  },
  "notes": "OPS400 Modulo 1 Options OPS400-M1 batch 01 item 1",
  "sot_checksum": "ops400_m1_options_v1"
}
```

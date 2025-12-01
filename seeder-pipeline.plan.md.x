# Seeder Pipeline Scripts

## Contexto

- 400 preguntas actuales en 10 bloques (5 modulos x 2 bloques)
- Batches dispersos en `01_processed_json/moduleX/block-BYY/batch-zz.json`
- Destino: Seeder PHP Laravel para tabla `mira_preguntas`
- Items con status "frozen" se USAN (ya revisados manualmente)

## Mapeo de campos

| JSON actual | Tabla destino | Transformacion |

|-------------|---------------|----------------|

| `module_id` | `modulo` | Directo (1-5) |

| `type` | `tipo` | "video" u "options" |

| `refactored_text` (video) | `texto` | Directo + escape PHP |

| `scenario` (options) | `texto` | Directo + escape PHP |

| `options_structured` | `opciones` | JSON encode; `"{}"` para video |

| - | `idioma` | "es" fijo |

## Entregables

### 1. Script consolidador: `scripts/consolidate_batches.py`

- Glob robusto: `batch-*.json` (no asumir cantidad fija)
- Ignorar status frozen (usar todos los items)
- **VALIDACIONES PRE-SEEDER:**
  - Max length texto: 60,000 chars (STOP si excede)
  - Module in [1, 2, 3, 4, 5] (STOP si fuera de rango)
  - Type in ['video', 'options'] (STOP si invalido)
  - JSON valido en options_structured (STOP si malformado)
  - Encoding UTF-8 verificado
- **WARNING de batches**: Log si bloque tiene <2 o >4 batches (anomalia)
- Debug verboso: cada archivo, cada item, cada ID
- Fail-fast: STOP inmediato + mensaje detallado si hay error
- Log trazabilidad: `consolidation_trace.jsonl`

### 2. Script transformador: `scripts/generate_seeder.py`

- Campo `opciones`: `"{}"` para video, `json.dumps()` para options
- **ESCAPE PHP**: Comillas simples/dobles y backslashes en texto
- Seeder Laravel con:
  - `DB::transaction()` para atomicidad (rollback si falla)
  - Chunks de 50 inserts
  - Conteo final con echo
- Debug verboso: transformaciones, conteos, warnings
- Fail-fast: STOP + detalle si hay anomalia
- Log trazabilidad: `seeder_trace.jsonl`
- **Chunk size configurable**: `--chunk-size=50` por defecto

### 3. Estructura de salida

```
02_final_artifacts/
  seeders/
    MiraPreguntasSeeder.php    <- Con DB::transaction()
  consolidated/
    module1_all.json ... module5_all.json
  logs/
    consolidation_trace.jsonl  <- {id, source_batch, module, type, checksum, ts}
    seeder_trace.jsonl         <- {id, modulo, tipo, texto_chars, row_num}
    execution_summary.json     <- {totals, by_module, by_type, hashes, duration}
```

## Validaciones criticas (Pre-mortem)

| Validacion | Donde | Accion si falla |

|------------|-------|-----------------|

| texto.length < 60000 | consolidate | STOP + mostrar item |

| module_id in 1-5 | consolidate | STOP + mostrar item |

| type in video/options | consolidate | STOP + mostrar item |

| options_structured parseable | consolidate | STOP + mostrar JSON |

| UTF-8 encoding | consolidate | STOP + mostrar bytes |

| Batch count anomaly | consolidate | WARNING (no stop) |

## Decisiones tecnicas

- Python 3.x stdlib only (json, pathlib, hashlib, datetime, argparse)
- UTF-8 explicito en todos los archivos
- Logs abundantes para revision por IA
- Preservar sot_checksum y notes en logs (trazabilidad)
- Validar conteo final por modulo antes de generar seeder
- Seeder atomico con DB::transaction()
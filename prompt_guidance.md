# Guía de prompts para el pipeline SOT (evitar errores comunes de la IA)

## Errores frecuentes que observamos
- Crear/ejecutar scripts `.py` o escribir en carpetas `temp/` en lugar de procesar inline con los agentes SOT.
- Ignorar los agentes correctos (usar prompts viejos) o no cargar `config .bmad/bmb/config.yaml`.
- No respetar el bloque/lote: usar batch num o start_index equivocados; sobreescribir batches previos.
- No validar longitudes (palabras/caracteres) ni banned words; dejar items congelados por simulación en lugar de refactor real.
- Opciones múltiples desequilibradas (distractores obvios o caricaturescos).

## Formato de prompt recomendado (funciona bien)
Usa este esquema y ajusta los valores según el bloque:
```
No crees ni ejecutes scripts (.py), ni uses carpeta temp, ni toques archivos existentes. Procesa inline con los agentes SOT (.bmad/custom/agents: <video|options>-refactor-sot, length-guard-sot, audit-sot). No simules ni generes “frozen” salvo que falle la validación.

1) Revisa 01_processed_json/moduleX/block-BYY/ y detecta el último batch-XX.json.
2) Si existe, usa batch_num = último+1 y batch_start_index = (último_lote_fin + 1). Si no hay batches, usa batch_num=01 y start_index=1.
3) Ejecuta pipeline-orchestrator con:
   module_id=X
   block_id=BYY
   target_type=<video|options>
   batch_size=<N>
   pilot_mode=false
   input_path=00_raw_data/<n>Bloque.md
4) Criterios:
   - Aplica SOT ModuloX <Video|Opciones>
   - Escenario/refactored_text 65–80 palabras y 300–380 chars; fail-fast si fuera de rango
   - Dos caminos con costo (video) o 4 opciones balanceadas (options); sin banned words
5) Guarda en 01_processed_json/moduleX/block-BYY/batch-<batch_num>.json y .log.jsonl.
Si no puedes hacerlo inline, dilo y no generes ni modifiques archivos.
```

## Notas clave
- Siempre cargar `.bmad/bmb/config.yaml` y usar solo agentes SOT en `.bmad/custom/agents/*sot*`.
- Validar longitudes: palabras 65–80, caracteres 300–380; rechazar fuera de rango.
- Opciones múltiples: 4 alternativas plausibles y similares en longitud/tono.
- No crear scripts auxiliares ni archivos de prueba; solo los JSON/LOG de salida del batch.

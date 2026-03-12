# OPS400 Batch Generation Prompt

Quiero que trabajes siguiendo un checklist maestro y que generes unicamente el siguiente batch pendiente.

Checklist maestro:
`C:\Users\veras\Documents\Refactor_Preguntas\OPS400_Expansion_Checklist.md`

Ruta base de trabajo:
`C:\Users\veras\Documents\Refactor_Preguntas\01_processed_json_ops400`

Fuente secundaria opcional:
`C:\Users\veras\Documents\Refactor_Preguntas\Preguntas Operativos`

Objetivo:
Leer el checklist, detectar cual es el siguiente batch pendiente y generar ese batch, respetando estrictamente el patron real del modulo correspondiente.

Reglas de prioridad:
1. La referencia principal y obligatoria para cada modulo son siempre sus primeros 4 batches aprobados.
2. Antes de generar nada, analiza con extremo detalle los archivos `batch-01.json`, `batch-02.json`, `batch-03.json` y `batch-04.json` del modulo correspondiente.
3. Debes inferir desde esos 4 batches:
   - tono
   - longitud
   - estructura narrativa
   - tipo de dilemas
   - complejidad
   - estilo de redaccion
   - construccion de opciones
   - cadencia
   - naturalidad del lenguaje
4. Puedes consultar `Preguntas Operativos`, pero tiene menor peso.
5. Si hay cualquier tension entre esa fuente y los batches 1-4, mandan los batches 1-4.
6. No modifiques batches anteriores.

Modo de ejecucion:
1. Abre el checklist maestro.
2. Identifica el siguiente batch pendiente.
3. Determina automaticamente:
   - modulo
   - carpeta destino
   - nombre del bloque
   - nombre del archivo de salida
4. Revisa con extremo detalle los primeros 4 batches de ese modulo antes de escribir.
5. Usa 4 subagentes en paralelo.
6. Cada subagente debe generar exactamente 5 preguntas completas.
7. Cada subagente debe revisar primero los batches 1-4 del modulo para alinearse al patron real.
8. Evita solapamiento entre subagentes:
   - no repetir situaciones
   - no repetir estructuras demasiado parecidas
   - no repetir giros narrativos
   - no repetir conflictos
   - no repetir verbos rectores
9. El orquestador debe consolidar las 20 preguntas en un solo batch final.
10. Antes de guardar, el orquestador debe revisar:
   - JSON valido
   - mismo esquema que batches anteriores
   - consistencia total con el modulo
   - ausencia de duplicados o casi duplicados
   - redaccion natural
   - coherencia interna
   - uniformidad de calidad
11. Guarda el archivo final en la ruta correcta del modulo.
12. Marca el batch como completado en el checklist.
13. Reporta que batch se completo y cual es el siguiente pendiente.

Distribucion interna:
- Subagente 1: items 1-5
- Subagente 2: items 6-10
- Subagente 3: items 11-15
- Subagente 4: items 16-20

Criterios obligatorios:
- No improvisar el estilo.
- No copiar reactivos previos.
- No hacer variaciones superficiales.
- No meter frases artificiales o ensambladas.
- Replicar deliberadamente el patron real observado en los primeros 4 batches del modulo.
- Trabajar solo el siguiente batch pendiente del checklist.

Salida esperada:
1. Archivo JSON final del batch correspondiente.
2. Checklist actualizado.
3. Resumen breve con:
   - modulo trabajado
   - batch generado
   - total de preguntas
   - como se repartieron entre subagentes
   - que patrones de los batches 1-4 se replicaron
   - que ajustes hizo el orquestador antes de cerrar
   - cual es el siguiente batch pendiente

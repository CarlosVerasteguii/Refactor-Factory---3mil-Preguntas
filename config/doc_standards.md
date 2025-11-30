
# ESTANDARES DE REFACTORIZACION MIRA (SOT-ALIGNED v4)

Este documento reemplaza versiones previas. Usa SOT módulo-específicos:
- Video: `SourceofTruth/SOT_Modulo{1-5}_Video.md` (por módulo)
- Options: `SourceofTruth/SOT_Modulo{1-5}_Opciones.md` (por módulo)
- Referencia general (fallback): `SourceofTruth/OPEN_GoldenSample_v2.md`

## Lenguaje y tono
- Tono: profesional accesible, frases concisas.
- Longitud meta: 65-80 palabras por reactivo (no superar 80).
- Longitud meta en caracteres: objetivo 320-350; rango aceptable 300-380 (rechazar fuera de rango).
- Banned words: ver `config/banned_words.txt`. Reemplazar según mapa.
- Evita tecnicismos y anglicismos innecesarios.
- PROHIBIDO vocabulario técnico específico: Scrum, Kanban, CEO, CTO, Sprint, Backlog, Software, App, Startup. Usar términos genéricos (ver banned_words.txt).

## Estructura obligatoria (Video / Open)
1) Contexto + presion en 1-2 frases.
2) Dos caminos claros:
   - Integridad con COSTO PERSONAL ALTO Y EXPLÍCITO (frustración de otros, afecta evaluación, daña reputación, jornada pesada, conflicto directo).
   - Atajo/beneficio inmediato (evitar conflicto, ganar tiempo/dinero, quedar bien).
3) Cierre en pregunta (varia el cierre: "Que haces y por que?", "Como justificas tu decision?", "Que priorizas y por que?").
4) REGLA CRITICA: La opción correcta debe ser DIFICIL de elegir. Si es muy fácil, el reactivo falla psicométricamente.

## Estructura obligatoria (MCQ / Options)
1) Escenario (1-2 frases): Contexto + presión, dos caminos implícitos. Meta 65-80 palabras, 300-380 chars.
2) 4 opciones sin etiquetas A-D, siguiendo REGLAS PSICOMETRICAS:
   - **integrity_correct**: Costo personal ALTO y EXPLICITO (frustración de otros, afecta evaluación, daña reputación). DEBE SER DIFICIL DE ELEGIR.
   - **pragmatic_distractor**: Parece razonable y proactiva (propone solución, busca cumplir) pero tiene costo oculto (calidad sacrificada, riesgo asumido). VIABLE a primera vista.
   - **evasive_distractor**: Parece proactiva (consulta, busca validación) pero EVITA DECIDIR mientras el tiempo pasa o traslada responsabilidad a otros.
   - **rationalized_distractor**: Justificación aparentemente razonable (calidad, beneficio colectivo, eficiencia) pero EVITA COMPROMISO o esfuerzo real.
3) VALIDACION PSICOMETRICA CRITICA:
   - RECHAZAR si la opción de integridad es muy fácil de elegir (sin costo real).
   - RECHAZAR si cualquier distractor es OBVIAMENTE malo (fácil de descartar).
   - Las trampas deben ser SUTILES, no obvias.
   - Todas las opciones deben parecer viables a primera vista.

## Formato de salida sugerido (JSON)
Video:
```json
{
  "id": "block-01-q001",
  "module_id": 1,
  "type": "video",
  "refactored_text": "...",
  "notes": "opcional breve",
  "sot_checksum": "..."
}
```

Options:
```json
{
  "id": "block-02-q001",
  "module_id": 1,
  "type": "options",
  "scenario": "...",
  "options_structured": {
    "integrity_correct": "...",
    "pragmatic_distractor": "...",
    "evasive_distractor": "...",
    "rationalized_distractor": "..."
  },
  "notes": "opcional breve",
  "sot_checksum": "..."
}
```

## Reglas de variacion
- Aperturas variadas (no siempre "Tu supervisor...").
- Cierre de pregunta variado.
- Distribuir el "costo" (social, tiempo, economico, reputacional) sin repetir el mismo patrón en todo el batch.

## Modulos (referencia rapida)
- Modulo 1: Integridad Laboral (score I). Temas: presupuesto, viáticos, uso de recursos, info confidencial, conflicto de interés.
- Modulo 2: Permanencia (score M). Temas: adaptación a cambios, nuevas políticas, gestión de estrés, cambios jerárquicos.
- Modulo 3: Ética (score I). Temas: dilemas morales, transparencia, impacto social, decisiones con información incompleta.
- Modulo 4: Riesgo/Control Emocional (score L). Temas: gestión de estrés, deadlines imposibles, control emocional, sobrecarga.
- Modulo 5: Apego Laboral (score C/L). Temas: cultura organizacional, sentido de pertenencia, confianza en la organización.
- Para detalles completos, ver `config/matrix_map.json`.
- IMPORTANTE: En runtime, cada agente DEBE cargar el SOT específico del módulo/tipo desde `SourceofTruth/` en lugar de depender de este doc.

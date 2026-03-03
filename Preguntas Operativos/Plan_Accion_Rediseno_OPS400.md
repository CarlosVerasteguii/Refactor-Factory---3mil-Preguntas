# Plan de Acción — Rediseño OPS400 (400 preguntas)

## Contexto

Ángeles revisó la muestra de 25 preguntas operativas y detectó que:

- El lenguaje era demasiado técnico/corporativo para nivel operativo
- Las opciones correctas eran **demasiado obvias** (siempre "sigue la regla" vs 3 que "la rompen")
- Se necesita un rediseño estructural, no solo de redacción

Se investigaron 6 variaciones de diseño SJT anti-faking. Se aprobó un enfoque **híbrido-dominante** donde cada módulo inclina hacia la variación que mejor le queda.

---

## Reglas base (aplican a TODAS las 400 preguntas)

1. **Equiparar tono y longitud** — Las 4 opciones deben sonar igual de razonables, con extensión similar.
2. **Ninguna opción claramente "mala"** — Todas deben reflejar algo que un empleado real haría con buena intención.
3. **Lenguaje operativo** — Máximo 2-3 líneas por escenario, vocabulario de primaria/secundaria, sin jerga corporativa.
4. **Quitar etiquetas** — En la versión final las opciones van como A, B, C, D (no "Correcta / Pragmática / Evasiva / Autojustificada").

---

## Distribución por módulo

| Módulo | Tema | 80 preguntas | Variación dominante | Pregunta cierra con… |
|---|---|---|---|---|
| **M1** | Integridad | 80 | **1A Kidder** (bueno vs. bueno) | ¿Qué haces? |
| **M2** | Adaptabilidad | 80 | **1C Secuencial** | ¿Qué es lo primero que haces? |
| **M3** | Servicio y ética | 80 | **1D Stakeholders** (¿a quién cuidas?) | ¿Qué haces? / ¿Qué haces primero? |
| **M4** | Seguridad | 80 | **1C Secuencial + 1A Kidder** | ¿Qué es lo primero que haces? |
| **M5** | Trabajo en equipo | 80 | **1D Stakeholders + 1E Profundidad** | ¿Qué haces? |

### Detalle por módulo

**M1 — Integridad (Variación 1A Kidder)**

- Cada escenario enfrenta dos valores legítimos: Verdad vs Lealtad, Justicia vs Misericordia, Corto plazo vs Largo plazo.
- Las 4 opciones representan diferentes prioridades éticas, no "seguir regla vs romperla".

**M2 — Adaptabilidad (Variación 1C Secuencial)**

- Preguntar "¿Qué es lo primero que haces?" ante un cambio de puesto, proceso o equipo.
- Las 4 opciones son cosas que un buen empleado haría, pero el orden revela disposición al cambio.

**M3 — Servicio y ética (Variación 1D Stakeholders)**

- Cada opción beneficia a un stakeholder diferente: cliente, compañero, empresa, proceso.
- Ninguna opción es "egoísta obvia"; todas tienen una lógica de servicio.

**M4 — Seguridad (1C + 1A)**

- Combina priorización bajo presión ("¿qué haces primero?") con dilemas de rapidez vs precaución.
- Las opciones representan diferentes grados de prudencia, todas razonables.

**M5 — Trabajo en equipo (1D + 1E)**

- Combina "¿a quién priorizas?" con niveles de profundidad de apoyo (mínimo → sistémico).
- Se evita el sesgo de "integridad = quedarse a trabajar fuera de horario".

---

## Proceso de ejecución

1. **Tomar las 80 preguntas existentes** de cada módulo (ya procesadas en batches JSON).
2. **Reescribir escenarios** aplicando las reglas base + variación dominante del módulo.
3. **Reescribir opciones** equiparando tono, longitud y deseabilidad; quitar etiquetas.
4. **Validar** que un lector externo no pueda identificar la correcta en <10 segundos.
5. **Exportar** al formato JSON del seeder para la app.

---

## Archivos de referencia

| Archivo | Propósito |
|---|---|
| `Comentarios Angeles.md` | Feedback original de Ángeles sobre problemas detectados |
| `Rubrica_Angeles_OPS400.md` | Rúbrica de redacción para nivel operativo |
| `Catalogo_Variaciones_Estrategia1.html` | Informe visual de las 6 variaciones investigadas |
| `Plan_Accion_Rediseno_OPS400.md` | **Este archivo** — plan aprobado |

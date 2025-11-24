# ESTÁNDARES DE REFACTORIZACIÓN MIRA (v2.0 Enterprise)

Este documento define la "Verdad Única" (Single Source of Truth) para la generación y refactorización de reactivos psicométricos. Todos los agentes (Video y Opciones) deben adherirse estrictamente a estas directivas.

---

## 1. REGLAS DE LENGUAJE Y TONO (Globales)

### 🚫 Vocabulario Prohibido (Lista Negra)
El lenguaje debe ser accesible para personal operativo y administrativo medio.
- **PROHIBIDO:** "Stakeholders", "Partes interesadas". -> **USAR:** "Clientes", "Proveedores", "Socios".
- **PROHIBIDO:** "Recursos Humanos", "RR.HH.", "Capital Humano". -> **USAR:** "Personal", "Gente de contratos", "Empleados".
- **PROHIBIDO:** "Activos organizacionales". -> **USAR:** "Equipos", "Herramientas", "Recursos de la empresa".
- **PROHIBIDO:** "Intereses organizacionales". -> **USAR:** "Intereses de la empresa".
- **PROHIBIDO:** Juerga legal o financiera compleja ("Compliance", "Due diligence").

### ✅ Estilo de Redacción
- **Tono:** Profesional pero cotidiano. Ni académico ni coloquial.
- **Longitud:** Máxima concisión.
    - **Situación:** 1-2 oraciones para establecer el contexto.
    - **Dilema:** 1 oración clara que contraste las dos opciones ("Si haces A, pasa X; si haces B, pasa Y").
    - **Total:** No más de 4-5 oraciones por planteamiento.
- **Inicios Variados:** NO empezar siempre con "Imagina que...". Usar:
    - "Te solicitan aprobar..."
    - "Descubres que..."
    - "Durante una reunión..."
    - "Tu supervisor te pide..."

---

## 2. INGENIERÍA DE DIFICULTAD (Física del Dilema)

Para que el reactivo sea válido, debe doler elegir la opción correcta.

### Principio de "Costo de la Integridad"
La opción correcta (Alta Integridad/Ética) **NUNCA** debe ser fácil ni gratuita.
- Debe implicar un **costo personal inmediato**: enojo del jefe, rechazo del equipo, perder un bono, trabajar horas extra, quedar como "lento" o "conflictivo".
- **PROHIBIDO:** Escenarios donde ser honesto te convierte en héroe y todos te aplauden al instante.

### Diseño de Opciones Incorrectas (Seductoras)
Las opciones incorrectas no deben parecer "malvadas", deben parecer **lógicas** o **necesarias**.
1.  **La Opción Pragmática:** "Es lo más eficiente/rápido/lógico para el negocio".
2.  **La Opción Evasiva:** "No es mi problema, mejor no me meto para no salir quemado".
3.  **La Opción Racionalizada:** "Lo hago por el bien del equipo/empresa, aunque rompa una regla pequeña".

---

## 3. FORMATOS ESPECÍFICOS POR TIPO

### 🎥 TIPO A: VIDEO (Preguntas Abiertas)
**Bloques Impares (1, 3, 5, 7, 9)**

**Estructura Obligatoria:**
1.  **Contexto:** Situación específica y concreta (quién, qué, dónde).
2.  **Complicación:** El factor de presión (tiempo, autoridad, dinero).
3.  **Dilema Explicito:** Contrastar las dos rutas principales.
    * "Si haces [Correcto], sufres [Consecuencia Negativa]."
    * "Si haces [Incorrecto], obtienes [Beneficio Inmediato]."
4.  **Cierre:** "¿Qué harías? Explica tu razonamiento."

**Ejemplo Perfecto (Video):**
> "Tu supervisor te pide registrar como 'gasto menor' una compra grande para que no llame la atención, porque si no se aprueba hoy se cae un proyecto importante. Si aceptas, ayudas a que el proyecto siga pero ocultas un gasto que rompe el presupuesto; si te niegas, el proyecto se puede perder y tu jefe puede decir que no apoyaste al equipo. ¿Qué harías? Explica tu razonamiento."

---

### 🔠 TIPO B: OPCIONES (Opción Múltiple)
**Bloques Pares (2, 4, 6, 8, 10)**

**Estructura Obligatoria:**
1.  **Escenario:** Breve descripción del problema (sin explicar el dilema tanto como en video).
2.  **4 Opciones (Sin etiquetas A, B, C, D en el texto, solo el contenido):**
    * **Opción 1 (Alta Integridad con Costo):** Cumple la regla al 100% aunque genere fricción o pérdida.
    * **Opción 2 (Pragmática):** Solución intermedia/rápida que compromete levemente la ética.
    * **Opción 3 (Evasiva/Política):** Evita el conflicto directo, delega o calla.
    * **Opción 4 (Racionalización/Complacencia):** Rompe la regla justificándose en la urgencia, costumbre u orden superior.

**Ejemplo Perfecto (Opciones):**
> **Escenario:** "Al cierre del día, la caja marca cierto monto pero el dinero contado es más. Tu supervisor dice que 'seguro alguien cobró de más sin mala intención' y que lo mejor es dejarlo así para evitar una auditoría larga."
>
> **Opciones:**
> - Pides que se registre la diferencia y se revisen los tickets, aunque todos deban quedarse tarde y tu supervisor se moleste. (Alta Integridad)
> - Cierras la caja como está, pero al día siguiente comentas casualmente que deberían mejorar el control. (Evasiva)
> - Ajustas los montos en el sistema para que cuadre, pensando que así nadie sale perjudicado. (Racionalización)
> - Cierras la caja sin decir nada, confiando en que si hubo error, el cliente reclamará después. (Pragmática/Pasiva)

---

## 4. GUÍA TEMÁTICA POR MÓDULO

Los agentes deben consultar el `matrix_map.json` para saber qué ID de módulo están procesando y aplicar estos temas.

**Módulo 1: Integridad Laboral (Score I)**
- *Temas:* Dinero, presupuestos, viáticos, robo hormiga, información confidencial, conflicto de interés.
- *Foco:* ¿Robas/Mientes por presión o beneficio?

**Módulo 2: Permanencia (Score M)**
- *Temas:* Cambios de jefe, reestructuras, aumento de carga, feedback injusto, ofertas externas.
- *Foco:* ¿Te vas a la primera dificultad o te adaptas?

**Módulo 3: Ética (Score I)**
- *Temas:* Dilemas morales profundos, seguridad del cliente vs ganancia, impacto social, denunciar a compañeros (whistleblowing).
- *Foco:* ¿Sigues tus principios o sigues a la manada?

**Módulo 4: Riesgo/Control Emocional (Score L)**
- *Temas:* Estrés extremo, insultos de clientes, errores graves públicos, provocaciones de compañeros.
- *Foco:* ¿Explotas/Te paralizas o gestionas la emoción?

**Módulo 5: Apego Laboral (Score C/L)**
- *Temas:* Cultura, rituales, burocracia "inútil", confianza en la dirección, trabajo en equipo vs "yo solo".
- *Foco:* ¿Confías en el sistema o eres cínico?
/**
 * MIRA MISSING BATCH GENERATOR
 * ----------------------------
 * Genera los lotes 7 y 8 (IDs 301-350 y 351-400)
 * siguiendo el formato de 01_processed_json y
 * las reglas de Integridad Laboral (Video).
 *
 * Uso: node tools/generate_missing_batches.js
 */

const fs = require('fs');
const path = require('path');

const OUTPUT_DIR = path.join(__dirname, '../01_processed_json');

const PLACES = [
  'una revisión interna de gastos',
  'el cierre de mes',
  'una visita de un cliente importante',
  'una reunión con tu supervisor',
  'la revisión de viáticos del equipo',
  'la planeación de inventarios',
  'la entrega de un informe sensible',
  'la asignación de turnos complicados',
  'la firma de un contrato clave',
  'la actualización de datos en el sistema'
];

const FACTS = [
  'descubres que un compañero cargó gastos personales como si fueran de trabajo',
  'tu supervisor te pide registrar una compra grande como si fuera un gasto menor para que pase sin revisión',
  'un proveedor te ofrece un regalo caro si aceleras un trámite que depende de ti',
  'notas que ciertos descuentos aplicados a un cliente favorito no están bien justificados en el sistema',
  'detectas que algunos viáticos fueron aprobados sin los comprobantes completos',
  'encuentras productos que faltan en el inventario pero nadie ha registrado mermas',
  'observas que se comparte información sensible por canales no seguros para ahorrar tiempo',
  'ves que los turnos más pesados se asignan siempre a la misma persona que casi nunca se queja',
  'tu jefe te sugiere no detallar ciertos gastos para que el presupuesto parezca equilibrado',
  'descubres que un compañero usa equipo de la empresa para trabajos personales pagados'
];

const CORRECT_ACTIONS = [
  'reportas la situación de forma clara y documentada',
  'pides que se revisen los comprobantes y registros antes de aprobar nada',
  'exiges aplicar las reglas tal como están definidas, aunque retrase el proceso',
  'dejas por escrito tus dudas y solicitas una revisión formal',
  'te niegas a aprobar algo que sabes que no cumple las reglas',
  'informas a un nivel superior que puede intervenir sin perder trazabilidad',
  'insistes en usar los canales formales aunque tome más tiempo',
  'redistribuyes la carga de manera justa aunque genere molestias',
  'registras todos los datos tal cual sucedieron, sin maquillar cifras',
  'pides que se pare el trámite hasta que todo esté en orden'
];

const COSTS = [
  'te arriesgas a que tu jefe se enoje y tengas que invertir más horas en aclaraciones',
  'puedes quedar como quien complica las cosas y retrasa los resultados del equipo',
  'es posible que pierdas un beneficio inmediato y que algunos compañeros te vean como rígido',
  'podrías recibir comentarios negativos por no ser “flexible” cuando hay presión de tiempo',
  'quizá se pierda un bono grupal o una oportunidad de negocio por no apresurar el proceso',
  'puedes ser etiquetado como conflictivo y quedar fuera de futuras facilidades',
  'corres el riesgo de que te excluyan de decisiones informales por ser demasiado estricto',
  'podrías tener que quedarte más tiempo revisando detalles que otros prefieren pasar por alto',
  'puede generarse tensión con tu supervisor directo por cuestionar su instrucción',
  'puedes quedar como quien “no apoya” al equipo cuando hay presión externa'
];

const COMFY_ACTIONS = [
  'dejas que el registro pase tal como te lo piden',
  'apruebas los gastos sin hacer muchas preguntas',
  'decides no decir nada y sigues el flujo normal',
  'ajustas los datos para que cuadren sin levantar alertas',
  'usas atajos en el sistema para que todo se vea en orden',
  'aceptas la explicación informal y sigues adelante',
  'trasladas la responsabilidad a otra persona y te mantienes al margen',
  'repartes las tareas difíciles a quien menos reclama para evitar discusiones',
  'cierras el reporte sin detallar los puntos dudosos',
  'priorizas que todo salga rápido aunque queden huecos en la información'
];

const BENEFITS = [
  'ganas tiempo y evitas discusiones incómodas, aunque refuerzas una práctica injusta',
  'todo parece fluir sin trabas y el equipo te ve como alguien práctico, aunque ignores un posible problema',
  'proteges tu relación con el jefe y evitas fricciones, pero dejas pasar algo que sabes que no está bien',
  'te ahorras trabajo extra y nadie te cuestiona, aunque el registro no refleje la realidad',
  'el indicador inmediato se ve mejor, pero el riesgo de un problema serio aumenta',
  'recibes agradecimientos implícitos por no complicar el proceso, a costa de tu tranquilidad',
  'parece que apoyas al grupo, pero normalizas que las reglas se doblen cuando conviene',
  'terminas a tiempo y sin reclamos, pero alguien carga de manera silenciosa con lo más pesado',
  'evitas entrar en un conflicto abierto, aunque sigues sosteniendo una zona gris',
  'todo queda “resuelto” por ahora, pero sabes que podrías enfrentar consecuencias más adelante'
];

const CLOSINGS = [
  '¿Cómo manejarías esta situación?',
  '¿Qué priorizas y por qué?',
  '¿Vale la pena el conflicto?',
  '¿Cómo justificas tu acción?',
  '¿Qué harías? Explica tu razonamiento.'
];

function buildItem(sourceId, indexInBatch) {
  const idx = indexInBatch;

  const place = PLACES[idx % PLACES.length];
  const fact = FACTS[idx % FACTS.length];
  const correct = CORRECT_ACTIONS[idx % CORRECT_ACTIONS.length];
  const cost = COSTS[idx % COSTS.length];
  const comfy = COMFY_ACTIONS[idx % COMFY_ACTIONS.length];
  const benefit = BENEFITS[idx % BENEFITS.length];
  const closing = CLOSINGS[sourceId % CLOSINGS.length];

  const sentence1 = `Durante ${place}, ${fact}.`;
  const sentence2 = `Si ${correct}, ${cost}; si ${comfy}, ${benefit}.`;
  const sentence3 = closing;

  const refactored = `${sentence1} ${sentence2} ${sentence3}`;

  const analysisNotes = 'Compresión: 3 oraciones. Costos: Tiempo + Social.';

  return {
    source_id: sourceId,
    module_id: 1,
    module_name: 'Integridad Laboral',
    module_score: 'I',
    type: 'video',
    refactored_text: refactored,
    analysis_notes: analysisNotes
  };
}

function generateRange(startId, endId, fileName) {
  const items = [];
  let index = 0;
  for (let id = startId; id <= endId; id++, index++) {
    items.push(buildItem(id, index));
  }

  const outPath = path.join(OUTPUT_DIR, fileName);
  fs.writeFileSync(outPath, JSON.stringify(items, null, 2), 'utf8');
  console.log(`Archivo generado: ${outPath} (${items.length} items)`);
}

function main() {
  generateRange(301, 350, 'batch_07_IDs_301-350.json');
  generateRange(351, 400, 'batch_08_IDs_351-400.json');
}

if (require.main === module) {
  main();
}


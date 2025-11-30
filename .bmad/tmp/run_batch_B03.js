const fs = require('fs');
const path = require('path');

// Ensure directory exists
const outDir = '01_processed_json/module2/block-B03';
if (!fs.existsSync(outDir)){
    fs.mkdirSync(outDir, { recursive: true });
}

// Simulated refactor based on SOT (Module 2 Video) 
// Target: 65-80 words, 300-380 chars.
const refactored_items = [
    "Tras la reestructura, tu nuevo jefe te humilla al rehacer tu trabajo ante todos. Dos líderes que lo retaron fueron degradados. Si vas a RRHH, te marcan como conflictivo y arriesgas tu puesto clave; si te adaptas, aceptas jornadas largas que dañan tu salud y validas un estilo que ya rompe al equipo. ¿Qué decides hacer para cuidar tu integridad y tu permanencia en la firma?",
    "Un gerente clave renuncia y tu jefe te asigna sus proyectos sin ajuste de sueldo, dándote solo promesas vagas. Si aceptas esta carga extra, cometerás fallos por el exceso que te imputarán a ti; si marcas límites claros, tu jefe dejará constancia de tu falta de flexibilidad, sacándote del plan de ascenso. ¿Cómo proteges tu carrera sin romper la buena relación hoy en este caso?",
    "La empresa elimina el modelo híbrido y exige oficina total, aunque vivas lejos. El director rotará a quien pida trato especial. Si aceptas, duplicas gastos y pierdes tiempo vital para cuidar a tu dependiente; si te opones, recibirás la etiqueta de poco fiel al rol justo antes de los despidos. ¿Cómo decides actuar ante esta nueva norma para no afectar tu vida ni tu empleo?",
    "Tras la compra, tu proyecto se pausa y te dan tareas menores mientras deciden cierres. Si aceptas este limbo, tu portafolio pierde peso y te quedas sin metas para defenderte; si presionas para moverte, te marcarán como un mal elemento y serás el primero en la lista de ajustes. ¿Qué estrategia sigues para conservar tu impacto y asegurar tu permanencia hoy en esta nueva etapa?",
    "Tras la fusión, tienes dos jefes con metas opuestas: uno pide mucha prisa, el otro rigor total hoy. Si sigues a uno, el otro bloquea tu nota anual y tus días libres; si esperas órdenes unificadas, los proyectos se frenan y ambos te culpan por tu indecisión. ¿Cómo resuelves este doble mando sin sabotear tu permanencia y tu reputación profesional hoy en esta gran empresa?",
    "No reemplazan a un colega y te dan su carga sin pago extra alguno. El director pide resultados para el bono. Si aceptas todo, harás errores que pueden causar tu despido; si pides repartir tareas, quedarás fuera de proyectos clave y perderás la buena imagen vital para mantenerte. ¿Cómo manejas la sobrecarga para asegurar tu lugar seguro en el equipo sin fallar a nadie ahora?",
    "Tu nuevo gerente cambia tu proceso por uno importado que falla y te pide liderarlo. Si te opones, te dirán resistente al cambio y te excluirán; si obedeces sin dudar, dañas la operación y te culparán al caer los números. ¿Cómo proteges tu buen nombre y fama y tu puesto ante esta orden dura y riesgosa para no perder tu valor real en la empresa?",
    "Tu rol se automatiza con la IA que tú debes entrenar, mientras evalúan un despido masivo global. Si enseñas todo lo que sabes, te quedas sin tareas únicas para defenderte; si frenas el entrenamiento, te arriesgas a una sanción grave por un acto desleal. ¿Qué haces para cuidar tu gran valor y permanencia ante este dilema tecnológico y conservar tu empleo actual en la firma?",
    "La dirección congela ascensos, duplica metas y exige el fin de semana sin pago extra. Quienes se quejaron fueron apartados. Si aceptas, das todo tu tiempo gratis y rozas el colapso real; si cuestionas, sales de los planes clave que deciden quién se queda aquí. ¿Cómo respondes a esta gran presión para asegurar bien tu futuro laboral sin dañar tu salud mental hoy en tu trabajo?",
    "Te piden crear la tienda digital sin saber cómo y con un tiempo irreal. Si pides ayuda, te reemplazan y dirán ya que no pudiste; si aceptas, usarás datos de base que no dominas y un gran error justificará tu salida. ¿Qué plan sigues para adaptarte y proteger tu permanencia ante este riesgo inminente y evitar ser despedido por fallar al entregar todo el proyecto?"
];

const output = refactored_items.map((text, index) => {
    const id = `block-B03-q${String(index + 1).padStart(3, '0')}`;
    const words = text.split(/\s+/).length;
    const chars = text.length;
    
    let notes = "";
    if (words < 65) notes += "Word count low (<65). ";
    if (words > 80) notes += "Word count high (>80). ";
    if (chars < 300) notes += "Char count low (<300). ";
    if (chars > 380) notes += "Char count high (>380). ";
    
    const status = (words >= 65 && words <= 80 && chars >= 300 && chars <= 380) ? "ok" : "frozen";
    
    return {
        id: id,
        module_id: 2,
        type: "video",
        refactored_text: text,
        notes: notes.trim() || "Clean",
        sot_checksum: "sot_m2_v_e4f1",
        audit_status: status,
        length_stats: `Words: ${words}, Chars: ${chars}`
    };
});

const jsonl = output.map(item => JSON.stringify({
    id: item.id,
    source_file: "00_raw_data/3Bloque.md",
    agent: "pipeline-orchestrator",
    step: "audit",
    status: item.audit_status,
    note: item.notes,
    timestamp: new Date().toISOString()
})).join('\n');

fs.writeFileSync(path.join(outDir, 'batch-01.json'), JSON.stringify(output, null, 2));
fs.writeFileSync(path.join(outDir, 'batch-01.jsonl'), jsonl);

console.log(`Batch 01 written to ${outDir}`);
console.log("Items processed:", output.length);
output.forEach(item => {
    if(item.audit_status !== 'ok') console.log(`Warning: Item ${item.id} status is ${item.audit_status} (${item.notes}) Length: Words=${item.length_stats}`);
});
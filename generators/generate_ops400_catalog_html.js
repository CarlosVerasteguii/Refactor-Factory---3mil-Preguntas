/**
 * OPS400 HTML CATALOG GENERATOR
 * -----------------------------
 * Toma los primeros 5 reactivos del batch-01.json de cada módulo (1..5)
 * en `01_processed_json_ops400/` y genera un HTML listo para imprimir / PDF.
 *
 * Uso:
 *   node generators/generate_ops400_catalog_html.js
 */

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const ROOT = path.join(__dirname, '..');
const INPUT_ROOT = path.join(ROOT, '01_processed_json_ops400');
const OUTPUT_PATH = path.join(
  ROOT,
  'Preguntas Operativos',
  'Catalogo_Muestra_Batch01_OPS400.html',
);

const MODULES = [
  { id: 1, theme: 'Integridad', color: 'blue' },
  { id: 2, theme: 'Adaptabilidad', color: 'green' },
  { id: 3, theme: 'Servicio y ética', color: 'orange' },
  { id: 4, theme: 'Seguridad', color: 'purple' },
  { id: 5, theme: 'Trabajo en equipo', color: 'teal' },
];

const OPTION_MAPPING = [
  { key: 'integrity_correct', label: 'Correcta', isCorrect: true },
  { key: 'pragmatic_distractor', label: 'Distractor', isCorrect: false },
  { key: 'evasive_distractor', label: 'Distractor', isCorrect: false },
  { key: 'rationalized_distractor', label: 'Distractor', isCorrect: false },
];

function escapeHtml(value) {
  return String(value ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/\"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

function walk(dir) {
  const out = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) out.push(...walk(full));
    else out.push(full);
  }
  return out;
}

function findBatch01Json(moduleDir) {
  if (!fs.existsSync(moduleDir)) {
    throw new Error(`No existe el directorio: ${moduleDir}`);
  }

  const matches = walk(moduleDir)
    .filter((p) => path.basename(p).toLowerCase() === 'batch-01.json')
    .sort((a, b) => a.localeCompare(b));

  if (matches.length === 0) {
    throw new Error(`No encontré batch-01.json dentro de: ${moduleDir}`);
  }

  if (matches.length > 1) {
    throw new Error(
      `Encontré múltiples batch-01.json dentro de ${moduleDir}:\n- ${matches.join(
        '\n- ',
      )}`,
    );
  }

  return matches[0];
}

function seededRng(seedText) {
  const hash = crypto.createHash('sha256').update(seedText).digest();
  let state = hash.readUInt32LE(0) || 1;

  return () => {
    // xorshift32
    state ^= state << 13;
    state ^= state >>> 17;
    state ^= state << 5;
    // uint32 -> [0,1)
    return (state >>> 0) / 0x100000000;
  };
}

function seededShuffle(array, seedText) {
  const rand = seededRng(seedText);
  const out = [...array];
  for (let i = out.length - 1; i > 0; i--) {
    const j = Math.floor(rand() * (i + 1));
    [out[i], out[j]] = [out[j], out[i]];
  }
  return out;
}

function loadQuestionsForModule(moduleId) {
  const moduleDir = path.join(INPUT_ROOT, `module${moduleId}`);
  const batchPath = findBatch01Json(moduleDir);
  const raw = fs.readFileSync(batchPath, 'utf8');
  const parsed = JSON.parse(raw);
  if (!Array.isArray(parsed)) {
    throw new Error(`El JSON no es un array: ${batchPath}`);
  }
  return { batchPath, items: parsed };
}

function getShuffledOptions(question, moduleId, letters) {
  const rawOptions = OPTION_MAPPING.map((mapping) => {
    const text = question.options_structured?.[mapping.key];
    if (!text) return null;
    return { key: mapping.key, text, isCorrect: mapping.isCorrect };
  }).filter(Boolean);

  return seededShuffle(rawOptions, `${question.id}::${moduleId}`).map((option, index) => ({
    ...option,
    letter: letters[index] ?? '?',
  }));
}

function buildHtml({ modulesData }) {
  const now = new Date();
  const dateLabel = now.toLocaleDateString('es-MX', {
    year: 'numeric',
    month: 'long',
    day: '2-digit',
  });

  const totalQuestions = modulesData.reduce(
    (acc, m) => acc + m.questions.length,
    0,
  );

  const toolbar = `
    <div class="toolbar no-print">
      <button class="btn" id="toggleKeysBtn" type="button">Mostrar clave</button>
      <button class="btn primary" type="button" onclick="window.print()">Imprimir / Guardar PDF</button>
    </div>
  `;

  const cover = `
    <div class="cover">
      <div class="cover-tag">OPS400 · Operativo · Muestra batch 01</div>
      <h1>Muestra de preguntas OPS400</h1>
      <p class="subtitle">5 preguntas por módulo (tomadas del primer batch) para revisión y lectura rápida.</p>
      <div class="cover-meta">
        <span>${escapeHtml(dateLabel)}</span>
        <span>${totalQuestions} preguntas</span>
        <span>5 módulos</span>
      </div>
      <div class="cover-note">Tip: puedes activar “Mostrar clave” antes de imprimir si quieres incluir respuestas correctas.</div>
    </div>
  `;

  const sources = modulesData
    .map(
      (m) =>
        `<li><strong>M${m.moduleId}</strong> — ${escapeHtml(
          m.batchPath.replace(ROOT + path.sep, ''),
        )}</li>`,
    )
    .join('\n');

  const intro = `
    <div class="container">
      <div class="info-box">
        <h2>Fuente</h2>
        <ul class="source-list">
          ${sources}
        </ul>
      </div>
  `;

  const letters = ['A', 'B', 'C', 'D'];

  let overallQuestionIndex = 0;

  const moduleSections = modulesData
    .map((mod, moduleIndex) => {
      const header = `
        <div class="section-header">
          <div class="section-number mod-${mod.color}">M${mod.moduleId}</div>
          <div class="section-title">
            <h2>${escapeHtml(mod.theme)}</h2>
            <div class="section-subtitle">Batch 01 · Primeras 5 preguntas</div>
          </div>
        </div>
      `;

      const cards = mod.questions
        .map((q, idx) => {
          overallQuestionIndex += 1;
          const reviewIndex = overallQuestionIndex;
          const scenario = escapeHtml(q.scenario).replace(/\n/g, '<br>');
          const options = getShuffledOptions(q, mod.moduleId, letters);

          const correct = options.find((o) => o.isCorrect);
          const correctLetter = correct?.letter ?? '?';

          const optionsHtml = options
            .map((o) => {
              const optionText = escapeHtml(o.text).replace(/\n/g, '<br>');
              const correctClass = o.isCorrect ? ' is-correct' : '';
              return `
                <li class="option opt-${o.letter.toLowerCase()}${correctClass}">
                  <span class="opt-letter">${o.letter}</span>
                  <span class="opt-text">${optionText}</span>
                </li>
              `;
            })
            .join('\n');

          return `
            <div class="question-card mod-${mod.color}">
              <div class="question-header">
                <div class="q-left">
                  <div class="q-number">Pregunta ${reviewIndex}/${totalQuestions}</div>
                  <div class="q-meta">M${mod.moduleId} · ${idx + 1}/5 del módulo</div>
                  <div class="q-id">${escapeHtml(q.id)}</div>
                </div>
                <div class="q-right">
                  <span class="history-pill">Histórica ${reviewIndex}/${totalQuestions}</span>
                  <span class="answer-pill">Correcta: <strong>${escapeHtml(
                    correctLetter,
                  )}</strong></span>
                </div>
              </div>
              <div class="question-body">
                <div class="scenario">${scenario}</div>
                <ol class="options-list">
                  ${optionsHtml}
                </ol>
              </div>
            </div>
          `;
        })
        .join('\n');

      const pageBreak = moduleIndex === modulesData.length - 1 ? '' : '';
      return `${header}\n${cards}\n${pageBreak}`;
    })
    .join('\n');

  const answerKeyRows = modulesData
    .flatMap((mod) =>
      mod.questions.map((q, idx) => {
        const sampleIndex = mod.questions.indexOf(q);
        const options = getShuffledOptions(q, mod.moduleId, letters);
        const correct = options.find((o) => o.isCorrect);
        return {
          moduleId: mod.moduleId,
          theme: mod.theme,
          id: q.id,
          modulePosition: idx + 1,
          samplePosition: sampleIndex,
          correctLetter: correct?.letter ?? '?',
        };
      }),
    )
    .map((r, index) => `
        <tr>
          <td>${escapeHtml(index + 1)}</td>
          <td>M${escapeHtml(r.moduleId)}</td>
          <td>${escapeHtml(r.theme)}</td>
          <td><code>${escapeHtml(r.id)}</code></td>
          <td><strong>${escapeHtml(r.correctLetter)}</strong></td>
        </tr>
      `)
    .join('\n');

  const answerKey = `
      <div class="answer-key">
        <div class="section-header">
          <div class="section-number key">✓</div>
          <div class="section-title">
            <h2>Clave (opcional)</h2>
            <div class="section-subtitle">Se muestra solo si activas “Mostrar clave”</div>
          </div>
        </div>

        <table class="key-table">
          <thead>
            <tr>
              <th>#</th>
              <th>Módulo</th>
              <th>Tema</th>
              <th>ID</th>
              <th>Correcta</th>
            </tr>
          </thead>
          <tbody>
            ${answerKeyRows}
          </tbody>
        </table>
      </div>
    </div>
  `;

  const styles = `
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700;800&display=swap');

      :root {
        --primary: #15314b;
        --primary-light: #295e8a;
        --success: #38a169;
        --blue: #1f5f99;
        --green: #28714a;
        --orange: #b55d1e;
        --purple: #6a4ea1;
        --teal: #16666a;
        --gray-50: #f7fafc;
        --gray-100: #edf2f7;
        --gray-200: #e2e8f0;
        --gray-300: #cbd5e0;
        --gray-500: #718096;
        --gray-600: #4a5568;
        --gray-700: #2d3748;
        --gray-800: #1a202c;
        --shadow: 0 2px 10px rgba(0,0,0,0.05);
      }

      * { margin: 0; padding: 0; box-sizing: border-box; }

      body {
        font-family: 'Source Sans 3', Georgia, serif;
        color: var(--gray-700);
        line-height: 1.55;
        background: white;
        font-size: 11pt;
      }

      @media print {
        body { font-size: 10pt; }
        .no-print { display: none !important; }
        .page-break { page-break-before: always; }
        @page { margin: 1cm 1.1cm; size: letter; }
      }

      .toolbar {
        position: fixed;
        top: 18px;
        right: 18px;
        display: flex;
        gap: 10px;
        z-index: 5;
      }

      .btn {
        border: 1px solid var(--gray-300);
        background: white;
        color: var(--gray-800);
        padding: 10px 14px;
        border-radius: 999px;
        font-weight: 600;
        font-size: 0.9rem;
        cursor: pointer;
        box-shadow: var(--shadow);
      }
      .btn.primary {
        background: var(--primary);
        border-color: var(--primary);
        color: white;
      }
      .btn:hover { transform: translateY(-1px); }

      .cover {
        text-align: center;
        padding: 32px 28px 26px;
        background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
        color: white;
        border-top: 12px solid #d99a2b;
        border-bottom: 6px solid #d99a2b;
        border-radius: 0 0 14px 14px;
        margin-bottom: 20px;
      }
      .cover-tag {
        display: inline-block;
        border: 2px solid rgba(255,255,255,0.7);
        padding: 4px 14px;
        border-radius: 999px;
        font-size: 0.8rem;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 14px;
      }
      .cover h1 {
        font-size: 2.05rem;
        font-weight: 800;
        margin-bottom: 8px;
        line-height: 1.15;
      }
      .cover .subtitle {
        font-size: 1.08rem;
        font-weight: 600;
        opacity: 0.92;
        max-width: 860px;
        margin: 0 auto 14px;
      }
      .cover-meta {
        display: flex;
        justify-content: center;
        gap: 18px;
        font-size: 0.9rem;
        opacity: 0.9;
        flex-wrap: wrap;
      }
      .cover-note {
        margin-top: 18px;
        font-size: 0.9rem;
        opacity: 0.9;
      }

      .container {
        max-width: 1120px;
        margin: 0 auto;
        padding: 6px 16px 28px;
      }

      .info-box {
        background: white;
        border: 2px solid var(--gray-200);
        border-left: 8px solid var(--primary);
        border-radius: 14px;
        padding: 14px 16px;
        margin-bottom: 18px;
      }
      .info-box h2 {
        font-size: 1.1rem;
        color: var(--gray-800);
        margin-bottom: 8px;
      }
      .source-list {
        margin-left: 18px;
        columns: 2;
        column-gap: 28px;
        color: var(--gray-600);
        font-size: 0.92rem;
      }
      .source-list li { margin-bottom: 4px; }

      .section-header {
        display: flex;
        align-items: center;
        gap: 14px;
        margin: 18px 0 10px;
        padding-bottom: 10px;
        border-bottom: 3px solid var(--primary);
        page-break-after: avoid;
      }

      .section-number {
        color: var(--primary);
        width: 38px;
        height: 38px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 800;
        font-size: 0.95rem;
        flex-shrink: 0;
        background: white;
        border: 3px solid var(--primary);
      }
      .section-number.mod-blue { color: var(--blue); border-color: var(--blue); }
      .section-number.mod-green { color: var(--green); border-color: var(--green); }
      .section-number.mod-orange { color: var(--orange); border-color: var(--orange); }
      .section-number.mod-purple { color: var(--purple); border-color: var(--purple); }
      .section-number.mod-teal { color: var(--teal); border-color: var(--teal); }
      .section-number.key { color: var(--green); border-color: var(--green); }

      .section-title h2 {
        font-size: 1.25rem;
        color: var(--primary);
        font-weight: 800;
        line-height: 1.2;
      }
      .section-subtitle {
        font-size: 0.9rem;
        color: var(--gray-500);
        margin-top: 2px;
      }

      .question-card {
        border: 2px solid var(--gray-200);
        border-left-width: 9px;
        border-radius: 14px;
        overflow: hidden;
        margin-bottom: 14px;
        box-shadow: var(--shadow);
        break-inside: avoid;
        page-break-inside: avoid;
        background: white;
      }
      .question-card.mod-blue { border-left-color: var(--blue); }
      .question-card.mod-green { border-left-color: var(--green); }
      .question-card.mod-orange { border-left-color: var(--orange); }
      .question-card.mod-purple { border-left-color: var(--purple); }
      .question-card.mod-teal { border-left-color: var(--teal); }

      .question-header {
        padding: 10px 14px 8px;
        color: var(--gray-800);
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 14px;
        border-bottom: 2px solid var(--gray-200);
        background: white;
      }

      .q-left { min-width: 0; }
      .q-number {
        font-weight: 800;
        font-size: 1.08rem;
        line-height: 1.1;
        color: var(--gray-800);
      }
      .q-meta {
        font-size: 0.88rem;
        color: var(--gray-600);
        margin-top: 2px;
      }
      .q-id {
        font-size: 0.8rem;
        color: var(--gray-500);
        margin-top: 1px;
        word-break: break-all;
      }

      .history-pill,
      .answer-pill {
        display: none;
        border: 2px solid var(--gray-300);
        color: var(--gray-800);
        padding: 5px 10px;
        border-radius: 999px;
        font-size: 0.85rem;
        white-space: nowrap;
        font-weight: 700;
      }
      .history-pill { display: inline-flex; }
      .q-right {
        display: flex;
        align-items: center;
        gap: 8px;
        flex-wrap: wrap;
        justify-content: flex-end;
      }

      body.show-keys .answer-pill { display: inline-flex; }

      .question-body {
        padding: 12px 14px 12px;
        background: white;
      }

      .scenario {
        background: white;
        border: 2px solid var(--gray-200);
        border-left: 6px solid var(--primary);
        border-radius: 10px;
        padding: 11px 12px;
        color: var(--gray-800);
        font-size: 0.98rem;
        margin-bottom: 10px;
      }

      .options-list {
        list-style: none;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 8px 10px;
        padding: 0;
      }

      .option {
        display: flex;
        gap: 10px;
        align-items: flex-start;
        padding: 10px 12px;
        border-radius: 10px;
        border: 2px solid var(--gray-200);
        border-left-width: 6px;
        background: white;
      }

      .opt-letter {
        width: 28px;
        height: 28px;
        border-radius: 9px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 900;
        flex-shrink: 0;
        background: white;
        border: 2px solid currentColor;
      }

      .opt-a { color: #1f5f99; border-left-color: #1f5f99; }
      .opt-b { color: #28714a; border-left-color: #28714a; }
      .opt-c { color: #b07900; border-left-color: #b07900; }
      .opt-d { color: #b43c74; border-left-color: #b43c74; }

      .opt-text {
        font-size: 0.95rem;
        color: var(--gray-800);
      }

      body.show-keys .option.is-correct {
        border-color: #38a169;
        box-shadow: 0 0 0 2px rgba(56,161,105,0.18) inset;
      }

      .answer-key { display: none; margin-top: 28px; }
      body.show-keys .answer-key { display: block; }

      .key-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.9rem;
        margin-top: 10px;
      }
      .key-table th {
        background: white;
        color: var(--primary);
        text-align: left;
        padding: 10px 12px;
        font-weight: 700;
        font-size: 0.85rem;
        border-bottom: 2px solid var(--primary);
      }
      .key-table td {
        padding: 9px 12px;
        border-bottom: 1px solid var(--gray-200);
        vertical-align: top;
      }
      .key-table tr:nth-child(even) { background: var(--gray-50); }

      code { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace; font-size: 0.88em; }

      @media (max-width: 860px) {
        .container { padding: 6px 12px 24px; }
        .source-list { columns: 1; }
        .options-list { grid-template-columns: 1fr; }
        .question-header {
          align-items: flex-start;
          flex-direction: column;
        }
        .q-right { justify-content: flex-start; }
      }
    </style>
  `;

  const script = `
    <script>
      (function () {
        const btn = document.getElementById('toggleKeysBtn');
        const updateLabel = () => {
          const on = document.body.classList.contains('show-keys');
          btn.textContent = on ? 'Ocultar clave' : 'Mostrar clave';
        };
        btn.addEventListener('click', () => {
          document.body.classList.toggle('show-keys');
          updateLabel();
        });
        updateLabel();
      })();
    </script>
  `;

  return `<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Muestra de preguntas OPS400 — Batch 01</title>
    ${styles}
  </head>
  <body>
    ${toolbar}
    ${cover}
    ${intro}
    ${moduleSections}
    ${answerKey}
    ${script}
  </body>
</html>
`;
}

function main() {
  if (!fs.existsSync(INPUT_ROOT)) {
    throw new Error(`No existe: ${INPUT_ROOT}`);
  }

  const modulesData = MODULES.map((m) => {
    const { batchPath, items } = loadQuestionsForModule(m.id);
    const questions = items.slice(0, 5);

    if (questions.length < 5) {
      throw new Error(
        `El batch-01 del módulo ${m.id} tiene menos de 5 preguntas: ${batchPath}`,
      );
    }

    return {
      moduleId: m.id,
      theme: m.theme,
      color: m.color,
      batchPath,
      questions,
    };
  });

  const html = buildHtml({ modulesData });

  const outDir = path.dirname(OUTPUT_PATH);
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });
  fs.writeFileSync(OUTPUT_PATH, html, 'utf8');

  const printable = OUTPUT_PATH.replace(ROOT + path.sep, '');
  console.log(`✅ HTML generado: ${printable}`);
}

try {
  main();
} catch (err) {
  console.error('🔥 Error generando el catálogo OPS400:', err?.message || err);
  process.exit(1);
}

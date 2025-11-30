const fs = require('fs');
const path = require('path');

// Configuration
const MODULE_ID = 1;
const BLOCK_ID = 'B02';
const BATCH_SIZE = 10;
const BATCH_START_INDEX = 1;
const INPUT_PATH = '00_raw_data/2Bloque.md';
const SOT_CHECKSUM = '2a4932b4b285f5288a0e022991b87184';
const TARGET_TYPE = 'options';

// Ensure directory exists
const outDir = `1/block-${BLOCK_ID}`;
if (!fs.existsSync(outDir)){
    fs.mkdirSync(outDir, { recursive: true });
}

// Read input file and extract items
const inputContent = fs.readFileSync(INPUT_PATH, 'utf8');
const insertPattern = /INSERT INTO.*?VALUES \(1, 'opciones', N'(.*?)', N'(.*?)'\);/gs;
const matches = [...inputContent.matchAll(insertPattern)];

console.log(`Found ${matches.length} total items in ${INPUT_PATH}`);

// Extract batch (start from index 0-based)
const batchItems = matches.slice(BATCH_START_INDEX - 1, BATCH_START_INDEX - 1 + BATCH_SIZE);

console.log(`Processing batch: indices ${BATCH_START_INDEX} to ${BATCH_START_INDEX + BATCH_SIZE - 1}`);

// Helper functions
function countWords(text) {
    return text.trim().split(/\s+/).length;
}

function normalizeText(text) {
    // Unescape SQL escaped quotes
    return text.replace(/''/g, "'");
}

function parseOptions(optionsJson) {
    const parsed = JSON.parse(optionsJson);
    return parsed.opciones || [];
}

// Process each item
const output = batchItems.map((match, index) => {
    const rawScenario = normalizeText(match[1]);
    const rawOptions = normalizeText(match[2]);

    const id = `block-${BLOCK_ID}-q${String(BATCH_START_INDEX + index).padStart(3, '0')}`;

    let scenario = rawScenario;
    let words = countWords(scenario);
    let chars = scenario.length;

    // Parse options
    let options = [];
    try {
        options = parseOptions(rawOptions);
    } catch(e) {
        console.error(`Error parsing options for ${id}:`, e.message);
    }

    // Length guard validation
    let length_notes = [];
    if (words < 65) length_notes.push(`Word count low (${words} < 65)`);
    if (words > 80) length_notes.push(`Word count high (${words} > 80)`);
    if (chars < 300) length_notes.push(`Char count low (${chars} < 300)`);
    if (chars > 380) length_notes.push(`Char count high (${chars} > 380)`);

    const length_status = (words >= 65 && words <= 80 && chars >= 300 && chars <= 380) ? "ok" : "frozen";

    // Audit validation (basic checks)
    let audit_notes = [];
    if (options.length !== 4) audit_notes.push(`Options count mismatch (${options.length} !== 4)`);
    if (!rawScenario.includes('¿')) audit_notes.push('Missing question mark');

    // Map to structured options (based on psychometric roles)
    const options_structured = {
        integrity_correct: options[0] || "",
        pragmatic_distractor: options[1] || "",
        evasive_distractor: options[2] || "",
        rationalized_distractor: options[3] || ""
    };

    const audit_status = (length_status === "ok" && audit_notes.length === 0) ? "ok" : "frozen";

    return {
        id,
        module_id: MODULE_ID,
        block_id: BLOCK_ID,
        type: TARGET_TYPE,
        scenario,
        options_structured,
        word_count: words,
        char_count: chars,
        length_status,
        length_notes: length_notes.join('; ') || null,
        audit_status,
        audit_notes: audit_notes.join('; ') || null,
        notes: `Raw item from ${INPUT_PATH}. Needs refactoring if frozen.`,
        sot_checksum: SOT_CHECKSUM
    };
});

// Generate JSONL log
const jsonl = output.map(item => JSON.stringify({
    id: item.id,
    source_file: INPUT_PATH,
    agent: "pipeline-orchestrator",
    step: "length-guard",
    status: item.length_status,
    note: item.length_notes || "OK",
    word_count: item.word_count,
    char_count: item.char_count,
    timestamp: new Date().toISOString()
})).join('\n');

// Write output files
const batchNum = String(Math.floor((BATCH_START_INDEX - 1) / BATCH_SIZE) + 1).padStart(3, '0');
fs.writeFileSync(path.join(outDir, `batch-${batchNum}.json`), JSON.stringify(output, null, 2));
fs.writeFileSync(path.join(outDir, `batch-${batchNum}.jsonl`), jsonl);

console.log(`\nBatch ${batchNum} written to ${outDir}/`);
console.log(`Items processed: ${output.length}`);
console.log(`\n=== LENGTH-GUARD REPORT ===`);

let frozen_count = 0;
output.forEach(item => {
    if(item.length_status !== 'ok') {
        frozen_count++;
        console.log(`❌ FROZEN: ${item.id} - Words: ${item.word_count} (65-80), Chars: ${item.char_count} (300-380)`);
        if (item.length_notes) console.log(`   Reason: ${item.length_notes}`);
    } else {
        console.log(`✓ OK: ${item.id} - Words: ${item.word_count}, Chars: ${item.char_count}`);
    }
});

console.log(`\n=== SUMMARY ===`);
console.log(`Total items: ${output.length}`);
console.log(`Passed: ${output.length - frozen_count}`);
console.log(`Frozen: ${frozen_count}`);

if (frozen_count > 0) {
    console.log(`\n⚠️  FAIL-FAST: ${frozen_count} item(s) frozen. Refactoring required before proceeding.`);
    process.exit(1);
} else {
    console.log(`\n✓ All items passed length-guard. Ready for audit phase.`);
}

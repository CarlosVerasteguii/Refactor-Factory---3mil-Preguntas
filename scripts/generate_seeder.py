#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Seeder Laravel - Seeder Pipeline
Transforma los JSONs consolidados en un seeder PHP Laravel compatible con mira_preguntas.
"""

import json
import sys
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any

# Configuración
INPUT_ROOT = Path("02_final_artifacts/consolidated")
OUTPUT_ROOT = Path("02_final_artifacts/seeders")
LOGS_ROOT = Path("02_final_artifacts/logs")

# Defaults
DEFAULT_CHUNK_SIZE = 50

def log_trace(trace_file: Path, data: Dict[str, Any]) -> None:
    """Escribe línea de trazabilidad en JSONL."""
    with open(trace_file, 'a', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False) + '\n')

def escape_php_string(text: str) -> str:
    """Escapa string para uso seguro en PHP (comillas, backslashes)."""
    # Escapar backslashes primero
    text = text.replace('\\', '\\\\')
    # Escapar comillas simples
    text = text.replace("'", "\\'")
    # Escapar comillas dobles
    text = text.replace('"', '\\"')
    # Escapar $ para evitar interpolación
    text = text.replace('$', '\\$')
    return text

def transform_item(item: Dict[str, Any], row_num: int) -> Dict[str, Any]:
    """Transforma un item del JSON a estructura de la tabla."""
    item_id = item.get('id', 'UNKNOWN')
    module_id = item.get('module_id')
    item_type = item.get('type')
    
    # Obtener texto según tipo
    if item_type == 'video':
        texto = item.get('refactored_text', '')
        opciones = "{}"  # Objeto JSON vacío para videos
    else:  # options
        texto = item.get('scenario', '')
        options_structured = item.get('options_structured', {})
        
        # Orden fijo de las claves psicométricas para convertir a lista
        ordered_keys = [
            "integrity_correct",
            "pragmatic_distractor",
            "evasive_distractor",
            "rationalized_distractor"
        ]
        
        # Extraer textos en orden, validando que existan las claves
        texts = []
        for key in ordered_keys:
            if key in options_structured:
                texts.append(options_structured[key])
            else:
                print(f"    [WARNING] {item_id} falta clave '{key}' en options_structured")
                texts.append("")  # Agregar vacío para mantener la estructura
        
        # Serializar como JSON con formato {"opciones": [...]}
        opciones = json.dumps({"opciones": texts}, ensure_ascii=False)
    
    # Escapar texto para PHP
    texto_escaped = escape_php_string(texto)
    opciones_escaped = escape_php_string(opciones)
    
    # Estructura para insert
    return {
        'modulo': module_id,
        'tipo': item_type,
        'texto': texto_escaped,
        'opciones': opciones_escaped,
        'idioma': 'es',
        # Metadata para logs
        '_id': item_id,
        '_row_num': row_num,
        '_texto_chars': len(texto),
        '_opciones_chars': len(opciones)
    }

def generate_seeder_php(items: List[Dict[str, Any]], chunk_size: int) -> str:
    """Genera el código PHP del seeder."""
    
    # Dividir en chunks
    chunks = []
    for i in range(0, len(items), chunk_size):
        chunk = items[i:i + chunk_size]
        chunks.append(chunk)
    
    php_code = f"""<?php

namespace Database\\Seeders;

use Illuminate\\Database\\Seeder;
use Illuminate\\Support\\Facades\\DB;

class MiraPreguntasSeeder extends Seeder
{{
    /**
     * Run the database seeds.
     * 
     * Generado automáticamente el {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
     * Total items: {len(items)}
     * Chunks: {len(chunks)} (tamaño: {chunk_size})
     */
    public function run()
    {{
        DB::transaction(function () {{
"""
    
    # Agregar cada chunk
    for chunk_idx, chunk in enumerate(chunks, 1):
        php_code += f"\n            // Chunk {chunk_idx}/{len(chunks)} ({len(chunk)} items)\n"
        php_code += "            DB::table('mira_preguntas')->insert([\n"
        
        for item_idx, item in enumerate(chunk):
            comma = "," if item_idx < len(chunk) - 1 else ""
            php_code += f"""                [
                    'modulo' => {item['modulo']},
                    'tipo' => '{item['tipo']}',
                    'texto' => '{item['texto']}',
                    'opciones' => '{item['opciones']}',
                    'idioma' => '{item['idioma']}',
                    'created_at' => now(),
                    'updated_at' => now(),
                ]{comma}
"""
        
        php_code += "            ]);\n"
    
    php_code += """        });
        
        echo "Seeder completado. Items insertados: """ + str(len(items)) + """\\n";
    }
}
"""
    
    return php_code

def main():
    """Función principal."""
    parser = argparse.ArgumentParser(description='Genera seeder Laravel desde JSONs consolidados')
    parser.add_argument('--chunk-size', type=int, default=DEFAULT_CHUNK_SIZE,
                        help=f'Tamaño de chunks para inserts (default: {DEFAULT_CHUNK_SIZE})')
    args = parser.parse_args()
    
    print("=" * 70)
    print("GENERADOR DE SEEDER LARAVEL - SEEDER PIPELINE")
    print("=" * 70)
    print(f"Chunk size: {args.chunk_size}")
    
    # Crear directorios
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    LOGS_ROOT.mkdir(parents=True, exist_ok=True)
    
    # Buscar todos los module*_all.json
    consolidated_files = sorted(INPUT_ROOT.glob("module*_all.json"))
    
    if not consolidated_files:
        print(f"\n[ERROR] No se encontraron archivos consolidados en {INPUT_ROOT}")
        print("   Ejecuta primero: python scripts/consolidate_batches.py")
        sys.exit(1)
    
    print(f"\n[INFO] Encontrados {len(consolidated_files)} archivos consolidados")
    
    all_transformed_items = []
    trace_file = LOGS_ROOT / "seeder_trace.jsonl"
    
    # Limpiar trace anterior
    if trace_file.exists():
        trace_file.unlink()
    
    # Procesar cada archivo consolidado
    for consolidated_file in consolidated_files:
        print(f"\n  [FILE] Procesando {consolidated_file.name}...")
        
        try:
            with open(consolidated_file, 'r', encoding='utf-8') as f:
                module_items = json.load(f)
            
            if not isinstance(module_items, list):
                print(f"    [ERROR] {consolidated_file.name} no es un array JSON")
                sys.exit(1)
            
            print(f"    [OK] {len(module_items)} items cargados")
            
            # Transformar cada item
            for item in module_items:
                row_num = len(all_transformed_items) + 1
                transformed = transform_item(item, row_num)
                all_transformed_items.append(transformed)
                
                # Log de trazabilidad
                log_trace(trace_file, {
                    'id': transformed['_id'],
                    'modulo': transformed['modulo'],
                    'tipo': transformed['tipo'],
                    'texto_chars': transformed['_texto_chars'],
                    'opciones_chars': transformed['_opciones_chars'],
                    'row_num': row_num,
                    'timestamp': datetime.now().isoformat()
                })
            
            print(f"    [OK] {len(module_items)} items transformados")
            
        except json.JSONDecodeError as e:
            print(f"    [ERROR] {consolidated_file.name} tiene JSON malformado")
            print(f"    Error: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"    [ERROR] Error procesando {consolidated_file.name}")
            print(f"    Tipo: {type(e).__name__}")
            print(f"    Mensaje: {str(e)}")
            sys.exit(1)
    
    # Generar seeder PHP
    print(f"\n[BUILD] Generando seeder PHP...")
    print(f"   Total items: {len(all_transformed_items)}")
    print(f"   Chunks: {(len(all_transformed_items) + args.chunk_size - 1) // args.chunk_size}")
    
    seeder_php = generate_seeder_php(all_transformed_items, args.chunk_size)
    
    # Guardar seeder
    seeder_file = OUTPUT_ROOT / "MiraPreguntasSeeder.php"
    with open(seeder_file, 'w', encoding='utf-8') as f:
        f.write(seeder_php)
    
    print(f"   [OK] Seeder generado: {seeder_file}")
    
    # Generar resumen de ejecución
    summary = {
        'timestamp': datetime.now().isoformat(),
        'total_items': len(all_transformed_items),
        'chunk_size': args.chunk_size,
        'chunks_count': (len(all_transformed_items) + args.chunk_size - 1) // args.chunk_size,
        'by_module': {},
        'by_type': {},
        'files_processed': [f.name for f in consolidated_files]
    }
    
    # Estadísticas por módulo
    for item in all_transformed_items:
        modulo = item['modulo']
        tipo = item['tipo']
        
        if modulo not in summary['by_module']:
            summary['by_module'][modulo] = 0
        summary['by_module'][modulo] += 1
        
        if tipo not in summary['by_type']:
            summary['by_type'][tipo] = 0
        summary['by_type'][tipo] += 1
    
    # Guardar resumen
    summary_file = LOGS_ROOT / "execution_summary.json"
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    
    print(f"   [OK] Resumen guardado: {summary_file}")
    
    # Resumen final
    print("\n" + "=" * 70)
    print("RESUMEN DE GENERACIÓN")
    print("=" * 70)
    print(f"Total items: {len(all_transformed_items)}")
    print(f"\nPor módulo:")
    for modulo in sorted(summary['by_module'].keys()):
        print(f"  Módulo {modulo}: {summary['by_module'][modulo]} items")
    print(f"\nPor tipo:")
    for tipo in sorted(summary['by_type'].keys()):
        print(f"  {tipo}: {summary['by_type'][tipo]} items")
    print(f"\n[OK] Trazabilidad guardada en: {trace_file}")
    print(f"[OK] Seeder listo en: {seeder_file}")
    print("=" * 70)

if __name__ == "__main__":
    main()


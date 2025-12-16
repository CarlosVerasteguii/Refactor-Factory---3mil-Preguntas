#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Consolidador de Batches - Seeder Pipeline
Consolida todos los batch-*.json de cada bloque en un all.json por módulo.
Incluye validaciones pre-seeder y trazabilidad completa.
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime
from glob import glob
from typing import List, Dict, Any
import hashlib

# Configurar encoding UTF-8 para Windows
if sys.platform == 'win32':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8')
    os.environ['PYTHONIOENCODING'] = 'utf-8'

# Configuración
INPUT_ROOT = Path("01_processed_json")
OUTPUT_ROOT = Path("02_final_artifacts/consolidated")
LOGS_ROOT = Path("02_final_artifacts/logs")

# Validaciones
MAX_TEXT_LENGTH = 60000
VALID_MODULES = [1, 2, 3, 4, 5]
VALID_TYPES = ['video', 'options']
MIN_BATCHES = 2
MAX_BATCHES = 4

def log_trace(trace_file: Path, data: Dict[str, Any]) -> None:
    """Escribe línea de trazabilidad en JSONL."""
    with open(trace_file, 'a', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False) + '\n')

def validate_item(item: Dict[str, Any], source_batch: str) -> None:
    """Valida un item según criterios pre-seeder. STOP si falla."""
    item_id = item.get('id', 'UNKNOWN')
    
    # Validar module_id
    module_id = item.get('module_id')
    if module_id not in VALID_MODULES:
        print(f"\n❌ ERROR: Item {item_id} tiene module_id={module_id} fuera de rango válido [1-5]")
        print(f"   Source: {source_batch}")
        print(f"   Item completo: {json.dumps(item, indent=2, ensure_ascii=False)}")
        sys.exit(1)
    
    # Validar type
    item_type = item.get('type')
    if item_type not in VALID_TYPES:
        print(f"\n❌ ERROR: Item {item_id} tiene type='{item_type}' inválido. Debe ser 'video' u 'options'")
        print(f"   Source: {source_batch}")
        print(f"   Item completo: {json.dumps(item, indent=2, ensure_ascii=False)}")
        sys.exit(1)
    
    # Obtener texto según tipo
    if item_type == 'video':
        texto = item.get('refactored_text', '')
    else:  # options
        texto = item.get('scenario', '')
    
    # Validar longitud de texto
    texto_length = len(texto)
    if texto_length > MAX_TEXT_LENGTH:
        print(f"\n❌ ERROR: Item {item_id} tiene texto de {texto_length} caracteres (máximo: {MAX_TEXT_LENGTH})")
        print(f"   Source: {source_batch}")
        print(f"   Tipo: {item_type}")
        print(f"   Primeros 200 chars: {texto[:200]}...")
        sys.exit(1)
    
    # Validar encoding UTF-8
    try:
        texto.encode('utf-8')
    except UnicodeEncodeError as e:
        print(f"\n❌ ERROR: Item {item_id} contiene caracteres no-UTF8")
        print(f"   Source: {source_batch}")
        print(f"   Error: {e}")
        print(f"   Bytes problemáticos: {e.object[e.start:e.end]}")
        sys.exit(1)
    
    # Validar options_structured si es tipo options
    if item_type == 'options':
        options = item.get('options_structured')
        if options is None:
            print(f"\n❌ ERROR: Item {item_id} es tipo 'options' pero no tiene 'options_structured'")
            print(f"   Source: {source_batch}")
            sys.exit(1)
        
        # Validar que es JSON válido
        try:
            json.dumps(options, ensure_ascii=False)
        except (TypeError, ValueError) as e:
            print(f"\n❌ ERROR: Item {item_id} tiene options_structured malformado (no es JSON válido)")
            print(f"   Source: {source_batch}")
            print(f"   Error: {e}")
            print(f"   Options: {json.dumps(options, indent=2, ensure_ascii=False)[:500]}")
            sys.exit(1)
        
        # Validar que tiene las 4 opciones requeridas
        required_keys = ['integrity_correct', 'pragmatic_distractor', 'evasive_distractor', 'rationalized_distractor']
        missing = [k for k in required_keys if k not in options]
        if missing:
            print(f"\n❌ ERROR: Item {item_id} le faltan opciones requeridas: {missing}")
            print(f"   Source: {source_batch}")
            print(f"   Opciones presentes: {list(options.keys())}")
            sys.exit(1)

def consolidate_module(module_num: int) -> Dict[str, Any]:
    """Consolida todos los bloques de un módulo."""
    module_path = INPUT_ROOT / f"module{module_num}"
    
    if not module_path.exists():
        print(f"⚠️  WARNING: Módulo {module_num} no existe en {module_path}")
        return {'items': [], 'blocks': []}
    
    all_items = []
    blocks_processed = []
    trace_file = LOGS_ROOT / "consolidation_trace.jsonl"
    
    # Buscar bloques (B01, B02, etc.)
    block_dirs = sorted([d for d in module_path.iterdir() if d.is_dir() and d.name.startswith('block-')])
    
    print(f"\n📦 Módulo {module_num}: Procesando {len(block_dirs)} bloques...")
    
    for block_dir in block_dirs:
        block_id = block_dir.name.replace('block-', '')
        print(f"  🔹 Bloque {block_id}...")
        
        # Buscar todos los batch-*.json
        batch_files = sorted(glob(str(block_dir / "batch-*.json")))
        
        if not batch_files:
            print(f"    ⚠️  WARNING: No se encontraron batches en {block_dir}")
            continue
        
        batch_count = len(batch_files)
        if batch_count < MIN_BATCHES or batch_count > MAX_BATCHES:
            print(f"    ⚠️  WARNING: Bloque {block_id} tiene {batch_count} batches (esperado: {MIN_BATCHES}-{MAX_BATCHES})")
        
        print(f"    📄 Encontrados {batch_count} batches")
        
        block_items = []
        for batch_file in batch_files:
            batch_name = Path(batch_file).name
            print(f"      📄 Procesando {batch_name}...")
            
            try:
                with open(batch_file, 'r', encoding='utf-8') as f:
                    batch_data = json.load(f)
                
                # Manejar dos formatos: array directo o objeto con 'items'
                if isinstance(batch_data, dict):
                    if 'items' in batch_data:
                        batch_data = batch_data['items']
                    else:
                        print(f"        ❌ ERROR: {batch_name} es un objeto pero no tiene campo 'items'")
                        print(f"        Campos encontrados: {list(batch_data.keys())}")
                        sys.exit(1)
                
                if not isinstance(batch_data, list):
                    print(f"        ❌ ERROR: {batch_name} no es un array JSON ni objeto con 'items'")
                    print(f"        Tipo encontrado: {type(batch_data)}")
                    sys.exit(1)
                
                print(f"        ✓ {len(batch_data)} items en batch")
                
                for item in batch_data:
                    # Validar item
                    validate_item(item, f"{block_dir.name}/{batch_name}")
                    
                    # Agregar a lista
                    block_items.append(item)
                    
                    # Log de trazabilidad
                    item_text = item.get('refactored_text') or item.get('scenario', '')
                    log_trace(trace_file, {
                        'id': item.get('id'),
                        'source_batch': f"{block_dir.name}/{batch_name}",
                        'module': module_num,
                        'type': item.get('type'),
                        'checksum': item.get('sot_checksum', ''),
                        'texto_chars': len(item_text),
                        'timestamp': datetime.now().isoformat()
                    })
                    
                    print(f"        ✓ Item {item.get('id')} validado")
                
            except json.JSONDecodeError as e:
                print(f"        ❌ ERROR: {batch_name} tiene JSON malformado")
                print(f"        Error: {e}")
                print(f"        Línea {e.lineno}, columna {e.colno}")
                sys.exit(1)
            except Exception as e:
                print(f"        ❌ ERROR: Error procesando {batch_name}")
                print(f"        Tipo: {type(e).__name__}")
                print(f"        Mensaje: {str(e)}")
                sys.exit(1)
        
        all_items.extend(block_items)
        blocks_processed.append({
            'block_id': block_id,
            'items_count': len(block_items),
            'batches_count': batch_count
        })
        
        print(f"    ✓ Bloque {block_id}: {len(block_items)} items consolidados")
    
    return {
        'items': all_items,
        'blocks': blocks_processed,
        'total_items': len(all_items)
    }

def main():
    """Función principal."""
    print("=" * 70)
    print("CONSOLIDADOR DE BATCHES - SEEDER PIPELINE")
    print("=" * 70)
    
    # Crear directorios de salida
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    LOGS_ROOT.mkdir(parents=True, exist_ok=True)
    
    # Limpiar trace anterior
    trace_file = LOGS_ROOT / "consolidation_trace.jsonl"
    if trace_file.exists():
        trace_file.unlink()
    
    # Procesar cada módulo
    all_modules_data = {}
    total_all_items = 0
    
    for module_num in VALID_MODULES:
        module_data = consolidate_module(module_num)
        all_modules_data[module_num] = module_data
        
        if module_data['items']:
            # Guardar all.json por módulo
            output_file = OUTPUT_ROOT / f"module{module_num}_all.json"
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(module_data['items'], f, ensure_ascii=False, indent=2)
            
            total_all_items += module_data['total_items']
            print(f"\n✓ Módulo {module_num}: {module_data['total_items']} items → {output_file}")
        else:
            print(f"\n⚠️  Módulo {module_num}: Sin items")
    
    # Resumen final
    print("\n" + "=" * 70)
    print("RESUMEN DE CONSOLIDACIÓN")
    print("=" * 70)
    print(f"Total items consolidados: {total_all_items}")
    print(f"Módulos procesados: {len([m for m in all_modules_data.values() if m['items']])}")
    
    for module_num, data in all_modules_data.items():
        if data['items']:
            print(f"\nMódulo {module_num}:")
            print(f"  Items: {data['total_items']}")
            print(f"  Bloques: {len(data['blocks'])}")
            for block in data['blocks']:
                print(f"    - {block['block_id']}: {block['items_count']} items ({block['batches_count']} batches)")
    
    print(f"\n✓ Trazabilidad guardada en: {trace_file}")
    print("=" * 70)

if __name__ == "__main__":
    main()


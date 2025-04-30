#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script para buscar y convertir todos los archivos Markdown (.md) en una ruta específica.
Los archivos PDF generados se guardarán en los mismos directorios de origen.
"""

import os
import sys
import argparse
import logging
import subprocess
from pathlib import Path

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("convert-all-md")

def find_md_files(directory):
    """
    Busca todos los archivos .md en el directorio especificado y sus subdirectorios.
    
    Args:
        directory (str): Ruta al directorio donde buscar
        
    Returns:
        list: Lista de rutas a archivos .md encontrados
    """
    md_files = []
    
    try:
        # Usar pathlib para buscar archivos .md de manera recursiva
        for md_file in Path(directory).rglob('*.md'):
            md_files.append(str(md_file))
        
        logger.info(f"Se encontraron {len(md_files)} archivos .md en {directory}")
    except Exception as e:
        logger.error(f"Error al buscar archivos .md: {str(e)}")
    
    return md_files

def convert_files(md_files):
    """
    Convierte los archivos .md a PDF usando mdpdfusion-cli.py.
    
    Args:
        md_files (list): Lista de rutas a archivos .md
        
    Returns:
        tuple: (éxitos, fallos) - Número de conversiones exitosas y fallidas
    """
    success_count = 0
    failure_count = 0
    
    for md_file in md_files:
        try:
            # Obtener el directorio del archivo .md
            output_dir = os.path.dirname(md_file)
            
            # Construir el comando para convertir el archivo
            cmd = [sys.executable, "mdpdfusion-cli.py", "-v", md_file]
            
            logger.info(f"Convirtiendo {md_file}...")
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                success_count += 1
                logger.info(f"Conversión exitosa: {md_file}")
            else:
                failure_count += 1
                logger.error(f"Error al convertir {md_file}: {result.stderr}")
        except Exception as e:
            failure_count += 1
            logger.error(f"Excepción al convertir {md_file}: {str(e)}")
    
    return success_count, failure_count

def main():
    """Función principal."""
    parser = argparse.ArgumentParser(
        description='Busca y convierte todos los archivos .md en una ruta específica'
    )
    
    parser.add_argument(
        'directory',
        help='Directorio donde buscar archivos .md'
    )
    
    args = parser.parse_args()
    
    # Verificar que el directorio existe
    if not os.path.isdir(args.directory):
        logger.error(f"El directorio {args.directory} no existe")
        return 1
    
    # Buscar archivos .md
    md_files = find_md_files(args.directory)
    
    if not md_files:
        logger.warning(f"No se encontraron archivos .md en {args.directory}")
        return 0
    
    # Convertir archivos
    success_count, failure_count = convert_files(md_files)
    
    # Mostrar resumen
    logger.info(f"Resumen de conversión:")
    logger.info(f"  - Total de archivos: {len(md_files)}")
    logger.info(f"  - Conversiones exitosas: {success_count}")
    logger.info(f"  - Conversiones fallidas: {failure_count}")
    
    return 0 if failure_count == 0 else 1

if __name__ == "__main__":
    sys.exit(main())

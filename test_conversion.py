import os
import sys
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Importar la función de conversión desde mdpdfusion.py
from mdpdfusion import convert_md_to_pdf

def main():
    # Archivo de entrada (por defecto o desde argumentos)
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "test_markdown.md"

    # Carpeta de salida (carpeta temp)
    output_folder = "temp"

    # Asegurarse de que la carpeta de salida existe
    os.makedirs(output_folder, exist_ok=True)

    # Verificar que el archivo de entrada existe
    if not os.path.exists(input_file):
        logger.error(f"El archivo {input_file} no existe")
        return

    # Convertir el archivo
    logger.info(f"Convirtiendo {input_file} a PDF...")
    output_pdf = convert_md_to_pdf(input_file, output_folder)

    if output_pdf and os.path.exists(output_pdf):
        logger.info(f"Conversión exitosa. PDF generado: {output_pdf}")
    else:
        logger.error("La conversión falló")

if __name__ == "__main__":
    main()

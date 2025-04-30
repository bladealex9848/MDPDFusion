#!/bin/bash
# MDPDFusion - Convertidor de Markdown a PDF para macOS
# Este script permite arrastrar archivos .md sobre él para convertirlos a PDF

echo "MDPDFusion - Convertidor de Markdown a PDF"
echo "========================================"
echo

# Obtener el directorio del script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Verificar si se proporcionaron argumentos
if [ $# -eq 0 ]; then
    echo "Error: No se proporcionaron archivos."
    echo "Arrastra uno o más archivos .md sobre este script para convertirlos a PDF."
    echo
    read -p "Presiona Enter para salir..."
    exit 1
fi

# Activar el entorno virtual si existe
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
else
    echo "Advertencia: No se encontró el entorno virtual. Usando Python del sistema."
fi

# Procesar cada archivo proporcionado
for file in "$@"; do
    echo "Procesando: $file"
    python mdpdfusion_cli.py "$file"
    echo
done

echo "Proceso completado."
echo
read -p "Presiona Enter para salir..."

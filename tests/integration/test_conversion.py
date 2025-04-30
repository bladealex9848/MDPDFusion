"""
Pruebas de integración para la conversión de Markdown a PDF.
"""

import unittest
import os
import tempfile
import shutil
from src.mdpdfusion.core import convert_md_to_pdf

class TestConversion(unittest.TestCase):
    """Pruebas de integración para la conversión de Markdown a PDF."""
    
    def setUp(self):
        """Configuración inicial para las pruebas."""
        # Crear un directorio temporal para las pruebas
        self.temp_dir = tempfile.TemporaryDirectory()
        
        # Crear archivos de prueba
        self.create_test_files()
    
    def tearDown(self):
        """Limpieza después de las pruebas."""
        self.temp_dir.cleanup()
    
    def create_test_files(self):
        """Crea archivos Markdown de prueba."""
        # Archivo simple
        simple_md = os.path.join(self.temp_dir.name, "simple.md")
        with open(simple_md, "w", encoding="utf-8") as f:
            f.write("# Título simple\n\nEste es un párrafo simple.")
        
        # Archivo con formato
        format_md = os.path.join(self.temp_dir.name, "format.md")
        with open(format_md, "w", encoding="utf-8") as f:
            f.write("# Título con **formato**\n\n"
                   "Este es un párrafo con *cursiva* y **negrita**.\n\n"
                   "```python\nprint('Hola mundo')\n```\n\n"
                   "- Lista 1\n- Lista 2\n  - Sublista 1\n  - Sublista 2\n\n"
                   "1. Numerada 1\n2. Numerada 2\n\n"
                   "> Cita de texto\n\n"
                   "[Enlace](https://example.com)\n\n"
                   "---\n\n"
                   "## Subtítulo\n\n"
                   "Texto final.")
        
        # Archivo con tabla
        table_md = os.path.join(self.temp_dir.name, "table.md")
        with open(table_md, "w", encoding="utf-8") as f:
            f.write("# Documento con tabla\n\n"
                   "| Columna 1 | Columna 2 | Columna 3 |\n"
                   "|-----------|-----------|----------|\n"
                   "| Celda 1   | Celda 2   | Celda 3  |\n"
                   "| Celda 4   | Celda 5   | Celda 6  |\n\n"
                   "Texto después de la tabla.")
    
    def test_convert_simple_md(self):
        """Prueba la conversión de un archivo Markdown simple."""
        # Ruta al archivo de entrada
        input_file = os.path.join(self.temp_dir.name, "simple.md")
        
        # Convertir el archivo
        output_pdf = convert_md_to_pdf(input_file, self.temp_dir.name)
        
        # Verificar que se generó el PDF
        self.assertIsNotNone(output_pdf)
        self.assertTrue(os.path.exists(output_pdf))
        
        # Verificar el tamaño del archivo (debe ser mayor que 0)
        self.assertGreater(os.path.getsize(output_pdf), 0)
    
    def test_convert_format_md(self):
        """Prueba la conversión de un archivo Markdown con formato."""
        # Ruta al archivo de entrada
        input_file = os.path.join(self.temp_dir.name, "format.md")
        
        # Convertir el archivo
        output_pdf = convert_md_to_pdf(input_file, self.temp_dir.name)
        
        # Verificar que se generó el PDF
        self.assertIsNotNone(output_pdf)
        self.assertTrue(os.path.exists(output_pdf))
        
        # Verificar el tamaño del archivo (debe ser mayor que 0)
        self.assertGreater(os.path.getsize(output_pdf), 0)
    
    def test_convert_table_md(self):
        """Prueba la conversión de un archivo Markdown con tabla."""
        # Ruta al archivo de entrada
        input_file = os.path.join(self.temp_dir.name, "table.md")
        
        # Convertir el archivo
        output_pdf = convert_md_to_pdf(input_file, self.temp_dir.name)
        
        # Verificar que se generó el PDF
        self.assertIsNotNone(output_pdf)
        self.assertTrue(os.path.exists(output_pdf))
        
        # Verificar el tamaño del archivo (debe ser mayor que 0)
        self.assertGreater(os.path.getsize(output_pdf), 0)
    
    def test_convert_nonexistent_file(self):
        """Prueba la conversión de un archivo que no existe."""
        # Ruta a un archivo que no existe
        input_file = os.path.join(self.temp_dir.name, "nonexistent.md")
        
        # Intentar convertir el archivo
        output_pdf = convert_md_to_pdf(input_file, self.temp_dir.name)
        
        # Verificar que no se generó ningún PDF
        self.assertIsNone(output_pdf)
    
    def test_convert_to_nonexistent_directory(self):
        """Prueba la conversión a un directorio que no existe."""
        # Ruta al archivo de entrada
        input_file = os.path.join(self.temp_dir.name, "simple.md")
        
        # Ruta a un directorio que no existe
        output_dir = os.path.join(self.temp_dir.name, "nonexistent_dir")
        
        # Intentar convertir el archivo
        output_pdf = convert_md_to_pdf(input_file, output_dir)
        
        # Verificar que no se generó ningún PDF
        self.assertIsNone(output_pdf)

if __name__ == "__main__":
    unittest.main()

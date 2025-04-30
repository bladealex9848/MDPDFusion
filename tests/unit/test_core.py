"""
Pruebas unitarias para el módulo core.
"""

import unittest
import os
import tempfile
from unittest.mock import patch, MagicMock
from src.mdpdfusion.core import convert_md_to_pdf

class TestCore(unittest.TestCase):
    """Pruebas para las funciones del módulo core."""
    
    def setUp(self):
        """Configuración inicial para las pruebas."""
        # Crear un archivo Markdown temporal para las pruebas
        self.temp_dir = tempfile.TemporaryDirectory()
        self.md_content = "# Título de prueba\n\nEste es un párrafo de prueba."
        self.md_file = os.path.join(self.temp_dir.name, "test.md")
        with open(self.md_file, "w", encoding="utf-8") as f:
            f.write(self.md_content)
    
    def tearDown(self):
        """Limpieza después de las pruebas."""
        self.temp_dir.cleanup()
    
    @patch("src.mdpdfusion.core.convert_with_pypandoc")
    @patch("src.mdpdfusion.core.convert_with_reportlab")
    def test_convert_md_to_pdf_pypandoc_success(self, mock_reportlab, mock_pypandoc):
        """Prueba la conversión exitosa con pypandoc."""
        # Configurar el mock para que pypandoc tenga éxito
        mock_pypandoc.return_value = True
        
        # Llamar a la función
        result = convert_md_to_pdf(self.md_file, self.temp_dir.name)
        
        # Verificar que se llamó a pypandoc pero no a reportlab
        mock_pypandoc.assert_called_once()
        mock_reportlab.assert_not_called()
        
        # Verificar que el resultado es la ruta al archivo PDF
        expected_pdf = os.path.join(self.temp_dir.name, "test.pdf")
        self.assertEqual(result, expected_pdf)
    
    @patch("src.mdpdfusion.core.convert_with_pypandoc")
    @patch("src.mdpdfusion.core.convert_with_reportlab")
    def test_convert_md_to_pdf_reportlab_fallback(self, mock_reportlab, mock_pypandoc):
        """Prueba el fallback a reportlab cuando pypandoc falla."""
        # Configurar los mocks
        mock_pypandoc.return_value = False
        mock_reportlab.return_value = True
        
        # Llamar a la función
        result = convert_md_to_pdf(self.md_file, self.temp_dir.name)
        
        # Verificar que se llamó a ambos conversores
        mock_pypandoc.assert_called_once()
        mock_reportlab.assert_called_once()
        
        # Verificar que el resultado es la ruta al archivo PDF
        expected_pdf = os.path.join(self.temp_dir.name, "test.pdf")
        self.assertEqual(result, expected_pdf)
    
    @patch("src.mdpdfusion.core.convert_with_pypandoc")
    @patch("src.mdpdfusion.core.convert_with_reportlab")
    def test_convert_md_to_pdf_both_fail(self, mock_reportlab, mock_pypandoc):
        """Prueba el caso en que ambos conversores fallan."""
        # Configurar los mocks
        mock_pypandoc.return_value = False
        mock_reportlab.return_value = False
        
        # Llamar a la función
        result = convert_md_to_pdf(self.md_file, self.temp_dir.name)
        
        # Verificar que se llamó a ambos conversores
        mock_pypandoc.assert_called_once()
        mock_reportlab.assert_called_once()
        
        # Verificar que el resultado es None
        self.assertIsNone(result)
    
    @patch("src.mdpdfusion.core.convert_with_pypandoc")
    def test_convert_md_to_pdf_file_not_found(self, mock_pypandoc):
        """Prueba el caso en que el archivo no existe."""
        # Llamar a la función con un archivo que no existe
        result = convert_md_to_pdf("archivo_inexistente.md", self.temp_dir.name)
        
        # Verificar que no se llamó a ningún conversor
        mock_pypandoc.assert_not_called()
        
        # Verificar que el resultado es None
        self.assertIsNone(result)
    
    @patch("src.mdpdfusion.core.convert_with_pypandoc")
    @patch("src.mdpdfusion.core.convert_with_reportlab")
    def test_convert_md_to_pdf_reportlab_error(self, mock_reportlab, mock_pypandoc):
        """Prueba el manejo de errores en reportlab."""
        # Configurar los mocks
        mock_pypandoc.return_value = False
        mock_reportlab.side_effect = ValueError("Error de prueba")
        
        # Llamar a la función
        result = convert_md_to_pdf(self.md_file, self.temp_dir.name)
        
        # Verificar que se llamó a ambos conversores
        mock_pypandoc.assert_called_once()
        mock_reportlab.assert_called_once()
        
        # Verificar que el resultado es None
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()

"""
Pruebas unitarias para el módulo formatters.
"""

import unittest
from src.mdpdfusion.formatters import process_inline_formatting, create_anchor_id

class TestFormatters(unittest.TestCase):
    """Pruebas para las funciones de formateo."""
    
    def test_process_inline_formatting_bold(self):
        """Prueba el formateo de texto en negrita."""
        # Prueba con asteriscos
        self.assertEqual(
            process_inline_formatting("Texto en **negrita**"),
            "Texto en <b>negrita</b>"
        )
        # Prueba con guiones bajos
        self.assertEqual(
            process_inline_formatting("Texto en __negrita__"),
            "Texto en <b>negrita</b>"
        )
    
    def test_process_inline_formatting_italic(self):
        """Prueba el formateo de texto en cursiva."""
        # Prueba con asteriscos
        self.assertEqual(
            process_inline_formatting("Texto en *cursiva*"),
            "Texto en <i>cursiva</i>"
        )
        # Prueba con guiones bajos
        self.assertEqual(
            process_inline_formatting("Texto en _cursiva_"),
            "Texto en <i>cursiva</i>"
        )
    
    def test_process_inline_formatting_bold_italic(self):
        """Prueba el formateo de texto en negrita y cursiva."""
        # Prueba con asteriscos
        self.assertEqual(
            process_inline_formatting("Texto en ***negrita y cursiva***"),
            "Texto en <b><i>negrita y cursiva</i></b>"
        )
        # Prueba con guiones bajos
        self.assertEqual(
            process_inline_formatting("Texto en ___negrita y cursiva___"),
            "Texto en <b><i>negrita y cursiva</i></b>"
        )
    
    def test_process_inline_formatting_code(self):
        """Prueba el formateo de código en línea."""
        self.assertEqual(
            process_inline_formatting("Código en línea: `print('Hola')`"),
            "Código en línea: <font face=\"Courier\">print('Hola')</font>"
        )
    
    def test_process_inline_formatting_link(self):
        """Prueba el formateo de enlaces."""
        # Enlace externo
        self.assertEqual(
            process_inline_formatting("[Enlace](https://example.com)"),
            "<link href=\"https://example.com\">Enlace</link>"
        )
        # Enlace interno
        result = process_inline_formatting("[Sección](#seccion)")
        self.assertTrue("<link href=\"#seccion\">Sección</link>" in result)
    
    def test_process_inline_formatting_strikethrough(self):
        """Prueba el formateo de texto tachado."""
        self.assertEqual(
            process_inline_formatting("Texto ~~tachado~~"),
            "Texto <strike>tachado</strike>"
        )
    
    def test_process_inline_formatting_escape(self):
        """Prueba el escape de caracteres especiales."""
        self.assertEqual(
            process_inline_formatting("Texto con \\*asteriscos\\* escapados"),
            "Texto con *asteriscos* escapados"
        )
    
    def test_create_anchor_id(self):
        """Prueba la creación de IDs de ancla."""
        # Texto simple
        self.assertEqual(create_anchor_id("Sección 1"), "sección-1")
        
        # Texto con caracteres especiales
        self.assertEqual(create_anchor_id("Sección: Título & Subtítulo"), "sección-título-subtítulo")
        
        # Texto con formato
        self.assertEqual(create_anchor_id("**Sección** en *negrita*"), "sección-en-negrita")
        
        # Texto con espacios múltiples
        self.assertEqual(create_anchor_id("Sección   con   espacios"), "sección-con-espacios")
        
        # Texto con guiones
        self.assertEqual(create_anchor_id("Sección - con - guiones"), "sección-con-guiones")
        
        # Texto con guiones al inicio y final
        self.assertEqual(create_anchor_id("-Sección con guiones-"), "sección-con-guiones")

if __name__ == "__main__":
    unittest.main()

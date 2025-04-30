#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script de entrada para la interfaz de línea de comandos de MDPDFusion.
"""

import sys
import logging
from src.mdpdfusion.cli import main

if __name__ == "__main__":
    # Configurar logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    try:
        main()
    except Exception as e:
        logging.critical(f"Error crítico: {str(e)}")
        sys.exit(1)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script de entrada para la interfaz gráfica de MDPDFusion.
"""

import sys
import logging

if __name__ == "__main__":
    # Configurar logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    try:
        from src.mdpdfusion.gui import main
        main()
    except ImportError as e:
        print(f"Error: No se pudo importar la interfaz gráfica. {str(e)}")
        print("Asegúrate de tener instalado PyQt5.")
        sys.exit(1)
    except Exception as e:
        logging.critical(f"Error crítico: {str(e)}")
        sys.exit(1)

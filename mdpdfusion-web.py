#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script de entrada para la interfaz web de MDPDFusion.
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
        import streamlit
        from src.mdpdfusion.web import main
        
        # Streamlit requiere que se ejecute como un script separado
        import os
        import subprocess
        script_path = os.path.abspath(__file__)
        dir_path = os.path.dirname(script_path)
        web_script = os.path.join(dir_path, "src", "mdpdfusion", "web.py")
        
        print("Iniciando interfaz web con Streamlit...")
        print("Abre tu navegador en http://localhost:8501")
        
        subprocess.run([sys.executable, "-m", "streamlit", "run", web_script])
    except ImportError as e:
        print(f"Error: No se pudo importar la interfaz web. {str(e)}")
        print("Asegúrate de tener instalado Streamlit.")
        sys.exit(1)
    except Exception as e:
        logging.critical(f"Error crítico: {str(e)}")
        sys.exit(1)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script para generar el ejecutable de MDPDFusion usando PyInstaller.
"""

import os
import sys
import subprocess
import shutil
import platform

def main():
    """Función principal para generar el ejecutable."""
    print("Generando ejecutable de MDPDFusion...")
    
    # Determinar el sistema operativo
    system = platform.system()
    
    # Crear directorio de salida si no existe
    if not os.path.exists("dist"):
        os.makedirs("dist")
    
    # Limpiar directorio de salida
    for item in os.listdir("dist"):
        item_path = os.path.join("dist", item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
        else:
            os.remove(item_path)
    
    # Instalar PyInstaller si no está instalado
    try:
        import PyInstaller
    except ImportError:
        print("Instalando PyInstaller...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    # Configurar opciones de PyInstaller
    icon_option = []
    if system == "Windows":
        if os.path.exists("assets/icon.ico"):
            icon_option = ["--icon=assets/icon.ico"]
        else:
            print("Advertencia: No se encontró el archivo de icono (assets/icon.ico)")
    elif system == "Darwin":  # macOS
        if os.path.exists("assets/icon.icns"):
            icon_option = ["--icon=assets/icon.icns"]
        else:
            print("Advertencia: No se encontró el archivo de icono (assets/icon.icns)")
    
    # Generar el ejecutable
    cmd = [
        "pyinstaller",
        "--name=MDPDFusion",
        "--onefile",
        "--windowed",
        *icon_option,
        "--add-data=assets/*;assets/",
        "--hidden-import=PIL._tkinter_finder",
        "mdpdfusion-gui.py"
    ]
    
    # Ajustar el separador de ruta según el sistema operativo
    if system != "Windows":
        cmd[5] = cmd[5].replace(";", ":")
    
    print(f"Ejecutando comando: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    
    if result.returncode == 0:
        print("Ejecutable generado correctamente.")
        
        # Copiar archivos adicionales
        if system == "Windows":
            # Crear archivo batch para arrastrar y soltar
            with open("dist/Arrastrar_MD_Aqui.bat", "w") as f:
                f.write('@echo off\n')
                f.write('echo Convirtiendo archivos Markdown a PDF...\n')
                f.write('MDPDFusion.exe %*\n')
                f.write('pause\n')
            
            print("Archivo batch para arrastrar y soltar creado.")
        
        print(f"Ejecutable disponible en: {os.path.abspath('dist/MDPDFusion.exe' if system == 'Windows' else 'dist/MDPDFusion')}")
    else:
        print("Error al generar el ejecutable.")
        sys.exit(1)

if __name__ == "__main__":
    main()

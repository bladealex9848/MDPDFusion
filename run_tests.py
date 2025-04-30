#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script para ejecutar pruebas y generar informes.
"""

import os
import sys
import subprocess
import argparse
import datetime

def main():
    """Función principal para ejecutar pruebas y generar informes."""
    parser = argparse.ArgumentParser(description="Ejecutar pruebas y generar informes")
    parser.add_argument("--unit", action="store_true", help="Ejecutar solo pruebas unitarias")
    parser.add_argument("--integration", action="store_true", help="Ejecutar solo pruebas de integración")
    parser.add_argument("--coverage", action="store_true", help="Generar informe de cobertura")
    parser.add_argument("--html", action="store_true", help="Generar informe HTML")
    args = parser.parse_args()
    
    # Crear directorio para informes si no existe
    reports_dir = "reports"
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
    
    # Fecha y hora actual para el nombre del informe
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Determinar qué pruebas ejecutar
    if not args.unit and not args.integration:
        # Si no se especifica, ejecutar todas las pruebas
        test_paths = ["tests/unit", "tests/integration"]
    else:
        test_paths = []
        if args.unit:
            test_paths.append("tests/unit")
        if args.integration:
            test_paths.append("tests/integration")
    
    # Comando base para pytest
    cmd = [sys.executable, "-m", "pytest"]
    
    # Añadir opciones según los argumentos
    if args.coverage:
        cmd.extend(["--cov=src/mdpdfusion", "--cov-report=term"])
        if args.html:
            cmd.append(f"--cov-report=html:reports/coverage_{timestamp}")
    
    if args.html:
        cmd.extend(["--html", f"reports/report_{timestamp}.html", "--self-contained-html"])
    
    # Añadir rutas de prueba
    cmd.extend(test_paths)
    
    # Ejecutar pruebas
    print(f"Ejecutando comando: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    
    if result.returncode == 0:
        print("Todas las pruebas pasaron correctamente.")
        if args.coverage and args.html:
            print(f"Informe de cobertura generado en: reports/coverage_{timestamp}")
        if args.html:
            print(f"Informe HTML generado en: reports/report_{timestamp}.html")
    else:
        print("Algunas pruebas fallaron.")
        sys.exit(1)

if __name__ == "__main__":
    main()

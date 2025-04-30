@echo off
REM Script para convertir todos los archivos Markdown en un directorio
REM Uso: ConvertirDirectorio.bat [directorio]

echo MDPDFusion - Convertidor de Markdown a PDF
echo ========================================
echo.

REM Verificar si se proporcionó un directorio
if "%~1"=="" (
    REM Si no se proporcionó un directorio, usar el directorio actual
    set "DIRECTORY=%CD%"
) else (
    REM Usar el directorio proporcionado
    set "DIRECTORY=%~1"
)

echo Convirtiendo todos los archivos Markdown en: %DIRECTORY%
echo.

REM Ejecutar el script Python
python convert_all_md.py "%DIRECTORY%"

echo.
echo Proceso completado.
echo.
pause

@echo off
REM MDPDFusion - Convertidor de Markdown a PDF
REM Este script permite arrastrar archivos .md sobre él para convertirlos a PDF

echo MDPDFusion - Convertidor de Markdown a PDF
echo ========================================
echo.

REM Verificar si se proporcionaron argumentos
if "%~1"=="" (
    echo Error: No se proporcionaron archivos.
    echo Arrastra uno o más archivos .md sobre este script para convertirlos a PDF.
    echo.
    pause
    exit /b 1
)

REM Activar el entorno virtual si existe
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
) else (
    echo Advertencia: No se encontró el entorno virtual. Usando Python del sistema.
)

REM Procesar cada archivo proporcionado
:process_files
if "%~1"=="" goto end

echo Procesando: %~1
python mdpdfusion_cli.py "%~1"
echo.

shift
goto process_files

:end
echo Proceso completado.
echo.
pause

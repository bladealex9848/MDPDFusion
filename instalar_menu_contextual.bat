@echo off
REM Script para instalar la opción "Convertir a PDF" en el menú contextual de Windows
REM Debe ejecutarse como administrador

echo Instalando MDPDFusion en el menú contextual de Windows...
echo ======================================================
echo.

REM Obtener la ruta completa del directorio actual
set CURRENT_DIR=%~dp0
set CURRENT_DIR=%CURRENT_DIR:~0,-1%

REM Escapar las barras invertidas para el registro
set "REG_PATH=%CURRENT_DIR:\=\\%"

REM Crear la entrada en el registro para archivos .md
reg add "HKEY_CLASSES_ROOT\.md\shell\ConvertirAPDF" /ve /t REG_SZ /d "Convertir a PDF con MDPDFusion" /f
reg add "HKEY_CLASSES_ROOT\.md\shell\ConvertirAPDF" /v Icon /t REG_SZ /d "%REG_PATH%\\icon.ico" /f
reg add "HKEY_CLASSES_ROOT\.md\shell\ConvertirAPDF\command" /ve /t REG_SZ /d "cmd.exe /c cd /d \"%REG_PATH%\" && MDPDFusion.bat \"%%1\"" /f

echo.
if %errorlevel% equ 0 (
    echo Instalación completada con éxito.
    echo Ahora puedes hacer clic derecho en cualquier archivo .md y seleccionar "Convertir a PDF con MDPDFusion".
) else (
    echo Error durante la instalación. Asegúrate de ejecutar este script como administrador.
)

echo.
pause

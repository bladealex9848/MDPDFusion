@echo off
REM Script para desinstalar la opción "Convertir a PDF" del menú contextual de Windows
REM Debe ejecutarse como administrador

echo Desinstalando MDPDFusion del menú contextual de Windows...
echo ======================================================
echo.

REM Eliminar la entrada del registro
reg delete "HKEY_CLASSES_ROOT\.md\shell\ConvertirAPDF" /f

echo.
if %errorlevel% equ 0 (
    echo Desinstalación completada con éxito.
) else (
    echo Error durante la desinstalación. Asegúrate de ejecutar este script como administrador.
)

echo.
pause

# Guía de Integración con el Sistema Operativo

Esta guía proporciona instrucciones detalladas sobre cómo integrar MDPDFusion con tu sistema operativo para una experiencia de usuario más fluida.

## Índice

- [Windows](#windows)
  - [Arrastrar y Soltar](#arrastrar-y-soltar-windows)
  - [Menú Contextual](#menú-contextual-windows)
  - [Solución de Problemas](#solución-de-problemas-windows)
- [macOS](#macos)
  - [Arrastrar y Soltar](#arrastrar-y-soltar-macos)
  - [Servicios del Sistema](#servicios-del-sistema-macos)
  - [Solución de Problemas](#solución-de-problemas-macos)

## Windows

### Arrastrar y Soltar (Windows)

El archivo `MDPDFusion.bat` permite convertir archivos Markdown a PDF simplemente arrastrándolos sobre él.

#### Configuración

1. Asegúrate de que has instalado todas las dependencias siguiendo las instrucciones en el README.md.
2. Verifica que el archivo `MDPDFusion.bat` esté en el directorio raíz del proyecto.

#### Uso

1. Selecciona uno o más archivos .md en el Explorador de Windows.
2. Arrastra los archivos seleccionados sobre el archivo `MDPDFusion.bat`.
3. Se abrirá una ventana de terminal que mostrará el progreso de la conversión.
4. Los archivos PDF generados se guardarán en el mismo directorio que los archivos .md originales.

### Menú Contextual (Windows)

Puedes añadir una opción "Convertir a PDF con MDPDFusion" al menú contextual del Explorador de Windows para archivos .md.

#### Instalación

1. Haz clic derecho en el archivo `instalar_menu_contextual.bat`.
2. Selecciona "Ejecutar como administrador".
3. Confirma cualquier diálogo de seguridad que aparezca.
4. Espera a que aparezca el mensaje de confirmación.

#### Uso

1. Haz clic derecho en cualquier archivo .md en el Explorador de Windows.
2. Selecciona "Convertir a PDF con MDPDFusion" en el menú contextual.
3. El archivo PDF generado se guardará en el mismo directorio que el archivo .md original.

#### Desinstalación

1. Haz clic derecho en el archivo `desinstalar_menu_contextual.bat`.
2. Selecciona "Ejecutar como administrador".
3. Confirma cualquier diálogo de seguridad que aparezca.
4. Espera a que aparezca el mensaje de confirmación.

### Solución de Problemas (Windows)

#### El menú contextual no aparece

- Asegúrate de haber ejecutado `instalar_menu_contextual.bat` como administrador.
- Verifica que la instalación haya terminado correctamente sin errores.
- Intenta reiniciar el Explorador de Windows o tu computadora.

#### Error al convertir archivos

- Verifica que el entorno virtual esté configurado correctamente.
- Asegúrate de que todas las dependencias estén instaladas.
- Comprueba que los archivos .md sean válidos y no contengan errores de sintaxis.

## macOS

### Arrastrar y Soltar (macOS)

El archivo `mdpdfusion_mac.command` permite convertir archivos Markdown a PDF simplemente arrastrándolos sobre él.

#### Configuración

1. Asegúrate de que has instalado todas las dependencias siguiendo las instrucciones en el README.md.
2. Haz el archivo ejecutable:
   ```bash
   chmod +x mdpdfusion_mac.command
   ```

#### Uso

1. Selecciona uno o más archivos .md en el Finder.
2. Arrastra los archivos seleccionados sobre el archivo `mdpdfusion_mac.command`.
3. Se abrirá una ventana de terminal que mostrará el progreso de la conversión.
4. Los archivos PDF generados se guardarán en el mismo directorio que los archivos .md originales.

### Servicios del Sistema (macOS)

Puedes añadir una opción "Convertir a PDF con MDPDFusion" al menú de Servicios de macOS para archivos .md.

#### Instalación

1. Haz clic derecho en el archivo `instalar_servicio_mac.command`.
2. Selecciona "Abrir".
3. Si aparece una advertencia de seguridad, haz clic en "Abrir" de nuevo.
4. Espera a que aparezca el mensaje de confirmación.

#### Uso

1. Haz clic derecho en cualquier archivo .md en el Finder.
2. Ve al submenú "Servicios".
3. Selecciona "Convertir a PDF con MDPDFusion".
4. El archivo PDF generado se guardará en el mismo directorio que el archivo .md original.

### Solución de Problemas (macOS)

#### El servicio no aparece en el menú

- Asegúrate de haber ejecutado `instalar_servicio_mac.command` correctamente.
- Verifica que la instalación haya terminado sin errores.
- Intenta reiniciar el Finder o tu computadora.
- Comprueba la configuración de Servicios en Preferencias del Sistema > Teclado > Atajos > Servicios.

#### Error "No se puede abrir"

Si recibes un error de que el archivo no se puede abrir porque proviene de un desarrollador no identificado:

1. Abre Preferencias del Sistema > Seguridad y Privacidad.
2. En la pestaña "General", haz clic en "Abrir de todos modos" junto al mensaje sobre el archivo bloqueado.
3. Intenta abrir el archivo nuevamente.

#### Error al convertir archivos

- Verifica que el entorno virtual esté configurado correctamente.
- Asegúrate de que todas las dependencias estén instaladas.
- Comprueba que los archivos .md sean válidos y no contengan errores de sintaxis.
- Verifica los permisos de los archivos y directorios.

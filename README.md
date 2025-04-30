# MDPDFusion

<p align="center">
  <img src="assets/logo.png" alt="MDPDFusion Logo">
</p>

MDPDFusion es una herramienta versátil que permite a los usuarios convertir archivos Markdown (.md) a PDF de manera sencilla y eficiente, ya sea a través de una interfaz web, línea de comandos o integración con el sistema operativo.

## Características

- **Múltiples formas de uso**:
  - Interfaz web intuitiva construida con Streamlit
  - Herramienta de línea de comandos (CLI)
  - Integración con el menú contextual del sistema operativo (Windows y macOS)
  - Arrastrar y soltar archivos para conversión rápida
- **Conversión de alta calidad**:
  - Preservación fiel del formato Markdown (negritas, cursivas, listas, etc.)
  - Soporte para tablas con formato visual adecuado
  - Bloques de código con resaltado de sintaxis
  - Imágenes con ajuste automático de tamaño
  - Enlaces internos funcionales entre secciones del documento
- **Flexibilidad**:
  - Soporte para la carga de múltiples archivos .md
  - Conversión rápida y eficiente
  - Opciones de personalización de salida

## Requisitos

- Python 3.10+
- Streamlit
- Markdown
- PyPandoc
- ReportLab

## Configuración del entorno virtual

### Windows

1. Abre una terminal (CMD o PowerShell)
2. Navega hasta la carpeta del proyecto:
   ```
   cd ruta\a\MDPDFusion
   ```
3. Crea un entorno virtual:
   ```
   python -m venv venv
   ```
4. Activa el entorno virtual:
   ```
   venv\Scripts\activate
   ```
5. Actualiza pip e instala las dependencias:
   ```
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

### macOS / Linux

1. Abre una terminal
2. Navega hasta la carpeta del proyecto:
   ```
   cd ruta/a/MDPDFusion
   ```
3. Crea un entorno virtual:
   ```
   python3 -m venv venv
   ```
4. Activa el entorno virtual:
   ```
   source venv/bin/activate
   ```
5. Actualiza pip e instala las dependencias:
   ```
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/bladealex9848/MDPDFusion.git
   cd MDPDFusion
   ```

2. Sigue los pasos de configuración del entorno virtual según tu sistema operativo.

## Uso

### Interfaz Web (Streamlit)

1. Asegúrate de que el entorno virtual esté activado.

2. Ejecuta la aplicación:
   ```
   streamlit run mdpdfusion.py
   ```

3. Abre tu navegador y ve a `http://localhost:8501`

4. Sube tus archivos .md usando el botón de carga de archivos

5. Haz clic en los botones de descarga para obtener tus archivos PDF convertidos

### Línea de Comandos (CLI)

El CLI permite convertir archivos Markdown desde la terminal:

```bash
# Convertir un archivo
python mdpdfusion_cli.py archivo.md

# Convertir múltiples archivos
python mdpdfusion_cli.py archivo1.md archivo2.md

# Especificar directorio de salida
python mdpdfusion_cli.py -o directorio_salida archivo.md

# Mostrar información detallada
python mdpdfusion_cli.py -v archivo.md
```

### Arrastrar y Soltar (Windows)

1. Simplemente arrastra uno o más archivos .md sobre el archivo `MDPDFusion.bat`
2. Los archivos PDF se generarán en el mismo directorio que los archivos .md originales

### Integración con el Menú Contextual

#### Windows

1. Ejecuta `instalar_menu_contextual.bat` como administrador (clic derecho > Ejecutar como administrador)
2. Ahora puedes hacer clic derecho en cualquier archivo .md y seleccionar "Convertir a PDF con MDPDFusion"
3. Para desinstalar, ejecuta `desinstalar_menu_contextual.bat` como administrador

#### macOS

1. Ejecuta `instalar_servicio_mac.command` (clic derecho > Abrir)
2. Ahora puedes hacer clic derecho en cualquier archivo .md, ir a Servicios y seleccionar "Convertir a PDF con MDPDFusion"

## Características Avanzadas

### Enlaces Internos

MDPDFusion soporta enlaces internos entre secciones del documento:

```markdown
## Mi Sección

Contenido...

[Enlace a la sección](#mi-sección)
```

Los enlaces internos se convierten automáticamente en enlaces funcionales en el PDF generado.

### Manejo de Errores

Si encuentras problemas con enlaces internos, MDPDFusion intentará recuperarse automáticamente:

1. Verifica que los enlaces internos apunten a secciones que existen en el documento
2. Asegúrate de que los IDs de ancla sean válidos (solo letras minúsculas, números, guiones y guiones bajos)
3. Revisa los mensajes de error para identificar enlaces problemáticos

### Personalización

Para obtener información detallada sobre la integración con el sistema operativo, consulta el archivo [INTEGRACION.md](INTEGRACION.md).

## Contribuir

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores antes de enviar un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.

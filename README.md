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

### Método 1: Ejecutable (Windows)

1. Descarga el archivo ejecutable desde la sección de [Releases](https://github.com/bladealex9848/MDPDFusion/releases)
2. Ejecuta el archivo `MDPDFusion.exe`
3. ¡Listo! Puedes arrastrar archivos .md sobre la aplicación o usar el botón "Añadir archivos"

### Método 2: Desde el código fuente

1. Clona este repositorio:
   ```
   git clone https://github.com/bladealex9848/MDPDFusion.git
   cd MDPDFusion
   ```

2. Sigue los pasos de configuración del entorno virtual según tu sistema operativo.

3. Instala el paquete en modo desarrollo:
   ```
   pip install -e .
   ```

## Uso

### Aplicación Gráfica (GUI)

1. Si instalaste el ejecutable, simplemente ábrelo haciendo doble clic en `MDPDFusion.exe`
2. Si instalaste desde el código fuente, ejecuta:
   ```
   python mdpdfusion-gui.py
   ```
3. Usa el botón "Añadir archivos" o arrastra archivos .md sobre la ventana
4. Selecciona el directorio de salida y haz clic en "Convertir a PDF"

### Interfaz Web (Streamlit)

1. Asegúrate de que el entorno virtual esté activado.

2. Ejecuta la aplicación:
   ```
   python mdpdfusion-web.py
   ```
   o
   ```
   streamlit run src/mdpdfusion/web.py
   ```

3. Abre tu navegador y ve a `http://localhost:8501`

4. Sube tus archivos .md usando el botón de carga de archivos

5. Haz clic en los botones de descarga para obtener tus archivos PDF convertidos

### Línea de Comandos (CLI)

El CLI permite convertir archivos Markdown desde la terminal:

```bash
# Convertir un archivo
python mdpdfusion-cli.py archivo.md

# Convertir múltiples archivos
python mdpdfusion-cli.py archivo1.md archivo2.md

# Especificar directorio de salida
python mdpdfusion-cli.py -o directorio_salida archivo.md

# Mostrar información detallada
python mdpdfusion-cli.py -v archivo.md
```

### Arrastrar y Soltar (Windows)

1. Si usas el ejecutable, simplemente arrastra uno o más archivos .md sobre `MDPDFusion.exe` o sobre `Arrastrar_MD_Aqui.bat` en la carpeta de instalación
2. Si usas la versión de código fuente, arrastra los archivos sobre `MDPDFusion.bat`
3. Los archivos PDF se generarán en el mismo directorio que los archivos .md originales

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

## Estructura del Proyecto

```
MDPDFusion/
├── assets/                  # Recursos gráficos (logo, iconos)
├── build/                   # Archivos generados durante la compilación
├── dist/                    # Ejecutables y distribuciones
├── docs/                    # Documentación
│   ├── images/              # Imágenes para la documentación
│   └── examples/            # Ejemplos de uso
├── reports/                 # Informes de pruebas y cobertura
├── src/                     # Código fuente
│   └── mdpdfusion/          # Paquete principal
│       ├── __init__.py      # Inicialización del paquete
│       ├── core.py          # Funcionalidad principal
│       ├── formatters.py    # Procesamiento de formato Markdown
│       ├── converters.py    # Conversores (ReportLab, Pandoc)
│       ├── cli.py           # Interfaz de línea de comandos
│       ├── gui.py           # Interfaz gráfica (PyQt5)
│       └── web.py           # Interfaz web (Streamlit)
├── tests/                   # Pruebas
│   ├── unit/                # Pruebas unitarias
│   ├── integration/         # Pruebas de integración
│   └── fixtures/            # Archivos de prueba
├── .gitignore               # Archivos ignorados por Git
├── CHANGELOG.md             # Registro de cambios
├── INTEGRACION.md           # Guía de integración con el sistema
├── LICENSE                  # Licencia del proyecto
├── README.md                # Este archivo
├── build_exe.py             # Script para generar ejecutable
├── mdpdfusion-cli.py        # Punto de entrada para CLI
├── mdpdfusion-gui.py        # Punto de entrada para GUI
├── mdpdfusion-web.py        # Punto de entrada para web
├── requirements.txt         # Dependencias del proyecto
├── run_tests.py             # Script para ejecutar pruebas
└── setup.py                 # Configuración de instalación
```

## Pruebas

MDPDFusion incluye un conjunto completo de pruebas unitarias y de integración:

### Ejecutar pruebas

```bash
# Ejecutar todas las pruebas
python run_tests.py

# Ejecutar solo pruebas unitarias
python run_tests.py --unit

# Ejecutar solo pruebas de integración
python run_tests.py --integration

# Generar informe de cobertura
python run_tests.py --coverage

# Generar informe HTML
python run_tests.py --html
```

### Generar ejecutable

Para generar un ejecutable (.exe en Windows):

```bash
python build_exe.py
```

El ejecutable se generará en la carpeta `dist/`.

## Contribuir

Las contribuciones son bienvenidas. Por favor, sigue estos pasos:

1. Haz un fork del repositorio
2. Crea una rama para tu característica (`git checkout -b feature/amazing-feature`)
3. Haz commit de tus cambios (`git commit -m 'Add some amazing feature'`)
4. Ejecuta las pruebas para asegurarte de que todo funciona
5. Haz push a la rama (`git push origin feature/amazing-feature`)
6. Abre un Pull Request

## Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.

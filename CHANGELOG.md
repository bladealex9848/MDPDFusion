# Registro de cambios (Changelog)

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.1] - 2023-04-30

### Corregido
- Interpretación correcta de etiquetas de formato Markdown (negritas, cursivas, etc.)
- Visualización adecuada de tablas en el PDF generado
- Integración del lenguaje de programación dentro de los bloques de código
- Procesamiento de formato en línea dentro de encabezados y otros elementos

### Mejorado
- Expresiones regulares más precisas para detectar formato en línea
- Manejo de casos especiales como asteriscos en medio de palabras
- Soporte para formato adicional como tachado y eliminación de escapes
- Mejor detección y procesamiento de tablas con separadores
- Logging detallado para facilitar la depuración

## [0.2.0] - 2023-04-30

### Agregado
- Soporte mejorado para tablas en Markdown con formato visual adecuado
- Soporte para imágenes con ajuste automático de tamaño y leyendas
- Manejo de listas anidadas con diferentes niveles de indentación
- Estilos visuales distintivos para bloques de código y citas
- Documentación detallada de las dependencias en requirements.txt
- Soporte para conversión de múltiples archivos Markdown a PDF
- Interfaz de usuario con Streamlit
- Documentación inicial

### Mejorado
- Conversión fiel de todos los elementos de formato Markdown a PDF
- Aspecto visual de los PDFs generados con mejor formato y estilos
- Manejo de errores durante la carga de imágenes y procesamiento de tablas
- Detección robusta de tablas con mejor análisis de separadores
- Visualización de bloques de código con el lenguaje integrado en el bloque

## [0.1.0] - 2023-04-30

### Agregado
- Configuración inicial del proyecto
- Implementación de la funcionalidad básica de conversión de Markdown a PDF
- Soporte para PyPandoc como motor principal de conversión
- Fallback a ReportLab cuando PyPandoc no está disponible
- Estructura básica de la aplicación Streamlit
- Documentación en README.md
- Configuración de entorno virtual para Windows y macOS
- Archivo CHANGELOG.md para seguimiento de cambios

### Cambiado
- Actualización del README.md con instrucciones detalladas para configurar entornos virtuales
- Inclusión del logo en el README.md

### Corregido
- Manejo de errores durante la conversión de archivos

[Unreleased]: https://github.com/bladealex9848/MDPDFusion/compare/v0.2.1...HEAD
[0.2.1]: https://github.com/bladealex9848/MDPDFusion/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/bladealex9848/MDPDFusion/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/bladealex9848/MDPDFusion/releases/tag/v0.1.0

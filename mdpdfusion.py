import streamlit as st
import markdown
import os
import tempfile
import logging
import sys
import traceback
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def convert_with_pypandoc(md_content, output_pdf):
    try:
        import pypandoc
        pypandoc.convert_text(md_content, 'pdf', format='md', outputfile=output_pdf)
        return True
    except ImportError:
        logger.error("No se pudo importar pypandoc. Asegúrate de que esté instalado.")
        return False
    except Exception as e:
        logger.error(f"Error al convertir con pypandoc: {str(e)}")
        return False

def convert_with_reportlab(md_content, output_pdf):
    try:
        doc = SimpleDocTemplate(output_pdf, pagesize=letter)
        styles = getSampleStyleSheet()
        flowables = []

        for line in md_content.split('\n'):
            if line.startswith('# '):
                flowables.append(Paragraph(line[2:], styles['Title']))
            elif line.startswith('## '):
                flowables.append(Paragraph(line[3:], styles['Heading2']))
            else:
                flowables.append(Paragraph(line, styles['Normal']))

        doc.build(flowables)
        return True
    except Exception as e:
        logger.error(f"Error al convertir con reportlab: {str(e)}")
        return False

def convert_md_to_pdf(md_file, output_folder):
    try:
        # Leer el contenido del archivo MD
        with open(md_file, 'r', encoding='utf-8') as file:
            md_content = file.read()
        
        # Convertir MD a HTML (solo para referencia, no se usa en la conversión)
        html_content = markdown.markdown(md_content)
        
        # Preparar el nombre del archivo de salida
        output_pdf = os.path.join(output_folder, os.path.splitext(os.path.basename(md_file))[0] + '.pdf')
        
        # Intentar conversión con pypandoc
        if convert_with_pypandoc(md_content, output_pdf):
            logger.info("Conversión exitosa con pypandoc")
            return output_pdf
        
        # Si falla, usar reportlab como última opción
        if convert_with_reportlab(md_content, output_pdf):
            logger.info("Conversión exitosa con reportlab")
            return output_pdf
        
        # Si todas las conversiones fallan, registrar un error
        logger.error("Todas las conversiones fallaron")
        return None
    except Exception as e:
        logger.error(f"Error inesperado en convert_md_to_pdf: {str(e)}")
        return None

def main():
    try:
        st.title("MDPDFusion: Convertidor de Markdown a PDF")
        
        # Selección de archivos MD
        md_files = st.file_uploader("Selecciona los archivos Markdown (.md)", type=['md'], accept_multiple_files=True)
        
        if md_files:
            # Crear una carpeta temporal para los archivos de salida
            with tempfile.TemporaryDirectory() as output_folder:
                for md_file in md_files:
                    # Guardar el archivo subido temporalmente
                    temp_md_path = os.path.join(output_folder, md_file.name)
                    with open(temp_md_path, 'wb') as temp_file:
                        temp_file.write(md_file.getvalue())
                    
                    # Convertir MD a PDF
                    pdf_path = convert_md_to_pdf(temp_md_path, output_folder)
                    
                    if pdf_path and os.path.exists(pdf_path):
                        # Ofrecer el archivo PDF para descarga
                        with open(pdf_path, 'rb') as pdf_file:
                            st.download_button(
                                label=f"Descargar {os.path.basename(pdf_path)}",
                                data=pdf_file,
                                file_name=os.path.basename(pdf_path),
                                mime="application/pdf"
                            )
                    else:
                        st.error(f"No se pudo convertir {md_file.name} a PDF. Por favor, revisa el archivo de entrada.")
    except Exception as e:
        st.error(f"Error inesperado: {str(e)}")
        logger.error(f"Error inesperado en main: {str(e)}")
        logger.error(traceback.format_exc())

if __name__ == "__main__":
    main()
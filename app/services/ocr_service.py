from PIL import Image
import pytesseract
from pdf2image import convert_from_path

def extract_text_from_image(image_path: str) -> str:
    """
    Extrae texto de una imagen utilizando OCR.
    
    :param image_path: Ruta de la imagen.
    :return: Texto extraído de la imagen.
    """
    try:
        return pytesseract.image_to_string(Image.open(image_path))
    except Exception as e:
        return f"Error al procesar la imagen: {str(e)}"

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extrae texto de un archivo PDF utilizando OCR.
    
    :param pdf_path: Ruta del archivo PDF.
    :return: Texto extraído del PDF.
    """
    try:
        text = ""
        images = convert_from_path(pdf_path)
        for i, page in enumerate(images):
            text += pytesseract.image_to_string(page)
        return text
    except Exception as e:
        return f"Error al procesar el PDF: {str(e)}"

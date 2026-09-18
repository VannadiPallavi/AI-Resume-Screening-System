from PyPDF2 import PdfReader

def extract_text_from_pdf(file_object):
    reader = PdfReader(file_object)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text.strip()
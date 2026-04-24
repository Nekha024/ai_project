import fitz  # PyMuPDF
from docx import Document 
import re

#Read PDF using PyMuPDF
def read_pdf(file_path):
    text = ""
    doc = fitz.open(file_path)

    for page in doc:
        text += page.get_text()

    return text


#Read DOCX
def read_docx(file_path):
    doc = Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

#Clean Text

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)  # remove extra spaces
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # remove symbols
    return text.strip()

#Combine Everything
def extract_resume_text(file_path):
    if file_path.endswith(".pdf"):
        text = read_pdf(file_path)

    elif file_path.endswith(".docx"):
        text = read_docx(file_path)

    else:
        raise ValueError("Unsupported file format")

    return clean_text(text)

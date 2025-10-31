# File: /ai-resume-analyzer/ai-resume-analyzer/app/utils/parsing.py

from typing import Union
import pdfplumber
import docx
import os

def parse_resume(file_path: str) -> Union[str, None]:
    """
    Parses a resume from a given file path.

    Args:
        file_path (str): The path to the resume file.

    Returns:
        Union[str, None]: The text content of the resume if parsing is successful, None otherwise.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension == '.pdf':
        return parse_pdf(file_path)
    elif file_extension == '.docx':
        return parse_docx(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a PDF or DOCX file.")

def parse_pdf(file_path: str) -> str:
    """
    Parses a PDF file and extracts text.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        str: The extracted text from the PDF.
    """
    with pdfplumber.open(file_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text() + '\n'
    return text.strip()

def parse_docx(file_path: str) -> str:
    """
    Parses a DOCX file and extracts text.

    Args:
        file_path (str): The path to the DOCX file.

    Returns:
        str: The extracted text from the DOCX.
    """
    doc = docx.Document(file_path)
    text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
    return text.strip()
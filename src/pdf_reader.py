# import PyPDF2

# def extract_text_from_pdf(pdf_path):
#     text = ""
#     with open(pdf_path, "rb") as file:
#         reader = PyPDF2.PdfReader(file)
#         for page in reader.pages:
#             page_text = page.extract_text()
#             if page_text:
#                 text += page_text + " "
#     return text.strip()  # Return cleaned text
import PyPDF2

def extract_text_from_pdf(pdf_path):
    """
    Reads and extracts text from a given PDF file.
    :param pdf_path: Path to the PDF file.
    :return: Extracted text as a single string.
    """
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                if page.extract_text():
                    text += page.extract_text() + " "
        return text.strip()
    except Exception as e:
        return f"❌ Error reading PDF: {e}"

if __name__ == "__main__":
    pdf_text = extract_text_from_pdf("sample_story.pdf")
    print(pdf_text[:500])  # Print the first 500 characters for preview

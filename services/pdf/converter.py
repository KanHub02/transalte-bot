from pdf2image import convert_from_path
import pytesseract

class PDFTextExtractor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def convert_pdf_to_images(self):
        return convert_from_path(self.pdf_path)

    def extract_text_from_images(self, pages, language="rus"):
        text = []
        for page in pages:
            # print(pytesseract.image_to_string(page, lang=language), "----------")
            text.append(pytesseract.image_to_string(page, lang=language))
        return text

    def extract_text_from_pdf(self, language='rus') -> str:
        pages = self.convert_pdf_to_images()
        text = self.extract_text_from_images(pages, language)
        extracted_text = ' '.join(text)
        return extracted_text
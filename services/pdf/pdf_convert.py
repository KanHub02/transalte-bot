from PyPDF2 import PdfReader
import aspose.pdf as ap


class PDFReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.reader = PdfReader(file_path)

    def get_number_of_pages(self):
        return len(self.reader.pages)

    def extract_text_from_page(self, page_number):
        page = self.reader.pages[page_number]
        return page.extract_text()


class PDFTextExtractor:
    def __init__(self, pdf_reader):
        self.pdf_reader = pdf_reader

    def extract_text_from_all_pages(self):
        res = ""
        for i in range(self.pdf_reader.get_number_of_pages()):
            text = self.pdf_reader.extract_text_from_page(i)
            res += str(text)
        return res


class PDFFileCreate:
    def __init__(self, new_file_name: str) -> None:
        document = ap.Document()
        self.document = document
        self.new_file_name = new_file_name

    def create_pages(self, page_text: str) -> "ap.Document.pages":
        page = self.document.pages.add()
        page.paragraphs.add(page_text)

    def create_log(self):
        self.document.convert(
            f"{self.new_file_name}.log",
            ap.PdfFormat.PDF_A_1B,
            ap.ConvertErrorAction.DELETE,
        )

    def save(self):
        self.document.save(f"{self.new_file_name}.pdf")


if __name__ == "__main__":
    pdf_reader = PDFReader("test.pdf")
    text_extractor = PDFTextExtractor(pdf_reader)
    result = text_extractor.extract_text_from_all_pages()
    print(result)

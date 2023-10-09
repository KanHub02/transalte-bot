from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from PIL import Image


class FontManager:
    @staticmethod
    def register_font(font_name, font_path):
        pdfmetrics.registerFont(TTFont(font_name, font_path))


class PDFGenerator:
    def __init__(self, filename, font_name="DejaVuSans"):
        self.canvas = canvas.Canvas(filename, pagesize=letter)
        self.width, self.height = letter
        self.font_name = font_name

    def draw_image(self, image_path):
        c = self.canvas
        width, height = letter
        with Image.open(image_path) as img:
            img_width, img_height = img.size

        c.drawImage(image_path, 100, height - 100 - img_height, img_width, img_height)

    def draw_text(self, x, y, text):
        self.canvas.setFont(self.font_name, 11)
        self.canvas.drawString(x, y, text)

    def save(self):
        self.canvas.save()


def main():
    font_manager = FontManager()
    font_manager.register_font('DejaVuSans', 'fonts/DejaVuSans.ttf')

    pdf_gen = PDFGenerator("reportlab_example.pdf")
    pdf_gen.draw_text(200, pdf_gen.height - 125, "Кыргызская республика")
    pdf_gen.draw_text(500, pdf_gen.height - 125, "Кыргызская республика")
    pdf_gen.draw_image(image_path="media/images/test.png")
    pdf_gen.save()


if __name__ == "__main__":
    main()

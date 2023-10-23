from decouple import config
import re

from pdf.converter import PDFTextExtractor
from translator.translate import EdenAITranslator, EdenAIConfig
from settings import translate_language_map
import marriage_patterns as pattern



EDEN_API_KEY = config("EDEN_API_KEY")

pdf_extractor = PDFTextExtractor('scan.pdf')
translator_config = EdenAIConfig(api_key=EDEN_API_KEY)
translator = EdenAITranslator(config=translator_config)
extracted_text = pdf_extractor.extract_text_from_pdf()
source_language, display_name = translator.detect_language(extracted_text)
translated_text = translator.translate("en", extracted_text, source_language)

print(translated_text)

info = pattern.extract_information(translated_text)

from typing import Any, List
import pprint

import easyocr


class TextReaderConfig:
    def __init__(
        self, language: List[str], file_path: str, gpu: bool, detail: bool = 0
    ) -> None:
        self.language = language
        self.file_path = file_path
        self.detail = detail 
        self.gpu = gpu


class TextReaderExecutor(TextReaderConfig):
    def __init__(
        self, language: List[str], file_path: str, detail: bool, gpu: bool
    ) -> None:
        super().__init__(language, file_path, detail, gpu)

    def text_reader(self) -> List[str]:
        reader = easyocr.Reader(self.language)
        result = reader.readtext(self.file_path, detail=self.detail, paragraph=True)
        return result


a = TextReaderExecutor(["ru", "en"], file_path="scan.png", detail=0, gpu=False)
pprint.pprint(a.text_reader())
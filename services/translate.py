import json
import requests


class EdenAIConfig:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.edenai.run/v2/translation/automatic_translation"
        self.headers = {"Authorization": f"Bearer {self.api_key}"}


class EdenAITranslator:
    def __init__(self, config: EdenAIConfig):
        self.config = config

    def translate(self, language, text, source_language):
        payload = {
            "show_original_response": False,
            "fallback_providers": "",
            "providers": "google,amazon",
            "source_language": source_language,
            "target_language": language,
            "text": text,
        }
        response = requests.post(
            self.config.base_url, json=payload, headers=self.config.headers
        )
        result = json.loads(response.text)
        if response.status_code == 200:
            return result["amazon"].get("text")
        else:
            return "Что-то пошло не так ИДИ НАХУЙ"
    
    def detect_language(self, message: str) -> str:
        url ="https://api.edenai.run/v2/translation/language_detection"
        payload={"show_original_response": False,"fallback_providers": "","providers": "google,amazon", 'text': message}
        response = requests.post(
            url=url, json=payload, headers=self.config.headers
        )
        result = json.loads(response.text)
        display_name = result['amazon']['items'][0].get("display_name")
        return result['amazon']['items'][0].get("language"), display_name
        


if __name__ == "__main__":
    api_key = "your_api_key_here"
    config = EdenAIConfig(api_key)
    translator = EdenAITranslator(config)

    language = "ru"  # Требуемый язык перевода
    text_to_translate = "Hello, world!"  # Текст для перевода

    translated_text = translator.translate(language, text_to_translate)
    print(translated_text)

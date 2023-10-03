import aiogram.utils.markdown as md

START_BOLD = (
    md.text(
        md.bold("Привет! Я бот-помошник."),
        "Я могу помочь тебе с переводом файла или текста.",
        sep="\n",
    ),
)
START_TEXT = ""
INFO_TEXT = "Я бот на основе иссскуственного инелекта. Использую интеграцию Amazon Eden AI API\nЯ делаю перевод для вас совершенно бесплатно"

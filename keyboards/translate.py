from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def translation_mode_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)  # Установим row_width равным 2 для вывода кнопок в две колонки

    btn1 = InlineKeyboardButton("Включить режим перевода", callback_data="enable_translation")
    btn2 = InlineKeyboardButton("Выключить режим перевода", callback_data="disable_translation")

    markup.add(btn1, btn2)
    return markup


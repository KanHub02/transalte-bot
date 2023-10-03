import logging

from aiogram.utils import executor
from aiogram import Bot, Dispatcher, types

from config import dp, bot, EDEN_API_KEY
from statics import START_BOLD, INFO_TEXT
from services.translate import EdenAITranslator, EdenAIConfig
from keyboards.translate import translation_mode_keyboard


logging.basicConfig(level=logging.INFO)

translation_mode = False  
language = "ru"

@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    await message.answer(
        START_BOLD,
        reply_markup=translation_mode_keyboard()
    )


@dp.callback_query_handler(lambda c: c.data == 'enable_translation')
async def enable_translation_mode(callback_query: types.CallbackQuery):
    global translation_mode
    translation_mode = True
    await bot.answer_callback_query(callback_query.id, "Режим перевода включен!")
    await bot.send_message(callback_query.from_user.id, "Введите текст для перевода:")


@dp.message_handler(commands=["info"])
async def info(message: types.Message):
    await bot.send_message(
        text=INFO_TEXT,
        chat_id=message.chat.id
    )
    

@dp.message_handler(content_types=types.ContentType.TEXT)
async def on_text(message: types.Message):
    global translation_mode
    if translation_mode:
        config = EdenAIConfig(EDEN_API_KEY)
        translator = EdenAITranslator(config)
        source_language, display_name = translator.detect_language(message.text)
        text_to_translate = message.text
        translated_text = translator.translate(language, text_to_translate, source_language)
        await message.reply("Перевод: " + str(translated_text))
        await message.reply("Язык: " + str(display_name))
    else:
        await message.reply("Перевод не включен. Включите режим перевода.")


@dp.callback_query_handler(lambda c: c.data == 'disable_translation')
async def disable_translation_mode(callback_query: types.CallbackQuery):
    global translation_mode
    translation_mode = False
    await bot.answer_callback_query(callback_query.id, "Режим перевода выключен!")
    await bot.send_message(callback_query.from_user.id, "Режим перевода выключен. Текст не будет переводиться.")



def execute():
    executor.start_polling(dp, skip_updates=True)
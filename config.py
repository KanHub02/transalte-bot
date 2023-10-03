from decouple import config
from aiogram import Bot, Dispatcher

EDEN_API_KEY = config("EDEN_API_KEY")

BOT_TOKEN = config("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

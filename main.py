import logging

from gtts import gTTS
from aiogram import Bot, Dispatcher, executor, types

TELEGRAM_BOT_TOKEN = "6439134880:AAFmRHrKP9yHYxMi2OEqrolJTdUnmGfJOBA"

logging.basicConfig(level = logging.INFO)

bot = Bot(token = TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands = ["start", "help"])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЯ бот-дублер!\nВведите что-нибудь!")

@dp.message_handler()
async def echo(message: types.Message):
    tts = gTTS(message.text, lang = "ru")

    tts.save(f"{message.from_user.id}.mp3")
    
    await message.answer_voice(open(f"{message.from_user.id}.mp3", "rb"))

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)
from gtts import gTTS
from aiogram import Bot, Dispatcher, types
from config.telegram import TELEGRAM_BOT_TOKEN

bot = Bot(token = TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands = ["start", "help"])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот-дублер! Введите что-нибудь!")

@dp.message_handler()
async def echo(message: types.Message):
    tts = gTTS(message.text, lang = "ru")

    tts.save(f"{message.from_user.id}.mp3")
    
    await message.answer_voice(open(f"{message.from_user.id}.mp3", "rb"))
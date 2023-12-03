from gtts import gTTS                               # Importing a text-to-speech module
from aiogram import Bot, Dispatcher, types          # Importing Box, Dispatcher and types from aiogram
from config.telegram import TELEGRAM_BOT_TOKEN      # Importing a Telegram token from the Telegram configurator

bot = Bot(token = TELEGRAM_BOT_TOKEN)               # Connecting the application to the Telegram bot
dp = Dispatcher(bot)                                # Connecting to the Telegram bot dispatcher application

@dp.message_handler(commands = ["start", "help"])
async def send_welcome(message: types.Message):     # Using the function when entering the start command
    await message.reply("Привет! Я бот-дублер! Введите что-нибудь!")

@dp.message_handler()
async def echo(message: types.Message):             # Using the function to vocalize the entered text
    tts = gTTS(message.text, lang = "ru")           # Receiving and voicing text in Russian

    tts.save(f"{message.from_user.id}.mp3")         # Saving an audio recording
    
    await message.answer_voice(open(f"{message.from_user.id}.mp3", "rb"))
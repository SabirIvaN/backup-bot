from aiogram import executor    # importing the executor module from the aiogram module
from actions.messages import dp # importing the bot dispatcher

# starting the bot
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)
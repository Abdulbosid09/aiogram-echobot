from aiogram import executor
from loader import bot

async def on_startup(dp):
    print("Bot ishga tushdi!")

if __name__ == "__main__":
    from main import dp

    executor.start_polling(dp,on_startup=on_startup)
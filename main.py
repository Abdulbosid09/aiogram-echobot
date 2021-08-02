from aiogram import types
from loader import dp

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    salom = f"Assalomu alaykum {message.from_user.first_name}"
    await message.answer(salom)

@dp.message_handler()
async def echo_message(message: types.Message):
    salom = f'''Assalomu alaykum {message.from_user.first_name}
Siz yozgan xabar <code>{message.text}</code>'''
    await message.answer(salom)

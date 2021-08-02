from aiogram import Bot , Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import API_KEY
storage=MemoryStorage()


bot = Bot(token=API_KEY,parse_mode="html")
dp = Dispatcher(bot,storage=storage)
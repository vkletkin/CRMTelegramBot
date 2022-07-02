import logging
from sqlighter import SQLighter
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# инициализируем бота
API_TOKEN = '5599022705:AAHX8VhiHhcVlVADgIXyrje7kmI8XoYjPfw'
bot = Bot(token=API_TOKEN)
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)

# задаем уровень логов
logging.basicConfig(level=logging.INFO)

# инициализируем соединение с БД
db = SQLighter('db.db')

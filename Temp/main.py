from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from config import token

bot = Bot(token=token)
dp = Dispatcher(bot)

button_hi = KeyboardButton('Привет! 👋')

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
greet_kb.add(button_hi)

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply('Бот создан для тестирования возможностей библиотек')

@dp.message_handler(commands=['start'])
async def keyboard(message: types.Message):
    await message.reply("Привет!", reply_markup=greet_kb)

@dp.message_handler()
async def echo(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)




if __name__ == "__main__":
    executor.start_polling(dp)
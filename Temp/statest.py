from aiogram.utils.helper import Helper, HelperMode, ListItem

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from config import token

from messages import *

class Test_states(Helper):
    mode = HelperMode.snake_case

    TEST_STATE_0 = ListItem()
    TEST_STATE_1 = ListItem()
    TEST_STATE_2 = ListItem()
    TEST_STATE_3 = ListItem()
    TEST_STATE_4 = ListItem()
    TEST_STATE_5 = ListItem()


bot = Bot(token=token)
dp = Dispatcher(bot)

dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())



@dp.message_handler(state='*', commands=['setstate'])
async def process_setstate_command(message: types.Message):
    argument = message.get_args()
    state = dp.current_state(user=message.from_user.id)
    if not argument:
        await state.reset_state()
        return await message.reply(MESSAGES['state_reset'])

    if (not argument.isdigit()) or (not int(argument) < len(Test_states.all())):
        return await message.reply(MESSAGES['invalid_key'].format(key=argument))

    await state.set_state(Test_states.all()[int(argument)])
    await message.reply(MESSAGES['state_change'], reply=False)

@dp.message_handler(state=Test_states.TEST_STATE_1)
async def first_test_state_case_met(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    await message.reply(f'Текущее состояние {state}')
    await message.reply('Первый!', reply=False)

@dp.message_handler(state=Test_states.TEST_STATE_2)
async def second_test_state_case_met(message: types.Message):
    await message.reply('Второй!', reply=False)

@dp.message_handler(state=Test_states.TEST_STATE_3 | Test_states.TEST_STATE_4)
async def third_or_fourth_test_state_case_met(message: types.Message):
    await message.reply('Третий или четвертый!', reply=False)

@dp.message_handler(state=Test_states.all())
async def some_test_state_case_met(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    text = MESSAGES['current_state'].format(
        current_state=await state.get_state(),
        states=Test_states.all()
    )
    await message.reply(text, reply=False)

async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(MESSAGES['start'])


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(MESSAGES['help'])

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)



if __name__ == "__main__":
    executor.start_polling(dp, on_shutdown=shutdown)

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import token

from aiogram.utils.helper import Helper, HelperMode, ListItem
from states import States

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from messages import MESSAGES

from markups import mark_up_1, mark_up_2, mark_up_3, mark_up_4

bot = Bot(token=token)
dp = Dispatcher(bot)

dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


async def shutdown(dispatcher: Dispatcher):
    '''
    Закрывает хранилище данных состояний
    '''
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(MESSAGES['start'].format(nick_name=message.from_user.username), reply=False, reply_markup=mark_up_1)


@dp.message_handler(state='*', commands=['state'])
async def what_state(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    await message.reply(MESSAGES['current_state'].format(current_state=await state.get_state()))

@dp.message_handler(state=States.TEST_STATE_1)
async def back_st_0(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    if message.text == 'Назад':
        await message.reply('Чем могу помочь?', reply=False, reply_markup=mark_up_1)
        await state.reset_state()

@dp.message_handler(state=States.TEST_STATE_2)
async def add_idea(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    if message.text == 'Наука и образование':
        await message.reply('Ссылка на канал с направлением (Наука и образование)', reply=False)
    elif message.text == 'Спорт и активный отдых':
        await message.reply('Ссылка на канал с направлением (Спорт и активный отдых)', reply=False)
    elif message.text == 'Досуг и развлечение':
        await message.reply('Ссылка на канал с направлением (Досуг и развлечение)', reply=False)
    elif message.text == 'Творчество и искусство':
        await message.reply('Ссылка на канал с направлением (Творчество и искусство)', reply=False)
    elif message.text == 'Благотворительность и волонтерство':
        await message.reply('Ссылка на канал с направлением (Благотворительность и волонтерство)', reply=False)
    elif message.text == 'Другое':
        await message.reply('Ссылка на канал с направлением (Другое)', reply=False)
    elif message.text == 'Назад':
        await message.reply('Чем могу помочь?', reply=False, reply_markup=mark_up_1)
        await state.reset_state()
    else:
        await message.reply(MESSAGES['unknown'], reply=False)

@dp.message_handler(state=States.TEST_STATE_3)
async def all_activities(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    if message.text == 'Наука и образование':
        await message.reply('Ссылка на канал с направлением (Наука и образование)', reply=False)
    elif message.text == 'Спорт и активный отдых':
        await message.reply('Ссылка на канал с направлением (Спорт и активный отдых)', reply=False)
    elif message.text == 'Досуг и развлечение':
        await message.reply('Ссылка на канал с направлением (Досуг и развлечение)', reply=False)
    elif message.text == 'Творчество и искусство':
        await message.reply('Ссылка на канал с направлением (Творчество и искусство)', reply=False)
    elif message.text == 'Благотворительность и волонтерство':
        await message.reply('Ссылка на канал с направлением (Благотворительность и волонтерство)', reply=False)
    elif message.text == 'Другое':
        await message.reply('Ссылка на канал с направлением (Другое)', reply=False)
    elif message.text == 'Назад':
        await message.reply('Чем могу помочь?', reply=False, reply_markup=mark_up_1)
        await state.reset_state()
    else:
        await message.reply(MESSAGES['unknown'], reply=False)


@dp.message_handler()
async def fs_answers(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    if message.text == 'Хочу узнать о тебе больше':
        await message.reply(MESSAGES['more'], reply=False, reply_markup=mark_up_3)
        await state.set_state(States.all()[1])
    elif message.text == 'Хочу предложить свою идею':
        await message.reply('Переход в блок предложить идею', reply=False, reply_markup=mark_up_4)
        await state.set_state(States.all()[2])
    elif message.text == 'Хочу узнать об актуальных мероприятиях!':
        await message.reply('Переход в блок актуальные мероприятия', reply=False, reply_markup=mark_up_2)
        await state.set_state(States.all()[3])
    else:
        await message.reply(MESSAGES['unknown'], reply=False)



if __name__ == "__main__":
    executor.start_polling(dp, on_shutdown=shutdown)

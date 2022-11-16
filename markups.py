from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

events = KeyboardButton('Хочу узнать об актуальных мероприятиях!')
suggest_an_idea = KeyboardButton('Хочу предложить свою идею')
more = KeyboardButton('Хочу узнать о тебе больше')

mark_up_1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
mark_up_1.add(events).add(suggest_an_idea).add(more)

science = KeyboardButton('Наука и образование')
sport = KeyboardButton('Спорт и активный отдых')
entertainment = KeyboardButton('Досуг и развлечение')
creation = KeyboardButton('Творчество и искусство')
charity = KeyboardButton('Благотворительность и волонтерство')
back = KeyboardButton('Назад')

mark_up_2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
mark_up_2.add(science).add(sport).add(entertainment).add(creation).add(charity).add(back)

mark_up_3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
mark_up_3.add(back)

other = 'Другое'

mark_up_4 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
mark_up_4.add(science).add(sport).add(entertainment).add(creation).add(charity).add(other).add(back)
from states import States


help_message = ''

start_message = 'Привет! {nick_name}\nЧем могу помочь ?'
invalid_key_message = 'Ключ "{key}" не подходит.\n' + help_message
state_change_success_message = 'Текущее состояние успешно изменено'
state_reset_message = 'Состояние успешно сброшено'
current_state_message = 'Текущее состояние - "{current_state}"'
more = '''Этот проект сделан студентами для студентов. Мы как никто другой понимаем тебя и твоё желание самореализоваться, получить новый опыт и сделать свою студенческую жизнь более яркой и познавательной.
Благодаря этому боту ты сможешь получать интересные посты и приглашения на увлекательные мероприятия, волнующие тебя, из различных ресурсов. Больше не надо подписываться на кучу источников -- только твои интересы и только бот-беззабот!
Наверняка и тебе хочется провести своё мероприятие или поделиться чем-то, но ты всё никак не можешь найти возможность. Поделись с ботом своей идеей, и её по достоинству оценят опытные организаторы'''
unknown = 'Такой команды я не знаю, попробуй что то другое'

MESSAGES = {
    'start': start_message,
    'help': help_message,
    'invalid_key': invalid_key_message,
    'state_change': state_change_success_message,
    'state_reset': state_reset_message,
    'current_state': current_state_message,
    'more': more,
    'unknown': unknown,
}
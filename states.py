from aiogram.utils.helper import Helper, HelperMode, ListItem


class States(Helper):
    mode = HelperMode.snake_case

    TEST_STATE_0 = ListItem()
    TEST_STATE_1 = ListItem()  # Клавиатура, только кнопка назад
    TEST_STATE_2 = ListItem()  # Хочу предложить свою идею
    TEST_STATE_3 = ListItem()  # Хочу узнать об актуальных мероприятиях!
    TEST_STATE_4 = ListItem()
    TEST_STATE_5 = ListItem()


if __name__ == "__main__":
    states = States()
    print(states.TEST_STATE_0)

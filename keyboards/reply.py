from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_main_keyboard():
    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="Подать заявку"),
                KeyboardButton(text="Прямая связь"),
                KeyboardButton(text="О работе"),
            ]
        ],
    )


def create_admin_keyboard():
    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="Обработка заявок"),
                KeyboardButton(text="Создание вопросов"),
                KeyboardButton(text="Редактирование вопросов"),
                KeyboardButton(text="Удаление вопросов"),
            ]
        ],
    )

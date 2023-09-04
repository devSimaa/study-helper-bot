from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def kb():
    kb = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [KeyboardButton(text="/schedule"), KeyboardButton(text="/homework")],
            [KeyboardButton(text="/Key_on"), KeyboardButton(text="/Key_off")],
        ],
    )
    return kb

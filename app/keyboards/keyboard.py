from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def kb():
    kb = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [KeyboardButton(text="🗓 Расписание")],
            [KeyboardButton(text="📝Домашнее задание")],
            [KeyboardButton(text="🕘 Время до конца пары")],
        ],
    )
    return kb

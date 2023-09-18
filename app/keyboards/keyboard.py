from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def kb(admin=None):
    kb = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [KeyboardButton(text="🗓 Расписание")],
            [KeyboardButton(text="📝Домашнее задание")],
            [KeyboardButton(text="🕘 Время до конца пары")],
        ],
    )
    if admin is True: kb.add(KeyboardButton(text="Редактировать"))
    return kb

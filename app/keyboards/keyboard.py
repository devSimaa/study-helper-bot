from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


async def base_kb(admin=None):
    kb = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [KeyboardButton(text="🗓 Расписание")],
            [KeyboardButton(text="📝 Домашнее задание")],
            [KeyboardButton(text="🕘 Время до конца пары")],
        ],
    )
    if admin is True: 
        kb1 = (KeyboardButton(text="✏️ Редактировать"))
        kb2 =(KeyboardButton(text="📊 Статистика"))
        kb.add(kb1,kb2)
    return kb

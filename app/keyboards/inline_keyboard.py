from aiogram.types import (
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


def base_ikb():
    ikb = InlineKeyboardMarkup(
        resize_keyboard=True,
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Название", callback_data="Калбек"),
            ],
        ],
    )
    return ikb
def update_statistica_ikb():
    ikb = InlineKeyboardMarkup(
        resize_keyboard=True,
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Обновить", callback_data="update_statistica"),
            ],
        ],
    )
    return ikb

def homework_ikb(variable):
    if variable == 1:
        ikb = InlineKeyboardMarkup(
            resize_keyboard=True,
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="*Эта неделя", callback_data="Эта неделя(дз)"
                    ),
                    InlineKeyboardButton(
                        text="Другая неделя", callback_data="Другая неделя(дз)"
                    ),
                ],
            ],
        )
    elif variable == 2:
        ikb = InlineKeyboardMarkup(
            resize_keyboard=True,
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Эта неделя", callback_data="Эта неделя(дз)"
                    ),
                    InlineKeyboardButton(
                        text="*Другая неделя", callback_data="Другая неделя(дз)"
                    ),
                ],
            ],
        )

    return ikb


def schedule_ikb(variable):
    if variable == 1:
        ikb = InlineKeyboardMarkup(
            resize_keyboard=True,
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="*Эта неделя", callback_data="Эта неделя(расписание)"
                    ),
                    InlineKeyboardButton(
                        text="Другая неделя", callback_data="Другая неделя(расписание)"
                    ),
                ],
            ],
        )
    elif variable == 2:
        ikb = InlineKeyboardMarkup(
            resize_keyboard=True,
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Эта неделя", callback_data="Эта неделя(расписание)"
                    ),
                    InlineKeyboardButton(
                        text="*Другая неделя", callback_data="Другая неделя(расписание)"
                    ),
                ],
            ],
        )
    return ikb

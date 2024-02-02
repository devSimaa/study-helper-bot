from aiogram.types import (
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from database.service.groupe import get_groups


async def group_ikb():
    groups = await get_groups()

    ikb = InlineKeyboardMarkup(resize_keyboard=True)
    for i in groups:
        ikb.add(InlineKeyboardButton(text=i['group'], callback_data=f"{i['group']}_join"))
    return ikb


async def start_ikb():
    ikb = InlineKeyboardMarkup()
    ikb.add(InlineKeyboardButton(text="Выбрать группу", callback_data="select_group"))
    return ikb


async def base_ikb():
    ikb = InlineKeyboardMarkup(
        resize_keyboard=True,
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Название", callback_data="Калбек"),
            ],
        ],
    )
    return ikb


async def update_statistica_ikb():
    ikb = InlineKeyboardMarkup(
        resize_keyboard=True,
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Обновить", callback_data="update_statistica"),
            ],
        ],
    )
    return ikb


async def homework_ikb(variable):
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


async def schedule_ikb(variable):
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

from aiogram.types import (
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from database.service.groupe import get_groups


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

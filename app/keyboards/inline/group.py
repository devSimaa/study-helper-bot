from aiogram.types import (ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton)
from database.service.groupe import get_groups


async def group_ikb():
    groups = await get_groups()

    ikb = InlineKeyboardMarkup(resize_keyboard=True)
    for i in groups:
        ikb.add(InlineKeyboardButton(text=i['group'], callback_data=f"{i['group']}_join"))
    return ikb



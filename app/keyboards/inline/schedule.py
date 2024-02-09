from aiogram.types import (ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton)

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
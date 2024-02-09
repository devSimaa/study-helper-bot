from aiogram.types import (ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton)



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

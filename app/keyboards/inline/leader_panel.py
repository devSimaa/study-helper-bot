from aiogram.types import (
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


async def leader_panel_ikb():
    ikb = InlineKeyboardMarkup(
        resize_keyboard=True,
        inline_keyboard=[
            [
                InlineKeyboardButton(text="➕ Add subject", callback_data="leaderAddSubject"),
                InlineKeyboardButton(text="❌ Delete subject", callback_data="leaderAddSubject"),
            ],
            [
                InlineKeyboardButton(text="✏️Schedule", callback_data="leaderEditSchedule"),
            ],
        ],
    )
    return ikb

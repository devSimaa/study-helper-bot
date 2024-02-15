from aiogram.types import (ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton)

async def admin_panel_ikb():
    ikb = InlineKeyboardMarkup(
        resize_keyboard=True,
        inline_keyboard=[
            [
                InlineKeyboardButton(text="👤 Users", callback_data="adminUser"),
                InlineKeyboardButton(text="🎓 Group", callback_data="adminGroup"),
            ],
        ],
    )
    return ikb

async def admin_panel_group_ikb():
    ikb = InlineKeyboardMarkup(
        resize_keyboard=True,
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Добавить группу [+]", callback_data="adminGroup_addGroup"),
                InlineKeyboardButton(text="Удалить группу [-]", callback_data="adminGroup_delGroup"),
            ],
        ],
    )
    return ikb

async def admin_panel_user_ikb():
    ikb = InlineKeyboardMarkup(
        resize_keyboard=True,
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Удалить старосту [+]", callback_data="adminUser_addLider"),
                InlineKeyboardButton(text="Назначить старосту [-]", callback_data="adminUser_delLider"),
            ],
            [
                InlineKeyboardButton(text="Заблокировать пользователя", callback_data="adminUser_banUser"),
                InlineKeyboardButton(text="Разблокировать пользователя", callback_data="adminUser_unbanUser"),
            ],
        ],
    )
    return ikb

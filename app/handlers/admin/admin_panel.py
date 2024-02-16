from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command

from loader import dp, bot
from app.keyboards.inline.admin_panel import admin_panel_ikb
from app.filters.admin import IsAdmin


@dp.message_handler(IsAdmin(), Command('admin'))
async def admin_panel_command(message: types.Message):
    await message.answer("Добро пожаловать в админ панель!", reply_markup=await admin_panel_ikb())


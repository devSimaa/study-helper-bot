from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from app.filters.admin import IsAdmin
from app.keyboards.inline.admin_panel import admin_panel_user_ikb

@dp.callback_query_handler(IsAdmin(), Text("adminUser"))
async def adminGroup(callback: types.CallbackQuery):
    await callback.message.edit_text('Что вы хотите сделать?', reply_markup=await admin_panel_user_ikb())



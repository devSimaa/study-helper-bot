from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command

from loader import dp, bot
from app.keyboards.inline.leader_panel import leader_panel_ikb
from app.filters.leader import IsLeader


@dp.message_handler(IsLeader(), Command('leader'))
async def leader_panel_command(message: types.Message):
    await message.answer("Добро пожаловать в админ панель!", reply_markup=await leader_panel_ikb())


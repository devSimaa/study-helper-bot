from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from app.filters.admin import IsAdmin
from database.service.groupe import add_group
from database.service.admin import get_admins


@dp.message_handler(Command("users"), IsAdmin())
async def user_controller(message: types.Message):
    pass



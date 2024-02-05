from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from app.states import Group
from app.filters.admin import IsAdmin
from database.service.groupe import add_group


        

@dp.message_handler(Command("add_group"), IsAdmin())
async def add_group_comnand(message: types.Message):
    await message.answer('Укажите название группы')
    await Group.name.set()  


@dp.message_handler(IsAdmin(),state=Group.name)
async def add_group_input(message: types.Message, state=FSMContext):
    await add_group(message.text)
    await message.reply((f"Added {message.text}"))
    await Group.next()


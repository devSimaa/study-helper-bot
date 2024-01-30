from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from app.states import Group

@dp.message_handler(Command("add_group"), user_id="743347029")
async def add_group_comnand(message: types.Message):
    await message.answer('Укажите название группы')
    await Group.name.set()


@dp.message_handler(state=Group.name)
async def load_gender(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        group_name = message.text
        await message.reply((f"Added {group_name}"))

    await Group.next()


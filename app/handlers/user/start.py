from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart
from loader import dp, bot
from app.keyboards.keyboard import kb
from data.config import admins
from database.service.users import add_user


@dp.message_handler(CommandStart())
async def start_command(message: types.Message):
    if message.from_user.id == int(admins):
        await message.answer(
        text="Здраствуйте, вы админ",
        reply_markup=kb(True),
    )
    else:
        await message.answer(
            text="Здраствуйте.",
            reply_markup=kb(),
        )
    await add_user(message.from_user.id)
    await message.delete()
    # await statistic("Старт")


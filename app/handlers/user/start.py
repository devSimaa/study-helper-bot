from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart
from loader import dp, bot
from app.keyboards.keyboard import kb


@dp.message_handler(CommandStart())
async def start_command(message: types.Message):
    await message.answer(
        text="Здраствуйте.",
        reply_markup=kb(),
    )
    await message.delete()

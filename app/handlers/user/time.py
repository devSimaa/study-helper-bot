from aiogram import types, Dispatcher
from loader import dp, bot


@dp.message_handler(commands="time")
async def time_command(message: types.Message):
    await message.answer(text="Здраствуйте.")
    await message.delete()

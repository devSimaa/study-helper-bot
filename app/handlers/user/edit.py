from aiogram import types, Dispatcher
from loader import dp, bot
from database.statistica import get_statistic


@dp.message_handler(text="📊 Статистика")
@dp.message_handler(commands="statistic")
async def time_command(message: types.Message):
    await message.answer(
        text=f"📊Статистика использывания:\n{await get_statistic()}"
    )
    await message.delete()


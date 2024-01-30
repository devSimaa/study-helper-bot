from aiogram import types, Dispatcher
from loader import dp, bot
from database.service.statistica import statistic


@dp.message_handler(text="🕘 Время до конца пары")
@dp.message_handler(commands="time")
async def time_command(message: types.Message):
    await message.answer(
        text="""
1) 8:30 - 9:30
2) 9:40 - 10:40
3) 10:50 - 11:50
4) 12:00 - 13:00
5) 13:10 - 14:10
6) 15:20 - 15:20
7) 16:30 - 16:30
"""
    )
    await message.delete()
    await statistic("Время")

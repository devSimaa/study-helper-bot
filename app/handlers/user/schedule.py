from aiogram import types, Dispatcher
from loader import dp, bot
from app.keyboards.inline_keyboard import schedule_ikb
from database.service.schedule import get_schedule
from database.service.statistica import statistic



@dp.message_handler(text="🗓 Расписание")
@dp.message_handler(commands="schedule")
async def schedule_command(message: types.Message):
    await message.answer(text=await get_schedule(week="first"), reply_markup=schedule_ikb(1))
    await message.delete()
    await statistic("Расписание")



@dp.callback_query_handler(text=["Эта неделя(расписание)", "Другая неделя(расписание)"])
async def schedule_handler(callback: types.CallbackQuery):
    if callback.data == "Эта неделя(расписание)":
        await callback.message.edit_text(
            text=await get_schedule(week="first"), reply_markup=schedule_ikb(1)
        )
    elif callback.data == "Другая неделя(расписание)":
        await callback.message.edit_text(
            text=await get_schedule(week="second"),
            reply_markup=schedule_ikb(2),
        )
    await statistic("Расписание")

from aiogram import types, Dispatcher
from loader import dp, bot
from app.keyboards.inline.schedule import schedule_ikb
from database.service.schedule import get_schedule




@dp.message_handler(text="🗓 Расписание")
@dp.message_handler(commands="schedule")
async def schedule_command(message: types.Message):
    await message.answer(text=await get_schedule(message.from_user.id, "week1"), reply_markup=await schedule_ikb(1))
    await message.delete()


@dp.callback_query_handler(text=["Эта неделя(расписание)", "Другая неделя(расписание)"])
async def schedule_handler(callback: types.CallbackQuery):
    if callback.data == "Эта неделя(расписание)":
        await callback.message.edit_text(
            text=await get_schedule(user_id=callback.from_user.id, week="week1"), reply_markup=await schedule_ikb(1)
        )
    elif callback.data == "Другая неделя(расписание)":
        await callback.message.edit_text(
            text=await get_schedule(user_id=callback.from_user.id, week="week2"),
            reply_markup=await schedule_ikb(2),
        )


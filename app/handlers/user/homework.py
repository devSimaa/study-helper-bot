from aiogram import types, Dispatcher
from loader import dp, bot
from app.keyboards.inline_keyboard import homework_ikb
from database.db_requests import get_schedule
from database.statistica import statistic



@dp.message_handler(text="📝Домашнее задание")
@dp.message_handler(commands="homework")

async def homework_command(message: types.Message):
    await message.answer(text=await get_schedule(week="first"), reply_markup=homework_ikb(1))
    await message.delete()
    await statistic("Домашнее задание")

@dp.callback_query_handler(text=["Эта неделя(дз)", "Другая неделя(дз)"])
async def homework_handler(callback: types.CallbackQuery):
    if callback.data == "Эта неделя(дз)":
        await callback.message.edit_text(
            text=await get_schedule(week="first"), reply_markup=homework_ikb(1)
        )
    elif callback.data == "Другая неделя(дз)":
        await callback.message.edit_text(
            text=await get_schedule(week="second"), reply_markup=homework_ikb(2)
        )
    await statistic("Домашнее задание")
    

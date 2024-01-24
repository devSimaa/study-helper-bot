from aiogram import types, Dispatcher

from loader import dp, bot
from app.keyboards.inline_keyboard import update_statistica_ikb

from database.statistica import get_statistic


@dp.message_handler(text="📊 Статистика")
@dp.message_handler(commands="statistic")
async def time_command(message: types.Message):
    await message.answer(
        text=f"📊Статистика использывания:\n{await get_statistic()}",reply_markup=update_statistica_ikb()
    )
    await message.delete()


@dp.callback_query_handler(text="update_statistica")
async def time_command(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=f"📊Статистика использывания:\n{await get_statistic()}"  
    )




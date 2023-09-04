from aiogram import types, Dispatcher
from loader import dp, bot
from app.keyboards.keyboard import kb


# вкл.чение клавиатуры
@dp.message_handler(commands="Key_on")
async def start_command(message: types.Message):
    await message.answer(
        text="Клавиатура включена.",
        reply_markup=kb(),
    )
    await message.delete()


# выключение клавиатуры
@dp.message_handler(commands=["Key_off"])
async def start_command(message: types.Message):
    remove_kb = types.ReplyKeyboardRemove()
    await message.answer(
        text="Клавиатура выключена.",
        reply_markup=remove_kb,
    )
    await message.delete()

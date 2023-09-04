from aiogram import types, Dispatcher
from loader import dp, bot
from app.keyboards.inline_keyboard import homework_ikb
from app.others.document_reader import doc_reader


@dp.message_handler(text="📝Домашнее задание")
@dp.message_handler(commands="homework")
async def homework_command(message: types.Message):
    await message.answer(text=doc_reader("homework_1"), reply_markup=homework_ikb(1))
    await message.delete()


@dp.callback_query_handler(text=["Эта неделя(дз)", "Другая неделя(дз)"])
async def homework_handler(callback: types.CallbackQuery):
    if callback.data == "Эта неделя(дз)":
        await callback.message.edit_text(
            text=doc_reader("homework_1"), reply_markup=homework_ikb(1)
        )
    elif callback.data == "Другая неделя(дз)":
        await callback.message.edit_text(
            text=doc_reader("homework_2"), reply_markup=homework_ikb(2)
        )

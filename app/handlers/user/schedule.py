from aiogram import types, Dispatcher
from loader import dp, bot
from app.keyboards.inline_keyboard import schedule_ikb
from app.others.document_reader import doc_reader

# ...document.txt_reader.reader_txt(r"D:\010101010\python\Bots\study-bot\document\schedule_1.txt")


# распиание
@dp.message_handler(commands="schedule")
async def schedule_command(message: types.Message):
    await message.answer(text=doc_reader("schedule_1"), reply_markup=schedule_ikb(1))
    await message.delete()


@dp.callback_query_handler(text=["Эта неделя(расписание)", "Другая неделя(расписание)"])
async def schedule_handler(callback: types.CallbackQuery):
    if callback.data == "Эта неделя(расписание)":
        await callback.message.edit_text(
            text=doc_reader("schedule_1"), reply_markup=schedule_ikb(1)
        )
    elif callback.data == "Другая неделя(расписание)":
        await callback.message.edit_text(
            text=doc_reader("schedule_2"),
            reply_markup=schedule_ikb(2),
        )

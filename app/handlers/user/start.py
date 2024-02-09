from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from loader import dp
from app.keyboards.inline.default import start_ikb
from database.service.users import add_user
from app.states.join_group import JoinGroup

@dp.message_handler(CommandStart())
async def start_command(message: types.Message):
    text = ("Бот для помощи в учебе! \nПодробнее в команде /help .")
    await message.answer(
        text=f"👋,  <a href='tg://user?id={message.from_user.id}'>{(message.from_user.full_name)}</a>\
            \n{text}" ,
        reply_markup= await start_ikb()
        )
    await add_user(user_id=message.from_user.id)
    await JoinGroup.message.set()
    





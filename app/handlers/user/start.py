from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart, Text
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from app.keyboards.keyboard import base_kb
from app.keyboards.inline_keyboard import group_ikb, start_ikb
from data.config import admins
from database.service.users import add_user, user_join_group
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
    





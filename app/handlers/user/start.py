from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart, Text
from loader import dp, bot
from app.keyboards.keyboard import base_kb
from app.keyboards.inline_keyboard import group_ikb, start_ikb

from data.config import admins
from database.service.users import add_user


@dp.message_handler(CommandStart())
async def start_command(message: types.Message):
    text = ("Бот для помощи в учебе! \nПодробнее в команде /help .")
    await message.answer(
        text=f"👋,  <a href='tg://user?id={message.from_user.id}'>{(message.from_user.full_name)}</a>\
            \n{text}" ,
        reply_markup= await start_ikb()
        )

@dp.callback_query_handler(Text("select_group"))
async def select_group(callback: types.CallbackQuery):
    await callback.message.edit_text("Выберите группу, или напишите свою.",
                                     reply_markup=await group_ikb()) 

@dp.callback_query_handler(Text(endswith="_join"))
async def join_group(callback: types.CallbackQuery):
    group = callback.data.replace("_join", "")
    await add_user(user_id=callback.from_user.id, group=group)
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer(f"Вы теперь в группе! Попробуйте использовать клавитару бота или обратитесь к /help для ознакомления с командами.",
                          reply_markup=await base_kb())
    

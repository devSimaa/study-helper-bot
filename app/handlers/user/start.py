from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart, Text
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from app.keyboards.keyboard import base_kb
from app.keyboards.inline_keyboard import group_ikb, start_ikb
from data.config import admins
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
    await JoinGroup.message.set()
    

@dp.callback_query_handler(Text("select_group"),state=JoinGroup.message)
async def select_group(callback: types.CallbackQuery):
    await callback.message.edit_text("Выберите группу, или напишите свою.",
                                     reply_markup=await group_ikb()) 
    await JoinGroup.next()
@dp.message_handler(state=JoinGroup.select)
async def join_group_inpuy(message: types.Message, state=FSMContext):
    await add_user(user_id=message.from_user.id, group=message.text)
    await message.answer("ДА")
    await JoinGroup.next()

@dp.callback_query_handler(Text(endswith="_join"), state=JoinGroup.select)
async def join_group(callback: types.CallbackQuery, state=FSMContext):
    group = callback.data.replace("_join", "")
    await add_user(user_id=callback.from_user.id, group=group)
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer(f"Вы теперь в группе! Попробуйте использовать клавитару бота или обратитесь к /help для ознакомления с командами.",
                          reply_markup=await base_kb())
    await JoinGroup.next()


from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from database.service.users import user_join_group
from app.keyboards.default.default import base_kb
from app.keyboards.inline.group import group_ikb

from app.states.join_group import JoinGroup


@dp.message_handler(Command("change_group"))
async def change_group_command(message: types.Message):
    await JoinGroup.message.set()
    await select_group(message)

@dp.message_handler(state=JoinGroup.select)
async def join_group_inpuy(message: types.Message, state=FSMContext):
    await user_join_group(user_id=int(message.from_user.id), group=message.text)
    await message.answer("Вы теперь в группе! Попробуйте использовать клавитару бота или обратитесь к /help для ознакомления с командами.")
    await JoinGroup.next()

@dp.callback_query_handler(Text("select_group"),state=JoinGroup.message)
async def select_group(callback: types.CallbackQuery):
    await callback.message.edit_text("Выберите группу, или напишите свою.",reply_markup=await group_ikb()) 
    await JoinGroup.next()

@dp.callback_query_handler(Text(endswith="_join"), state=JoinGroup.select)
async def join_group(callback: types.CallbackQuery, state=FSMContext):
    group = callback.data.replace("_join", "")
    await user_join_group(user_id=callback.from_user.id, group=group)
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer(f"Вы теперь в группе! Попробуйте использовать клавитару бота или обратитесь к /help для ознакомления с командами.",
                          reply_markup=await base_kb())
    await JoinGroup.next()

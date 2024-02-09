from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from app.states import Group
from app.filters.admin import IsAdmin
from database.service import groupe
from app.keyboards.inline_keyboard import admin_panel_group_ikb

        

@dp.callback_query_handler(IsAdmin(), Text("adminGroup"))
async def adminGroup(callback: types.CallbackQuery):
    await callback.message.edit_text('Что вы хотите сделать?', reply_markup=await admin_panel_group_ikb())

@dp.callback_query_handler(IsAdmin(), Text("adminGroup_addGroup"))
async def add_group(callback: types.CallbackQuery):
    await callback.message.edit_text('Укажите название группы')
    await Group.name.set()  


@dp.message_handler(IsAdmin(),state=Group.name)
async def add_group_input(message: types.Message, state=FSMContext):
    await groupe.add_group(message.text)
    await  message.reply((f"<code>{message.text}</code> - группа добавленна."))
    await Group.next()


@dp.callback_query_handler(IsAdmin(), Text("adminGroup_delGroup"))
async def del_group(callback: types.CallbackQuery):
    await callback.message.edit_text('Укажите название группы')
    await Group.name.set()  


@dp.message_handler(IsAdmin(),state=Group.name)
async def del_group_input(message: types.Message, state=FSMContext):
    await groupe.add_group(message.text)
    await  message.reply((f"<code>{message.text}</code> - группа удаленна."))
    await Group.next()


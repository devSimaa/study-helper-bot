from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from app.states import Group
from app.filters.admin import IsAdmin
from database.service import groupe
from app.keyboards.inline.adin_panel import admin_panel_group_ikb
from app.keyboards.inline.group import del_group_ikb

        

@dp.callback_query_handler(IsAdmin(), Text("adminGroup"))
async def adminGroup(callback: types.CallbackQuery):
    await callback.message.edit_text('Что вы хотите сделать?', reply_markup=await admin_panel_group_ikb())

@dp.callback_query_handler(IsAdmin(), Text("adminGroup_addGroup"))
async def add_group(callback: types.CallbackQuery):
    await callback.message.edit_text('Укажите название группы')
    await Group.addGroup.set()  


@dp.message_handler(IsAdmin(),state=Group.addGroup)
async def add_group_input(message: types.Message, state=FSMContext):
    await groupe.add_group(message.text)
    await  message.reply((f"<code>{message.text}</code> - группа добавленна."))
    await Group.next()


@dp.callback_query_handler(IsAdmin(), Text("adminGroup_delGroup"))
async def del_group(callback: types.CallbackQuery):
    await callback.message.edit_text('Укажите название группы', reply_markup=await del_group_ikb())
    await Group.delGroup.set()  

@dp.callback_query_handler(IsAdmin(), Text(endswith="_del"), state=Group.delGroup)
async def select_del_group(callback: types.CallbackQuery):
    group = callback.data.replace("_del", "")
    await groupe.del_group(group)
    await  callback.message.reply((f"<code>{group}</code> - группа удаленна."))
    await Group.next()

@dp.message_handler(IsAdmin(),state=Group.delGroup)
async def del_group_input(message: types.Message, state=FSMContext):
    await groupe.del_group(message.text)
    await  message.reply((f"<code>{message.text}</code> - группа удаленна."))
    await Group.next()


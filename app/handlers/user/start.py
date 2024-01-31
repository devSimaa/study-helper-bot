from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart, Text
from loader import dp, bot
from app.keyboards.keyboard import kb
from app.keyboards.inline_keyboard import group_ikb

from data.config import admins
from database.service.users import add_user


@dp.message_handler(CommandStart())
async def start_command(message: types.Message):
    if message.from_user.id == int(admins):
        await message.answer(
        text="Здраствуйте, вы админ",
        reply_markup=await group_ikb(),
    )
    else:
        await message.answer(
            text="Здраствуйте.",
            reply_markup=kb(),
        )
    await message.delete()

@dp.callback_query_handler(Text(endswith="_join"))
async def join_group(callback: types.CallbackQuery):
    group = callback.data.replace("_join", "")
    await add_user(user_id=callback.from_user.id, group=group)
    await callback.answer(f"Вы добавленны в группу {group}")
    

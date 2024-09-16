from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from tgbot_admin.bot.loader import dp, bot, _

import os
import django
# Устанавливаем переменную окружения для Django настроек
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_core.settings')

# Инициализируем Django
django.setup()

from tgbot_admin.models import TodoList
from asgiref.sync import sync_to_async

@sync_to_async
def get_list():
    return list(TodoList.objects.values('title', 'content', 'created'))

@dp.message_handler(CommandStart())
async def _start_command(message: types.Message):
    # from tgbot_admin.models import get_list

    todolist = await get_list()
    list = [i for i in todolist]
    print(list)
    text = _("👋, <a href='tg://user?id={}'>{}</a>")
    await message.answer(text.format(message.from_user.id, message.from_user.full_name))
    # await message.answer(todolist)

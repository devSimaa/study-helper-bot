from aiogram.dispatcher.filters.state import StatesGroup, State


class JoinGroup(StatesGroup):
    message = State()
    select = State()
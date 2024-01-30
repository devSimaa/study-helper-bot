from aiogram.dispatcher.filters.state import StatesGroup, State


class Group(StatesGroup):
    name = State()
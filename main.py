from aiogram import Bot, Dispatcher, executor
from app import middlewares, handlers
from loader import dp, bot


async def start_up(_):
    print(" [< Бот запущен >] ")


if __name__ == "__main__":
    executor.start_polling(
        dp,
        on_startup=start_up,
        skip_updates=True,
    )

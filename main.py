from aiogram import Bot, Dispatcher, executor
from app import middlewares, handlers
from loader import dp, bot
from database.models.user import db_close

async def start_up(_):
    # await db_start()
    import database.statistica
    print("< Bot start_up >")   

async def on_shutdown(dispatcher: Dispatcher):
    await db_close()
    print("Shutting down...")

if __name__ == "__main__":
    executor.start_polling(
        dp,
        on_startup=start_up,
        on_shutdown=on_shutdown,
        skip_updates=True,
    )
    
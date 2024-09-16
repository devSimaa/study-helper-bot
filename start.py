import os
import sys
from multiprocessing import Process, current_process
import asyncio

def run_django():
    """Run the Django server."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(['manage.py', 'runserver', '--noreload'])

async def run_bot():
    """Run the Telegram bot."""
    from tgbot_admin.bot.run import runbot
    await runbot()  # Корректный вызов корутины

def start_bot():
    """Wrapper function to run the bot in a new event loop."""
    asyncio.run(run_bot())  # Запускаем корутину run_bot() через asyncio.run()

if __name__ == '__main__':
    # Проверяем, что код запускается только в основном процессе
    if current_process().name == 'MainProcess':
        # Создаем процессы для Django и бота
        django_process = Process(target=run_django, name='DjangoProcess')
        bot_process = Process(target=start_bot, name='BotProcess')  # Используем start_bot, чтобы правильно вызвать корутину

        # Запускаем процессы
        django_process.start()
        bot_process.start()

        # Ждем завершения процессов
        django_process.join()
        bot_process.join()

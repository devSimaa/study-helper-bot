from database.db_connect import db_time
from .users import get_user


async def get_time(user_id):
    group = await get_user(user_id)['group']
    return db_time.find_one({'group': group})

async def add_time():
    pass

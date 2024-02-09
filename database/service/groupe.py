from database.db_connect import db_groups
from .schedule import add_schedule


async def get_groups() -> list:
    return db_groups.find({}, {"_id": 0})
    

async def add_group(group_name):
    db_groups.insert_one({"group": group_name})
    
    await add_schedule(group_name)

async def del_group(group_name):
    db_groups.delete_one({"group": group_name})
    
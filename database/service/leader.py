from database.db_connect import db_users

async def get_leader(user_id):
    return db_users.find_one({"_id":user_id})

async def add_leader(user_id) -> None:
    if await get_leader(user_id) is None: db_users.insert_one({"_id": user_id, "group": "", "role": "leader"})

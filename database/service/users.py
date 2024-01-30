from database.db_connect import db_users

async def get_user(user_id) -> None:
    return db_users.find_one({"_id":user_id})

async def add_user(user_id, group: str) -> None:
    if await get_user(user_id) is None: db_users.insert_one({"_id": user_id, "group": group})

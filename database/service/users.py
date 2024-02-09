from database.db_connect import db_users

async def get_user(user_id) -> None:
    print(db_users.find_one({"_id":user_id}))
    return db_users.find_one({"_id":user_id})

async def add_user(user_id) -> None:
    if await get_user(user_id) is None: db_users.insert_one({"_id": user_id, "group": "", "role": "user"})

async def user_join_group(user_id, group: str) -> None:
    db_users.update_one({"_id":user_id}, {"$set":{"group": group}})
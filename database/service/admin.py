from database.db_connect import db_users
from data.config import admins

async def get_admins() -> list:
    admins_users = db_users.find({"role":"admin"}, {"_id":1})
    for i in admins_users:
        admins.append(i["_id"])
    return admins

async def add_admin(user_id: int) -> None:
    db_users.update_one({"_id":user_id}, {"$set":{"role": "admin"}})    
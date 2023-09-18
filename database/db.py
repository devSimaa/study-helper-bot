from pymongo import MongoClient
import asyncio
from data.config import mongodb_url


async def db_start():
    global client, coll, db
    client = MongoClient(mongodb_url)
    db = client["studybot"]
    coll = db.schedule


async def db_close():
    client.close()

async def get_schedule(day):
    inf = (coll.find_one({"day": f"{day}:"},{"_id": 0, "day": 0}))
    sche = f"{day}: \n"
    for key, value in inf.items():
        sche += (f'{key}) {value} \n')
    return sche






from pymongo import MongoClient
from data.config import mongodb_url


client = MongoClient(mongodb_url)

db = client["studybot"]
db_users = db.users
db_groups = db.groups
db_schedule = db.schedule
db_homework = db.homework
db_time = db.time
db_statistic = db.statistic


async def db_close():
    client.close()


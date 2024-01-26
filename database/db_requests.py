from peewee import Model, PostgresqlDatabase, CharField

# Подключение к базе данных PostgreSQL
db = PostgresqlDatabase(name='название_вашей_базы_данных',user='ваш_пользователь', password='ваш_пароль', host='localhost')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField()
    email = CharField(unique=True)

# from pymongo import MongoClient
# from data.config import mongodb_url


# client = MongoClient(mongodb_url)
# print(client)
# db = client["studybot"]
# db_schedule = db['schedule']
# db_homework = db.homework
# statistic = db.statistic


# async def db_close():
#     client.close()

# async def get_schedule(day=None, week=str):
#     if day is None: day = ["Monday","Tuesday", "Wednesday", "Thursday", "Friday"]
#     sche=''

#     for i in day:
#         sche += f"{i}: \n"
#         info = (db_schedule.find_one({"day": f"{i}:", "tags": f"{week}"},{"_id": 0, "day": 0, "tags": 0}))
#         for key, value in info.items():
#             sche += (f'{key}) {value} \n')
#         sche += ('\n')
#     return sche

# async def get_homework(day=None, week=str):
#     if day is None: day = ["Monday","Tuesday", "Wednesday", "Thursday", "Friday"]
#     sche=''

#     for i in day:
#         sche += f"{i}: \n"
#         info = (db_homework.find_one({"day": f"{i}"},{"_id": 0, "day": 0, "tags": 0}))
#         for key, value in info.items():
#             sche += (f'{key}) {value} \n')
#         sche += ('\n')
#     return sche
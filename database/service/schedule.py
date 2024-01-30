from database.db_connect import db_schedule


async def get_schedule(usr_id):
    pass

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


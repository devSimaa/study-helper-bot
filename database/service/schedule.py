from database.db_connect import db_schedule
from database.service.users import get_user


days = ["Monday","Tuesday", "Wednesday", "Thursday", "Friday"]
async def get_schedule(user_id, week):
    user = await get_user(user_id)
    schedule = db_schedule.find_one({"group": user["group"]}, {"_id": 0, f"{week}": 1})[week]
    text = ''
    for day in days:
        text += f"{day}: \n"
        for key, value in schedule[day].items():
            if value:
                text += (f'{key}) {value} \n')
        text += ('\n')

    return text

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


async def add_schedule(group_name):
    schedule = {"group": group_name}

    for week_number in range(1, 3):
        week_key = f"week{week_number}"
        schedule[week_key] = {}


        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
            day_schedule = {}

            for period in range(1, 6):
                period_key = str(period)
                day_schedule[period_key] = ""

            schedule[week_key][day] = day_schedule

    db_schedule.insert_one(schedule)
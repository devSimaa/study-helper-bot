from database.db_connect import db_groups, db_schedule


async def get_groups() -> list:
    return db_groups.find({}, {"_id": 0})

async def add_group(group_name):
    db_groups.insert_one({"group": group_name})
    db_schedule.insert_one({
    f"group": group_name,
    "week1": {
        "Monday": {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": ""
        },
        "Tuesday": {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": ""
        },
        "Wednesday": {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": ""
        },
        "Thursday": {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": ""
        },
        "Friday": {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": ""
        }
    },
    "week2": {
        "Monday": {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": ""
        },
        "Tuesday": {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": ""
        },
        "Wednesday": {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": ""
        },
        "Thursday": {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": ""
        },
        "Friday": {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": ""
        }
    }
})


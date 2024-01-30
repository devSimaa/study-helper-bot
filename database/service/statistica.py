from database.db_connect import db_statistic

# statistic.products.updateOne({ $inc: { quantity: -2, "metrics.orders": 1 })


async def statistic(name):
    db_statistic.update_one({"tags": 0},{"$inc": {f"{name}": +1}})

async def get_statistic():
    sche = ''
    list = ["Старт","Расписание","Домашнее задание","Время"]
    
    info = (db_statistic.find_one({"tags": 0},{"_id":0, "tags": 0}))
    for key, value in info.items():
        sche += (f'{key}: {value} \n')
    return sche

from .db_requests import db
from pymongo import MongoClient

db_statistic = db.statistic
# statistic.products.updateOne({ $inc: { quantity: -2, "metrics.orders": 1 })

async def statistic(name):
    db_statistic.update_one({"tags": 0},{"$inc": {f"{name}": +1}})

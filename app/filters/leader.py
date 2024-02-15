from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message
from database.service.leader import get_leader


class IsLeader(BoundFilter):
    async def check(self, message: Message):
        if int(message.from_user.id) in await get_leader():
            return True
        else:
            return False
        

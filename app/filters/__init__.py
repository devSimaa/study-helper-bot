from loader import dp
from .admin import IsAdmin
from .leader import IsLeader



if __name__ == 'bot.filters':
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsLeader)


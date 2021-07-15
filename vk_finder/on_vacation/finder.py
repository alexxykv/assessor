from .users import Users
from .user_data import UserData


def find(data):
    user_data = UserData(data)
    user_ids = Users.search(user_data)

    fields = [
        'bdate', 'city', 'connections',
        'screen_name', 'site', 'universities',
        'photo_200', 'counters'
    ]
    users_info = Users.get(user_ids, fields)

    return users_info

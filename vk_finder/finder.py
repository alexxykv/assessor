from .users import Users
from .user_data import UserData


def find(data):
    user_data = UserData(data)
    user_ids = Users.search(user_data)
    users_info = Users.get(user_ids)

    return users_info

from .api import vk
from .user_search import UserSearch


class Users:

    def __init__(self):
        pass

    @staticmethod
    def get(user_id):
        fields = [
            'bdate', 'city', 'connections',
            'screen_name', 'site', 'universities',
            'photo_200', 'counters'
        ]

        try:
            response = vk.users.get(user_ids=user_id, fields=fields)
            return response[0]
        except:
            return ''

    @staticmethod
    def search(data):
        user = UserSearch.run(data)
        return user

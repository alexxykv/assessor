from .vk import vk


class Users:

    def __init__(self):
        pass

    @staticmethod
    def search(user_data):
        fullname = user_data.get_fullname()
        users = vk.users.search(q=fullname, count=1000, **user_data.__dict__)
        user_ids = []
        for item in users['items']:
            user_ids.append(item['id'])
            
        return user_ids

    @staticmethod
    def get(user_ids):
        users = vk.users.get(user_ids=user_ids, fields=[
            'bdate', 'city', 'connections',
            'screen_name', 'site', 'universities',
            'photo_200', 'counters'
        ])

        return users

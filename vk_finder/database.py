from .vk import vk


class Database:

    def __init__(self):
        pass

    @staticmethod
    def get_city_id(q, country_id=1):
        city = vk.database.getCities(q=q, country_id=country_id)
        city_id = city['items'][0]['id']
        return city_id

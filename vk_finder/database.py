from .vk import vk


class Database:

    def __init__(self):
        pass

    @staticmethod
    def get_city_id(city, country_id=1):
        city = vk.database.getCities(q=city, country_id=country_id)
        city_id = city['items'][0]['id'] if city['items'] else 0
        return city_id
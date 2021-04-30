from .vk import vk
from .user_info import UserInfo

class VkFinder:

    def __init__(self, data):
        self.user_info = UserInfo(data)

    def get_city(self):  # Только для России(вроде) ПРОВЕРИТЬ
        clients_city = vk.database.getCities(country_id=1, q=self.user_info.city)
        return clients_city['items'][0]['id']

    def search(self):
        params = self.user_info.__dict__
        if hasattr(self.user_info, 'city')
            params['city'] = self.get_city()
        users = vk.users.search(q=self.user_info.get_fullname(), count=1000, **params)

        user_ids = []
        for item in users['items']:
            user_ids.append(items['id'])

        return user_ids

    def get(self):
        user_ids = self.search()
        users = vk.get(user_ids=user_ids, fields=[
            'bdate', 'city', 'connections',
            'screen_name', 'site', 'universities',
            'photo_200', 'counters'
        ])

        return users
    
    # def get_users(self):  # Поиск. Возвращает список idщников, пример: vk.com/id1337322 -> 1337322
    #     params = self.user_info.__dict__
    #     params['city'] = self.get_city()

    #     users = vk.users.search(q=self.user_info.get_fullname(), count=1000, **params)
    #     user_ids = []
    #     for item in users['items']:
    #         user_ids.append(item['id'])

    #     return user_ids

    # def get_nicknames(self): # вот эту штуку надо отдать Саням и сделать по ним поиск. Тут список никнеймов пользователей
    #     nicknames = []
    #     ids = ''
    #     for i in self.get_users():
    #         ids += str(i) + ','
    #     for i in vk.users.get(user_ids=ids[:len(ids) - 1], fields='screen_name'):
    #         nicknames.append(i['screen_name'])
    #     return nicknames

    # def get_information(self):
    #     users_info = []
    #     ids = ''
    #     for i in self.get_users():
    #         ids += str(i) + ','
    #     for i in vk.users.get(user_ids=ids[:len(ids) - 1],
    #                           fields='followers_count,counters,exports,site,connections'):
    #         users_info.append(i)
    #         # print(i)
    #         # print(i['first_name'], i['last_name'])
    #         # print(f'Количество друзей: {i["counters"]["friends"]}')
    #         # print(f'Количество подписчиков: {i["followers_count"]}')
    #         # print(F"Сайт: {i['site']}")
    #     return users_info

    # def print_links(self):
    #     array = []
    #     spisok_id = self.get_nickname()
    #     for id in spisok_id:
    #         array.append('vk.com/' + id)

    #     return array
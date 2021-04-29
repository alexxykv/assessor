import vk_api
from vk_finder.access_token import SUPER_SECRET_TOKEN


class VkFinder:

    def __init__(self, info):
        self.name = info['first_name']
        self.last_name = info['last_name']
        self.birth_day = info['date_birth'].timetuple()[2] if info['date_birth'] else None
        self.birth_month = info['date_birth'].timetuple()[1] if info['date_birth'] else None
        self.birth_year = info['date_birth'].timetuple()[0] if info['date_birth'] else None
        self.city = info['city']
        self.fullname = self.name + ' ' + self.last_name

    def connect(self):
        return vk_api.VkApi(token=SUPER_SECRET_TOKEN).get_api()

    def get_city(self):  # Только для России(вроде) ПРОВЕРИТЬ
        vk = self.connect()
        clients_city = vk.database.getCities(country_id=1, q=self.city)
        return clients_city['items'][0]['id']

    def get_users(self):  # Поиск. Возвращает список idщников, пример: vk.com/id1337322 -> 1337322
        vk = self.connect()
        spisok_id = []
        dict = {}
        if self.birth_day:
            dict['birth_day'] = self.birth_day
        if self.birth_month:
            dict['birth_month'] = self.birth_month
        if self.birth_year:
            dict['birth_year'] = self.birth_year
        users = vk.users.search(q=self.fullname, city=self.get_city(),
                                count=1000, **dict)
        for item in users['items']:
            spisok_id.append(str(item['id']))

        return spisok_id

    def get_nicknames(self): # вот эту штуку надо отдать Саням и сделать по ним поиск. Тут список никнеймов пользователей
        vk = self.connect()
        nicknames = []
        ids = ''
        for i in self.get_users():
            ids += str(i) + ','
        for i in vk.users.get(user_ids=ids[:len(ids) - 1], fields='screen_name'):
            nicknames.append(i['screen_name'])
        return nicknames

    def get_information(self):
        vk = self.connect()
        users_info = []
        ids = ''
        for i in self.get_users():
            ids += str(i) + ','
        for i in vk.users.get(user_ids=ids[:len(ids) - 1],
                              fields='followers_count,counters,exports,site,connections'):
            users_info.append(i)
            # print(i)
            # print(i['first_name'], i['last_name'])
            # print(f'Количество друзей: {i["counters"]["friends"]}')
            # print(f'Количество подписчиков: {i["followers_count"]}')
            # print(F"Сайт: {i['site']}")
        return users_info

    def print_links(self):
        array = []
        spisok_id = self.get_nickname()
        for id in spisok_id:
            array.append('vk.com/' + id)

        return array
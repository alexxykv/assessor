import vk_api
from vk_finder.access_token import SUPER_SECRET_TOKEN


class VkFinder:

    def __init__(self, info):
        self.name = info['first_name']
        self.last_name = info['last_name']
        self.birth_day = info['birth_day']
        self.birth_month = info['birth_month']
        self.birth_year = info['birth_year']
        self.city = info['city']

        self.fullname = self.name + ' ' + self.last_name

    def connect(self):
        return vk_api.VkApi(token=SUPER_SECRET_TOKEN).get_api()

    def get_users(self):
        vk = self.connect()
        spisok_id = []
        our_users = vk.users.search(q=self.fullname, birth_day=self.birth_day,
                                    birth_month=self.birth_month, birth_year=self.birth_year, count=1000)
        for a in our_users['items']:
            spisok_id.append(str('vk.com/id' + str(a['id'])))

        return spisok_id

# clients_city = vk.database.getCities(country_id=1, need_all=1)
# print(clients_city)
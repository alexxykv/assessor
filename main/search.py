from vk_finder.users import Users
from parsing.habr import search as hs
from parsing.github import user_searching

import requests


class Search:

    def __init__(self, data):
        self.data = data
        self.data['sites_found'] = []

    def run(self):
        if 'vk.com' not in self.data['sites']:
            self.vk()

        if 'habr.com' not in self.data['sites']:
            self.habr()

        if 'github.com' not in self.data['sites']:
            self.github()

        if 'codeforces.com' not in self.data['sites']:
            self.codeforce()

        if 'kaggle.com' not in self.data['sites']:
            self.kaggle()

    def vk(self):
        user_id, nickname = Users.search(self.data)

        if user_id or nickname:
            site = {
                'url': f'https://vk.com/id{user_id}',
                'id': user_id,
                'nickname': nickname,   
            }

            self.data['sites'].update( {'vk.com': site} )
            self.data['sites_found'].append('vk.com')

    def habr(self):
        result = {}
        # TODO добавить url в результат поиска
        url = 'https://habr.com/ru/users'
        searched_by_name = hs.Search.search_users(f"{self.data['first_name']} {self.data['last_name']}")

        for _, site in self.data['sites'].items():
            if result: break

            nickname = site['nickname']
            searched_by_nickname = hs.Search.search_users(nickname)

            if len(searched_by_nickname) > 0:
                if searched_by_nickname[0]['nickname'].lower() == nickname:
                    result.update({
                        'url': f'{url}/{nickname}/',
                        'nickname': nickname,
                    })
                    break

            for user in searched_by_name:
                if user['nickname'].lower() == nickname:
                    result.update({
                        'url': f'{url}/{nickname}',
                        'nickname': nickname,
                    })
                    break

        else:
            if len(searched_by_name) == 1:
                result.update({
                    'url': f"{url}/{searched_by_name[0]['nickname']}",
                    'nickname': searched_by_name[0]['nickname'],
                })

        if result:
            self.data['sites'].update( {'habr.com': result} )
            self.data['sites_found'].append('habr.com')

    def github(self):
        result = {}

        for _, site in self.data['sites'].items():
            if result: break

            nickname = site['nickname']
            searched_users = user_searching.srch(nickname)

            if len(searched_users) > 0:
                if searched_users[0]['nickname'].lower() == nickname:
                    result.update({
                        'url': searched_users[0]['url'],
                        'nickname': nickname,
                    })
                    break

        if result:
            self.data['sites'].update( {'github.com': result} )
            self.data['sites_found'].append('github.com')

    def codeforce(self):
        result = {}
        
        for _, site in self.data['sites'].items():
            if result: break

            nickname = site['nickname']
            response = requests.get(f'https://codeforces.com/profile/{nickname}/')

            if not response.history:
                result.update({
                    'url': response.url,
                    'nickname': nickname,
                })
                break

        if result:
            self.data['sites'].update( {'codeforces.com': result} )
            self.data['sites_found'].append('codeforces.com')

    def linkedin(self):
        pass

    def kaggle(self):
        result = {}

        for _, site in self.data['sites'].items():
            if result: break

            nickname = site['nickname']
            response = requests.get(f'https://www.kaggle.com/{nickname}/')

            if response.ok:
                result.update({
                    'url': response.url,
                    'nickname': nickname,
                })
                break
        
        if result:
            self.data['sites'].update( {'kaggle.com': result} )
            self.data['sites_found'].append('kaggle.com')

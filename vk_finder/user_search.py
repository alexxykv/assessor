from .api import vk
from .database import Database

from collections import Counter
import json


class UserSearch:

    def __init__(self):
        pass

    @staticmethod
    def run(data):
        """Takes data from form"""

        info = _data_handler(data)
        counter = Counter()

        counter.update(UserSearch._way_1(info))
        if len(counter) != 1:
            counter.update(UserSearch._way_2(info))
            counter.update(UserSearch._way_3(info))

        if len(counter) != 0:
            return counter.most_common(1)[0][0]
        return tuple(['', ''])

    @staticmethod
    def _way_1(info):
        """Search by all info. Returns list id"""

        response = vk.users.search(**info, fields=['screen_name'])
        items = response['items']
        users = []

        for item in items:
            id = item['id']
            nickname = item['screen_name']
            users.append((id, nickname))

        return users

    @staticmethod
    def _way_2(info):
        """Search by nicknames from other sites. Returns list id."""

        nicknames = info['nicknames']
        users = []

        for nickname in nicknames:
            response = vk.users.search(q=nickname, fields=['screen_name'])
            items = response['items']
            
            for item in items:
                id = item['id']
                nickname = item['screen_name']
                users.append((id, nickname))

        return users

    @staticmethod
    def _way_3(info):
        """Search by groups. Returns list id."""
        
        with open('vk_finder/resources/groups.json', 'r', encoding='utf-8') as file:
            groups = json.load(file)

        users = []

        for group in groups:
            group_id = group['id']

            response = vk.users.search(
                q=info['q'],
                group_id=group_id,
                birth_day=info['birth_day'],
                birth_month=info['birth_month'],
                fields=['screen_name']
            )
            items = response['items']

            for item in items:
                id = item['id']
                nickname = item['screen_name']
                users.append((id, nickname))

        return users

def _data_handler(data):
    """Processes data for submission to vk. Returns dict info."""

    first_name = data['first_name']
    last_name = data['last_name']
    q = f'{first_name} {last_name}'

    date_birth = data['date_birth']
    if date_birth:
        splits = date_birth.split('-')
        birth_year, birth_month, birth_day = splits
    else:
        birth_year, birth_month, birth_day = ['', '', '']

    city = data['city']
    if city:
        city = Database.get_city_id(city)
    else:
        city = ''

    nicknames = []
    for _, value in data['sites'].items():
        nickname = value['nickname']
        nicknames.append(nickname)

    info = {
        'q': q,
        'city': city,
        'birth_month': birth_month,
        'birth_day': birth_day,
        'nicknames': nicknames,
    }

    if birth_year:
        info.update({'birth_year': birth_year})

    return info

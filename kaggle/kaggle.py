import requests
import re
import json
from .user import User

class Kaggle:

    @staticmethod
    def _kaggle_dict(url):
        resp = requests.get(url)
        if resp.ok:
            text = resp.text
        else:
            return ''
        raw_json = re.search(r'{"userId":.*"userAllowsUserMessages":.*?}', text, flags=re.S).group()
        cooked_json = json.loads(raw_json)
        cooked_json['followers'].pop('list')
        cooked_json['following'].pop('list')
        return cooked_json

    @staticmethod
    def get_user(nickname):
        url = 'https://www.kaggle.com/' + nickname
        kaggle = Kaggle._kaggle_dict(url)
        print(kaggle)
        if kaggle:
            user = User(kaggle)
            return user
        return ''

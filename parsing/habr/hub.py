from .utils import get_HTMLtext, fetch
from .regex import RegexHub
from .urls import URL

class Hub:

    def __init__(self, hub_name):
        self.url = URL.hub(hub_name)
        text = get_HTMLtext(self.url)
        self.hub_name = hub_name
        self.name = self._get_name(text)
        self.rating = self._get_rating(text)

    def _get_name(self, text):
        name = fetch(RegexHub.NAME, text)
        return name[0] if name else ''

    def _get_rating(self, text):
        rating = fetch(RegexHub.RATING, text)
        return rating[0].replace(',', '.').replace('\xa0', '') if rating else ''

    @staticmethod
    def get(hub_name):
        hub = Hub(hub_name)
        return hub.__dict__

    @staticmethod
    def get_authors(hub_name):
        url = URL.hub_authors(hub_name)
        text = get_HTMLtext(url)
        authors = fetch(RegexHub.AUTHORS, text)
        contribution = fetch(RegexHub.CONTRIB_AUTHORS, text)
        result = []
        for i in range(len(authors)):
            result.append({
                'nickname': authors[i][0],
                'name': authors[i][1],
                'contribution': contribution[i].replace(',', '.').replace('\xa0', '')
            })
        return result

    @staticmethod
    def get_companies(hub_name):
        url = URL.hub_companies(hub_name)
        text = get_HTMLtext(url)
        companies = fetch(RegexHub.COMPANIES, text)
        contribution = fetch(RegexHub.CONTRIB_AUTHORS, text)
        result = []
        for i in range(len(companies)):
            result.append({
                'company': companies[i][0],
                'name': companies[i][1],
                'contribution': contribution[i].replace(',', '.').replace('\xa0', '')
            })
        return result
        
    @staticmethod
    def _get_posts(text):
        posts = fetch(RegexHub.POSTS, text)
        result = []
        for i in range(len(posts)):
            result.append({
                'type': posts[i][0],
                'id': posts[i][1],
                'title': posts[i][2]
            })
        return result

    @staticmethod
    def get_top_posts(hub_name, page=1):
        url = URL.hub_top_posts(hub_name, page)
        text = get_HTMLtext(url)
        posts = Hub._get_posts(text)
        return posts

    @staticmethod
    def get_last_posts(hub_name, page=1):
        url = URL.hub_last_posts(hub_name, page)
        text = get_HTMLtext(url)
        posts = Hub._get_posts(text)
        return posts
    
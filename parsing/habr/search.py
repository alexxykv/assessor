from .utils import get_HTMLtext, fetch
from .urls import URL
from .regex import RegexSearch


class Search:

    @staticmethod
    def search_posts(req, page=1, order_by='relevance'):
        url = URL.search(req, 'posts', page, order_by)
        text = get_HTMLtext(url)
        posts = fetch(RegexSearch.POSTS, text)
        for i in range(len(posts)):
            posts[i] = {
                'type': posts[i][0],
                'id': posts[i][1],
                'title': posts[i][2]
            }
        return posts

    @staticmethod
    def search_hubs_and_companies(req, page=1, order_by='relevance'):
        url = URL.search(req, 'hubs', page, order_by)
        text = get_HTMLtext(url)
        hubs = fetch(RegexSearch.HUBS, text)
        hub_subs = fetch(RegexSearch.HUB_SUBS, text)
        hub_rating = fetch(RegexSearch.HUB_RATING, text)
        result = []
        for i in range(len(hubs)):
            result.append({
                'name': hubs[i],
                'subs': hub_subs[i].replace('\xa0', '').replace(',', '.'),
                'rating': hub_rating[i].replace('\xa0', '').replace(',', '.')
            })
        return result

    @staticmethod
    def search_users(req, page=1, order_by='relevance'):
        url = URL.search(req, 'users', page, order_by)
        text = get_HTMLtext(url)
        users_name = fetch(RegexSearch.USER_NAME, text)
        users_nickname = fetch(RegexSearch.USER_NICKNAME, text)
        result = []
        for i in range(len(users_nickname)):
            result.append({
                'name': users_name[i],
                'nickname': users_nickname[i]
            })
        return result

    @staticmethod
    def search_comments(req, page=1, order_by='relevance'):
        pass

from .utils import fetch, get_text
from .comment import Comment
from .regex import RegexUser
from .urls import URL


class User:
    def __init__(self, nickname):
        self.url = URL.user_profile(nickname)
        text = get_text(self.url)
        self.nickname = nickname
        self.name = self._get_name(text)
        self.specialization = self._get_specialization(text)
        self.dob = self._get_dob(text)
        self.registered = self._get_registered(text)
        self.activity = self._get_activity(text)
        self.ranked = self._get_ranked(text)
        self.city = self._get_city(text)
        self.region = self._get_region(text)
        self.country = self._get_country(text)
        self.city = self._get_city(text)
        self.region = self._get_region(text)
        self.country = self._get_country(text)
        self.stats = self._get_stats(text)
        self.work = self._get_work(text)
        self.hubs = self._get_hubs(text)
        self.companies = self._get_companies(text)
        self.contribution = self._get_contribution(text)
        # self.posts = User.get_posts(self.nickname)
        # self.comments = User.get_comments(self.nickname)
        # self.favorites = User.get_favorites(self.nickname)

    def _get_name(self, text):
        name = fetch(RegexUser.NAME, text)
        return name[0] if name else ''

    def _get_nickname(self, text):
        nickname = fetch(RegexUser.NICKNAME, text)
        return nickname[0] if nickname else ''

    def _get_specialization(self, text):
        specialization = fetch(RegexUser.SPECIALIZATION, text)
        return specialization[0] if specialization else ''

    def _get_dob(self, text):
        dob = fetch(RegexUser.DOB, text)
        return dob[0] if dob else ''

    def _get_registered(self, text):
        registered = fetch(RegexUser.REGISTERED, text)
        return registered[0] if registered else ''

    def _get_activity(self, text):
        activity = fetch(RegexUser.ACTIVITY, text)
        return activity[0] if activity else ''

    def _get_ranked(self, text):
        ranked = fetch(RegexUser.RANKED, text)
        return ranked[0] if ranked else ''

    def _get_city(self, text):
        city = fetch(RegexUser.CITY, text)
        return city[0] if city else ''

    def _get_region(self, text):
        region = fetch(RegexUser.REGION, text)
        return region[0] if region else ''

    def _get_country(self, text):
        country = fetch(RegexUser.COUNTRY, text)
        return country[0] if country else ''

    def _get_stats(self, text):
        stats = fetch(RegexUser.STATS, text)
        return {
            'karma': stats[0].replace(',', '.').replace('\xa0', ''),
            'rating': stats[1].replace(',', '.').replace('\xa0', ''),
            'followers': stats[2], 'following': stats[3]
        } if stats else ''

    def _get_work(self, text):
        work = fetch(RegexUser.WORK, text)
        return {
            'url': URL.company(work[0][0]),
            'name': work[0][1]
        } if work else ''

    def _get_hubs(self, text):
        hubs = fetch(RegexUser.HUBS, text)
        for i in range(len(hubs)):
            hubs[i] = {
                'url': hubs[i][0],
                'name': hubs[i][1]
            }
        return hubs

    def _get_companies(self, text):
        companies = fetch(RegexUser.COMPANIES, text)
        for i in range(len(companies)):
            companies[i] = {
                'url': companies[i][0],
                'name': companies[i][1]
            }
        return companies

    def _get_contribution(self, text):
        contrib_url = fetch(RegexUser.CONTRIB_URL, text)
        contrib_name = fetch(RegexUser.CONTRIB_NAME, text)
        contrib_value = fetch(RegexUser.CONTRIB_VALUE, text)

        contrib = []
        for i in range(len(contrib_url)):
            contrib.append({
                'url': contrib_url[i],
                'name': contrib_name[i],
                'value': contrib_value[i]
            })
        return contrib

    @staticmethod
    def get(nickname):
        user = User(nickname)
        return user.__dict__
    
    @staticmethod
    def get_posts(nickname, page=1):
        url = URL.user_posts(nickname, page)
        text = get_text(url)
        posts = fetch(RegexUser.POSTS, text)
        for i in range(len(posts)):
            posts[i] = {
                'type': posts[i][0],
                'id': posts[i][1],
                'title': posts[i][2]
            }
        return posts

    @staticmethod
    def get_comments(nickname, page=1):
        url = URL.user_comments(nickname, page)
        text = get_text(url)
        comments = Comment._get(text)
        return comments

    @staticmethod
    def get_favorites(nickname, page=1):
        url = URL.user_favorites(nickname, page)
        text = get_text(url)
        favorites = fetch(RegexUser.POSTS, text)
        for i in range(len(favorites)):
            favorites[i] = {
                'type': favorites[i][0],
                'url': favorites[i][1],
                'title': favorites[i][2]
            }
        return favorites

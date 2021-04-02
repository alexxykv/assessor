from . import regex
from .utils import fetch, get_text
from .urls import URL


class User:
    def __init__(self, url):
        text = get_text(url)

        self.url = url
        
        name = fetch(regex.NAME, text)
        if name: 
            self.name = name[0]

        self.nickname = fetch(regex.NICKNAME, text)[0]
        self.specialization = fetch(regex.SPEC, text)[0]

        dates = fetch(regex.DATES, text)
        self.registered = dates.pop()
        if len(dates) != 0:
            self.dob = dates.pop()

        ranked = fetch(regex.RANKED, text)
        if ranked: 
            self.ranked = ranked[0]
        
        city = fetch(regex.CITY, text)
        if city:
            self.city = city[0]

        region = fetch(regex.REGION, text)
        if region:
            self.region = region[0]

        country = fetch(regex.COUNTRY, text)
        if country:
            self.country = country[0]

        activity = fetch(regex.ACTIVITY, text)[0].split(', ')
        date = activity[0].split('.')
        time = activity[1].split(':')
        self.activity = {
            'day': date[0], 'month': date[1], 'year': date[2],
            'hours': time[0], 'minutes': time[1]
        }

        stats = fetch(regex.STATS, text)
        if stats:
            self.stats = {
                'karma': stats[0], 'rating': stats[1],
                'followers': stats[2], 'following': stats[3]
            }

        work = fetch(regex.WORK, text)
        if work:
            self.work = {
                'url': URL._habr + work[0][0],
                'name': work[0][1]
            }
        
        self.hubs = fetch(regex.USER_HUBS, text)
        for i in range(len(self.hubs)):
            self.hubs[i] = {
                'url': self.hubs[i][0],
                'name': self.hubs[i][1]
            }

        self.companies = fetch(regex.COMPANIES, text)
        for i in range(len(self.companies)):
            self.companies[i] = {
                'url': self.companies[i][0],
                'name': self.companies[i][1]
            }
        
        self.contribution = fetch(regex.CONTRIB, text)
        contrib_link = fetch(regex.CONTRIB_LINK, text)
        for i in range(len(self.contribution)):
            self.contribution[i] = {
                'url': contrib_link[i],
                'name': self.contribution[i][0],
                'value': self.contribution[i][1]
            }

        url_user_posts = URL.user_posts(self.nickname)
        text_user_posts = get_text(url_user_posts)
        self.posts = fetch(regex.POSTS, text_user_posts)
        for i in range(len(self.posts)):
            self.posts[i] = {
                'url': self.posts[i][0],
                'title': self.posts[i][1]
            }

        url_user_comments = URL.user_comments(self.nickname)
        text_user_comments = get_text(url_user_comments)
        self.comments = fetch(regex.USER_COMMENTS, text_user_comments)

        url_user_favorites = URL.user_favorites(self.nickname)
        text_user_comments = get_text(url_user_favorites)
        self.favorites = fetch(regex.POSTS, text_user_comments)
        for i in range(len(self.favorites)):
            self.favorites[i] = {
                'url': self.favorites[i][0],
                'title': self.favorites[i][1]
            }

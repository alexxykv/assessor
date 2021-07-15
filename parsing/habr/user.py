from .comment import Comment
from .regex import RegexUser
from .urls import URL
from .utils import (
    fetch, get_HTMLtext, stats_handler,
    convert_to_number, views_handler,
    coms_count_handler, voitings_handler
)


class User:
    def __init__(self, nickname):
        self.url = URL.user_profile(nickname)
        text = get_HTMLtext(self.url)

        self.nickname = self._get_nickname(text)
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
        self.contributions = self._get_contributions(text)
        # self.posts = User.get_posts(self.nickname)
        # self.comments = User.get_comments(self.nickname)
        # self.favorites = User.get_favorites(self.nickname)

    def _get_name(self, text):
        fetched_name = fetch(RegexUser.NAME, text)
        if fetched_name:
            name = fetched_name[0]
            return name
        else:
            return ''

    def _get_nickname(self, text):
        fetched_nickname = fetch(RegexUser.NICKNAME, text)
        if fetched_nickname:
            nickname = fetched_nickname[0]
            return nickname
        else:
            return ''

    def _get_specialization(self, text):
        fetched_specialization = fetch(RegexUser.SPECIALIZATION, text)
        if fetched_specialization:
            specialization = fetched_specialization[0]
            return specialization
        else:
            return ''

    def _get_dob(self, text):
        fetched_dob = fetch(RegexUser.DOB, text)
        if fetched_dob:
            dob = fetched_dob[0]
            return dob
        else:
            return ''

    def _get_registered(self, text):
        fetched_registered = fetch(RegexUser.REGISTERED, text)
        if fetched_registered:
            registered = fetched_registered[0]
            return registered
        else:
            return ''

    def _get_activity(self, text):
        fetched_activity = fetch(RegexUser.ACTIVITY, text)
        if fetched_activity:
            activity = fetched_activity[0]
            return activity
        else:
            return ''

    def _get_ranked(self, text):
        fetched_rank = fetch(RegexUser.RANKED, text)
        if fetched_rank:
            rank = int(fetched_rank[0])
            return rank
        else:
            return ''

    def _get_city(self, text):
        fetched_city = fetch(RegexUser.CITY, text)
        if fetched_city:
            city = fetched_city[0]
            return city
        else:
            return ''

    def _get_region(self, text):
        fetched_region = fetch(RegexUser.REGION, text)
        if fetched_region:
            region = fetched_region[0]
            return region
        else:
            return ''

    def _get_country(self, text):
        fetched_country = fetch(RegexUser.COUNTRY, text)
        if fetched_country:
            country = fetched_country[0]
            return country
        else:
            return ''

    def _get_stats(self, text):
        fetched_stats = fetch(RegexUser.STATS, text)
        if fetched_stats:
            karma, rating, followers, following = stats_handler(fetched_stats)
            stats = {
                'karma': round(karma),
                'rating': round(rating),
                'followers': followers,
                'following': following,
            }

            return stats
        else:
            return { 'karma': 0, 'rating': 0, 'followers': 0, 'following': 0 }

    def _get_work(self, text):
        fetched_work_name = fetch(RegexUser.WORK_NAME, text)
        fetched_work_alias = fetch(RegexUser.WORK_ALIAS, text)

        if fetched_work_name and fetched_work_alias:
            name = fetched_work_name[0]
            alias = fetched_work_alias[0]
            url = URL.company(alias)
            work = {
                'url': url,
                'name': name,
                'alias': alias,
            }

            return work
        else:
            return {}

    def _get_hubs(self, text):
        fetched_hub_names = fetch(RegexUser.HUB_NAMES, text)
        fetched_hub_aliases = fetch(RegexUser.HUB_ALIAS, text)
        fetched_hubs = zip(fetched_hub_names, fetched_hub_aliases)
        hubs = []

        for name, alias in fetched_hubs:
            url = URL.hub(alias)
            hub = {
                'url': url,
                'name': name,
                'alias': alias,
            }

            hubs.append(hub)

        return hubs

    def _get_companies(self, text):
        fetched_company_names = fetch(RegexUser.COMPANY_NAME, text)
        fetched_company_aliases = fetch(RegexUser.COMPANY_ALIAS, text)
        fetched_companies = zip(
            fetched_company_names,
            fetched_company_aliases
        )
        companies = []

        for name, alias in fetched_companies:
            url = URL.company(alias)
            company = {
                'url': url,
                'name': name,
                'alias': alias,
            }

            companies.append(company)

        return companies

    def _get_contributions(self, text):
        fetched_contrib_names = fetch(RegexUser.CONTRIB_NAME, text)
        fetched_contrib_aliases = fetch(RegexUser.CONTRIB_ALIAS, text)
        fetched_contrib_values = fetch(RegexUser.CONTRIB_VALUE, text)
        fetched_contribs = zip(
            fetched_contrib_names,
            fetched_contrib_aliases,
            fetched_contrib_values
        )
        contribs = []

        for name, alias, value in fetched_contribs:
            url = URL.hub(alias)
            contrib = {
                'url': url,
                'name': name,
                'alias': alias,
                'value': convert_to_number(value),
            }

            contribs.append(contrib)

        return contribs

    def _get_posts(self, text):
        fetched_post_id = fetch(RegexUser.POST_ID, text)
        fetched_post_type = fetch(RegexUser.POST_TYPE, text)
        fetched_post_title = fetch(RegexUser.POST_TITLE, text)
        fetched_post_voitings = fetch(RegexUser.POST_VOITINGS, text)
        fetched_post_views = fetch(RegexUser.POST_VIEWS, text)
        fetched_post_favs_count = fetch(RegexUser.POST_FAVS_COUNT, text)
        fetched_post_coms_count = fetch(RegexUser.POST_COMS_COUNT, text)
        fetched_posts = zip(
            fetched_post_id,
            fetched_post_type,
            fetched_post_title,
            fetched_post_voitings,
            fetched_post_views,
            fetched_post_favs_count,
            fetched_post_coms_count
        )
        posts = []

        for (id, type, title, voitings,
             views, favs_cnt, coms_cnt) in fetched_posts:
            url = URL.post(id)
            post = {
                'url': url,
                'type': type,
                'title': title,
                'voitings': voitings_handler(voitings),
                'views': views_handler(views) / 1000,
                'favs_count': int(favs_cnt),
                'coms_count': coms_count_handler(coms_cnt),
                # TODO add tags
            }

            posts.append(post)

        return posts

    def _get_comments(self, text):
        fetched_com_id = fetch(RegexUser.COM_ID, text)
        fetched_com_post_id = fetch(RegexUser.COM_POST_ID, text)
        fetched_com_time = fetch(RegexUser.COM_TIME, text)
        fetched_com_voitings = fetch(RegexUser.COM_VOITINGS, text)
        fetched_coms = zip(
            fetched_com_id,
            fetched_com_post_id,
            fetched_com_time,
            fetched_com_voitings
        )
        coms = []

        for (id, post_id, time, voitings) in fetched_coms:
            url = URL.comment(id, post_id)
            com = {
                'url': url,
                'id': id,
                'post_id': post_id,
                'time': time,
                'voitings': voitings_handler(voitings),
            }

            coms.append(com)

        return coms

    def get(self):
        dictionary = self.__dict__
        return dictionary

    def get_posts(self, page=1):
        url = URL.user_posts(self.nickname, page)
        text = get_HTMLtext(url)

        posts = self._get_posts(text)
        return posts

    def get_comments(self, page=1):
        url = URL.user_comments(self.nickname, page)
        text = get_HTMLtext(url)

        comments = self._get_comments(text)
        return comments

    def get_favorites(self, page=1):
        url = URL.user_favorites(self.nickname, page)
        text = get_HTMLtext(url)

        favorites = self._get_posts(text)
        return favorites

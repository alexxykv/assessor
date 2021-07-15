from parsing import habr
from parsing.github import gitpars
from parsing.codeforces import codeforces
from linkedin_api import Linkedin
from vk_finder.users import Users

from .calculate import Calculate
from .metrics import Metrics
import os


class Processor:

    def __init__(self, data):
        self.data = data
        self.result = {}

        # self.found = {}
        # self.done = []

    def run(self):
        do = {
            'habr.com': self.habr,
            'github.com': self.github,
            'linkedin.com': self.linkedin,
            'codeforces.com': self.codeforces,
            'vk.com': self.vk,
        }

        sites = self.data['sites']

        for site in sites:
            alias = site.split('.')[0]
            self.result[alias] = do[site]()

    def habr(self):
        nickname = self.data['sites']['habr.com']['nickname']
        user = habr.User(nickname)
        result = {}
        
        user_info = user.get()
        result.update(user_info)

        user_posts = user.get_posts()
        result.update( {'posts': user_posts} )

        avg_all = Metrics.HABR_AVG_ALL
        result.update( {'avg_all': avg_all} )

        avg_own = {}
        avg_contributions = Calculate.avg_habr_contributions(user.contributions)
        avg_posts = Calculate.avg_habr_posts(user_posts)

        avg_own.update( {'contribs': avg_contributions} )
        avg_own.update(avg_posts)
        result.update( {'avg_own': avg_own} )

        analysis = Calculate.habr_analysis(user_info, avg_own, avg_all)
        result.update( {'analysis': analysis} )

        ratio = Calculate.habr_evaluation(user_info, avg_own, avg_all)
        result.update( {'ratio': ratio} )
        
        return result

    def github(self):
        url = self.data['sites']['github.com']['url']
        user = gitpars.GithubParser(url)

        avg_all = Metrics.GIT_AVG_ALL

        result = {
            'avg_values': avg_all,
            'data_lang': user.languages,
            'nick': user.nickname,
            'user_repos': user.user_repos,
            'forked_repos': user.forked_repos,
            'count_all_repos': len(user.user_repos) + len(user.forked_repos),
            'count_forked_repos': len(user.forked_repos),
            'count_user_repos': len(user.user_repos),
            'count_fork': len(user.forked_repos),
            'count_lang': len(user.languages),
            'followers': user.followers,
            'stars': user.stars,
            'profile_url': user.url,
            'contributions_year': user.average_contributions(3),
            'photo': user.photo
        }

        analysis = Calculate.git_analysis(user, avg_all)
        result.update( {'analysis': analysis} )

        ratio = Calculate.git_evaluation(user, avg_all)
        result.update( {'ratio': ratio} )

        return result

    def linkedin(self):
        url = self.data['sites']['linkedin.com']['url']
        nickname = self.data['sites']['linkedin.com']['nickname']

        login = os.environ.get('LINKEDIN_LOGIN')
        password = os.environ.get('LINKEDIN_PASSWORD')
        api = Linkedin(login, password)
        
        result = {}

        profile = api.get_profile(nickname)
        result.update(profile)

        contact = api.get_profile_contact_info(nickname)
        result.update(contact)

        network = api.get_profile_network_info(nickname)
        result.update(network)

        skills = api.get_profile_skills(nickname)
        result.update( {'skills': skills} )

        result.update( {'url': url} )

        return result

    def codeforces(self):
        nickname = self.data['sites']['codeforces.com']['nickname']
        api = codeforces.Codeforce()
        result = {}

        user = api.user_info([nickname])
        result.update( {'user': user[0]} )

        blogs = api.user_blog_entries(nickname)
        result.update( {'blogs': blogs} )

        return result


    def vk(self):
        user_id, user_nickname = ['', '']

        if 'id' not in self.data['sites']['vk.com']:
            user_nickname = self.data['sites']['vk.com']['nickname']
        else:
            user_id = self.data['sites']['vk.com']['id']

        user_info = Users.get(user_id or user_nickname)

        return user_info

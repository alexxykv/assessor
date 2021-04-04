import re
from parsing.github import gitpars
from parsing.habr.user import User


class CheckUrl:
    def __init__(self, sites):
        self.sites = sites
        self.url = ''
        self.result = {}

    def check(self):
        pars_dict = {'github.com': self.github, 'habr.com': self.habr}
        for i in range(0, len(self.sites)):
            self.url = self.sites[i]
            domen = re.findall(r'//([^/]*\.[^/:]+)', self.url)[0]
            self.result[domen] = pars_dict[domen]()
        return self.result

    def github(self):
        return gitpars.GithubParser(self.url)

    def habr(self):
        nick = self.url.split('/')[-2]
        return User.get(nick)
import re
from parsing.habr import parser
from parsing.github import gitpars
import json


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
        return json.loads(parser.get_user(self.url))
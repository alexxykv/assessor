import re
from parsing.github import gitpars


class CheckUrl:
    def __init__(self, sites, sherlock):
        self.sites = sites
        self.url = ''
        self.result = {}
        self.sherlock = sherlock

    def check(self):
        pars_dict = {'github.com': self.github, 'habr.com': self.habr, 'www.linkedin.com': self.linkedin,
                     'codeforces.com': self.codeforces}
        for i in range(0, len(self.sites)):
            self.url = self.sites[i]
            domen = re.findall(r'//([^/]*\.[^/:]+)', self.url)[0]
            self.result[domen] = pars_dict[domen]() if domen in pars_dict else None
        if self.sherlock:
            for i in self.sherlock.items():
                self.url = i[1]
                if i[0] == 'GitHub' and 'github.com' not in self.result:
                    self.result['github.com'] = pars_dict['github.com']()
                if i[0] == 'habr' and 'habr.com' not in self.result:
                    self.result['habr.com'] = pars_dict['habr.com']()
        return self.result

    def codeforces(self):
        url = (self.url + '/').replace('//', '/')
        nick = url.split('/')[-2]
        return nick

    def linkedin(self):
        url = (self.url + '/').replace('//', '/')
        nick = url.split('/')[-2]
        return nick

    def github(self):
        return gitpars.GithubParser(self.url)

    def habr(self):
        url = (self.url + '/').replace('//', '/')
        nick = url.split('/')[-2]
        return nick

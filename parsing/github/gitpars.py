import requests
import json
import math
import datetime
import bs4
from parsing.github import request_construct as rc

class GithubParser:

    def __init__(self, url):
        self.url = url
        self.nickname = url.replace('\\', '/').split('/')[-1]
        self.main_page = json.loads(rc.auth_get(f"https://api.github.com/users/{self.nickname}").text)
        self.all_repos = []
        self.user_repos = []
        self.forked_repos = []
        self.__fetch_repos()
        self.stars = self.__stars()
        self.followers = self.__followers()
        self.languages = self.__languages()
        self.company = self.main_page['company']
        self.photo = self.main_page["avatar_url"]
        self.name = self.main_page["name"]
        self.hireable = True if self.main_page["hireable"] else False
        self.bio = self.main_page["bio"]
        self.created_at = self.main_page["created_at"]

    def __stars(self):
        return sum(list(map(lambda x: x['stargazers_count'], self.user_repos)))

    def __followers(self):
        return self.main_page['followers']

    def __languages(self):
        languages = {}
        n = 0
        for rep in self.user_repos:
            for l, c in json.loads(rc.auth_get(rep["languages_url"]).text).items():
                if l not in languages.keys():
                    languages[l] = c
                else:
                    languages[l] += c
                n += c
        res = {}
        for l, c in languages.items():
            percents = c/n * 100
            if percents < 5:
                if "Other" not in res.keys():
                    res["Other"] = 0
                res["Other"] += percents
            else:
                res[l] = percents
        return res

    def __organizations(self):
        js = json.loads(rc.auth_get(f"https://api.github.com/users/{self.nickname}/orgs").text)
        return list(map(lambda x: x['login'], js))

    def __fetch_repos(self):
        i = 1
        max_pages = math.ceil(self.main_page["public_repos"] / 100)
        while i <= max_pages:
            repos = json.loads(rc.auth_get(f"https://api.github.com/users/{self.nickname}/repos?page={i}&per_page=100").text)
            if len(repos) == 0:
                break
            self.all_repos += repos
            self.user_repos += list(filter(lambda x: not x['fork'], repos))
            self.forked_repos += list(filter(lambda x: x['fork'], repos))
            i += 1

    def __fetch_contributions(self, n):
        n = min([datetime.datetime.now().year - int(self.created_at[:4]) + 1, n])
        year = datetime.datetime.now().year
        contributions = []
        for i in range(n):
            page = requests.get(
                f"https://github.com/{self.nickname}?tab=overview&from={year - i}-12-01&to={year - i}-12-31").text
            page = bs4.BeautifulSoup(page, features="html.parser")
            text = page.find("h2", {'class': "f4 text-normal mb-2"}).text
            text = text.replace("\n", "")
            text = text.replace(',', '')
            num = list(filter(lambda x: x.isdigit(), text.split(' ')))[0]
            contributions.append(int(num))
        return contributions

    def average_contributions(self, n):
        now_month = datetime.datetime.now().month
        contributions = self.__fetch_contributions(n)
        for i in range(len(contributions)):
            contributions[i] = round(contributions[i] / (now_month if i == 0 else 12))
        if len(contributions) < 3:
            contributions += [0] * (3 - len(contributions))
        return contributions

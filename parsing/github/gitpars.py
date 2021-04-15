import requests
import json
import math
from parsing.github import request_construct as rc



class GithubParser:

    def __init__(self, url):
        self.profile_url = url
        self.nickname = url.replace('\\', '/').split('/')[-1]
        self.main_page = json.loads(rc.auth_get(f"https://api.github.com/users/{self.nickname}").text)
        self.all_repos = []
        self.user_repos = []
        self.forked_repos = []
        self.fetch_repos()

    def stars(self):
        return sum(list(map(lambda x: x['stargazers_count'], self.user_repos)))

    def followers(self):
        return self.main_page['followers']

    def languages(self):
        languages = {}
        n = 0
        for rep in self.user_repos:
            for l, c in json.loads(requests.get(rep["languages_url"]).text).items():
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

    def photo(self):
        return self.main_page["avatar_url"]

    def organizations(self):
        js = json.loads(rc.auth_get(f"https://api.github.com/users/{self.nickname}/orgs").text)
        return list(map(lambda x: x['login'], js))

    def fetch_repos(self):
        i = 1
        max_pages = math.ceil(self.main_page["public_repos"] / 100)
        while i <= max_pages:
            repos = json.loads(rc.auth_get(f"https://api.github.com/users/{self.nickname}/repos?page={i}&per_page=100").text)
            if len(repos) == 0:
                break
            self.all_repos += repos
            self.user_repos += list(filter(lambda x: not x['fork'], repos))
            self.forked_repos += list(filter(lambda x: x['fork'], repos))
            i+=1

    def limit(self):
        return rc.auth_get("https://api.github.com/rate_limit").text

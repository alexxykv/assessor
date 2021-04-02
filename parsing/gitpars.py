import requests
import json
import math


class GithubParser:

    def __init__(self, url):
        self.nickname = url.replace('\\', '/').split('/')[-1]
        self.main_page = json.loads(requests.get(f"https://api.github.com/users/{self.nickname}").text)
        self.repos = []
        self.fetch_repos()

    def followers(self):
        return self.main_page['followers']

    def user_repos(self):
        return list(filter(lambda x: not x['fork'], self.repos))

    def languages(self):
        languages = {}
        n = 0
        for rep in self.user_repos():
            for l, c in json.loads(requests.get(rep["languages_url"]).text).items():
                if l not in languages.keys():
                    languages[l] = c
                else:
                    languages[l] += c
                n += c
        res = []
        for l, c in languages.items():
            res.append((l, c/n * 100))
        return res

    def fetch_repos(self):
        i = 1
        max_pages = math.ceil(self.main_page["public_repos"] / 100)
        while i <= max_pages:
            repos = json.loads(requests.get(f"https://api.github.com/users/{self.nickname}/repos?page={i}&per_page=100").text)
            if len(repos) == 0:
                break
            self.repos += repos
            i+=1

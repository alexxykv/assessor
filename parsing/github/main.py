from parsing.github import gitpars
import requests


chel = gitpars.GithubParser("https://api.github.com/users/ash2k")
print(chel.stars())
print(chel.followers())
print(len(chel.user_repos))
print(len(chel.forked_repos))
print(len(chel.all_repos))
print(chel.organizations())


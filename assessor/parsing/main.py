import gitpars
import requests

chel = gitpars.GithubParser("https://github.com/ash2k")
print(chel.languages())
print(chel.user_repos())


from parsing.github.api_token import SUPER_SECRET_TOKEN
import requests as r

def auth_get(url):
    return r.get(url, headers={"Authorization" : f"token {SUPER_SECRET_TOKEN}"})
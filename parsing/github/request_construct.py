from parsing.github.api_token import SUPER_SECRET_TOKEN
import requests as r
import json


def auth_get(url):
    return r.get(url, headers={"Authorization" : f"token {SUPER_SECRET_TOKEN}"})

def check_limit():
    return auth_get("https://api.github.com/rate_limit").text

def get_json_resp(url):
	resp = auth_get(url)
	return json.loads(resp.text)

# def auth_get(url):
#     return r.get(url, headers={"Authorization" : f"token {SUPER_SECRET_TOKEN}"})
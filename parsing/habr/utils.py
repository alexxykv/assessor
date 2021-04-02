import re
import requests


def fetch(regex, text):
    data = re.findall(regex, text)
    return data


def get_text(url):
    text = requests.get(url).text
    return text

from . import regex
from .utils import fetch, get_text
from .urls import URL

class Post:
    def __init__(self, url):
        text = get_text(url)

        self.url = url
        self.id = url.split('/')[-2]
        self.author = fetch(regex.AUTHOR, text)[0]
        self.voitings = fetch(regex.VOITINGS, text)[0]
        self.favs_count = fetch(regex.FAVS_COUNT, text)[0]
        self.views = fetch(regex.VIEWS, text)[0]
        self.com_count = fetch(regex.COM_COUNT, text)[0]
        self.tags = fetch(regex.TAGS, text)

        self.hubs = fetch(regex.POST_HUBS, text)
        for i in range(len(self.hubs)):
            self.hubs[i] = {
                'url': self.hubs[i][0],
                'name': self.hubs[i][1]
            }

        self.comments = fetch(regex.POST_COMMENTS, text)
        for i in range(len(self.comments)):
            self.comments[i] = URL.post_comment(self.id, self.comments[i])
        
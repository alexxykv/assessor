from .utils import fetch, get_text
from .comment import Comment
from .regex import RegexPost
from .urls import URL

class Post:
    def __init__(self, post_id):
        self.url = URL.post(post_id)
        text = get_text(self.url)
        self.post_id = post_id
        self.author = self._get_author(text)
        self.time = self._get_time(text)
        self.voitings = self._get_voitings(text)
        self.favs_count = self._get_favs_count(text)
        self.views = self._get_views(text)
        self.comments_count = self._get_comments_count(text)
        self.tags = self._get_tags(text)
        self.hubs = self._get_hubs(text)
        self.comments = self._get_comments(text)

    def _get_author(self, text):
        author = fetch(RegexPost.AUTHOR, text)
        return author[0] if author else ''

    def _get_time(self, text):
        time = fetch(RegexPost.TIME, text)
        return time[0] if time else ''

    def _get_voitings(self, text):
        voitings = fetch(RegexPost.VOITINGS, text)
        return voitings[0] if voitings else ''

    def _get_favs_count(self, text):
        favs_count = fetch(RegexPost.FAVS_COUNT, text)
        return favs_count[0] if favs_count else ''

    def _get_views(self, text):
        views = fetch(RegexPost.VIEWS, text)
        return views[0] if views else ''

    def _get_comments_count(self, text):
        comments_count = fetch(RegexPost.COMMENTS_COUNT, text)
        return comments_count[0] if comments_count else ''

    def _get_tags(self, text):
        tags = fetch(RegexPost.TAGS, text)
        return tags

    def _get_hubs(self, text):
        hubs = fetch(RegexPost.HUBS, text)
        for i in range(len(hubs)):
            hubs[i] = {
                'url': hubs[i][0],
                'name': hubs[i][1]
            }
        return hubs

    def _get_comments(self, text):
        comments = Comment._get(text)
        return comments

    @staticmethod
    def get(post_id):
        post = Post(post_id)
        return post.__dict__
    
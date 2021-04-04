from .regex import RegexComment
from .utils import fetch
from .urls import URL

class Comment:

    def __init__(comment_id):
        pass

    @staticmethod
    def _get(text):
        comments_id = fetch(RegexComment.ID, text)
        author = fetch(RegexComment.AUTHOR, text)
        post_id = fetch(RegexComment.POST_ID, text)
        time = fetch(RegexComment.TIME, text)
        voitings = fetch(RegexComment.VOITINGS, text)
        comments = []
        for i in range(len(comments_id)):
            comments.append({
                'id': comments_id[i],
                'author': author[i],
                'time': time[i],
                'voitings': voitings[i]
            })
            if post_id:
                comments[i]['post_id'] = post_id[i]
        return comments

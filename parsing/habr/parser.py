import json
from .user import User
from .post import Post


def get_user(url):
    user = User(url)
    return json.dumps(user.__dict__)


def get_post(url):
    post = Post(url)
    return json.dumps(post.__dict__)

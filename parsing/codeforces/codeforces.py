import requests
import json
from utils import drop_tags


class Codeforce:
    """
    Class for accessing the Codeforce API.
    """

    API = 'https://codeforces.com/api/'
    USER_AGENT = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) ' +
                 'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                 'Chrome/39.0.2171.95 Safari/537.36')

    def __init__(self):
        """Initialization"""
        
        self.session = requests.Session();
        self.session.headers = {
            'User-Agent': Codeforce.USER_AGENT,
        }

    def _get(self, method_name: str, params: dict):
        """
        GET request to codeforces API.

        `method_name`: Method API name
        `params`: params
        """

        req = Codeforce.API + method_name
        res = self.session.get(req, params=params)

        dict = json.loads(res.text)
        status = dict['status']

        if status == 'OK':
            result = dict['result']
            return result
        elif status == 'FAILED':
            comment = dict['comment']

            if comment.startswith('handles'):
                raise HandleNotFound(comment)
            elif comment.startswith('blogEntryId'):
                raise BlogEntryIdNotFound(comment)

    def user_info(self, handles: list):
        """
        Returns information about one or more users.

        `handles`: A list of handles. You can transfer up to 10,000 handles.
        """

        method_name = 'user.info'
        params = {
            'handles': ';'.join(handles),
        }

        try:
            res = self._get(method_name, params)
            return res
        except HandleNotFound:
            return []

    def user_blog_entries(self, handle: str):
        """
        Returns a list of the specified user's blog entries.

        `handle`: Codeforces user handle.
        """

        method_name = 'user.blogEntries'
        params = {
            'handle': handle,
        }

        try:
            res = self._get(method_name, params)
            return res
        except HandleNotFound:
            return []

    def user_rating(self, handle: str):
        """
        Returns the rating history of the specified user.

        `handle`: Codeforces user handle.
        """

        method_name = 'user.rating'
        params = {
            'handle': handle,
        }

        try:
            res = self._get(method_name, params)
            return res
        except HandleNotFound:
            return []

    def blog_entry_view(self, blog_entry_id):
        """
        Returns a blog entry.

        `blog_entry_id`: Id of the blog entry.
        """

        method_name = 'blogEntry.view'
        params = {
            'blogEntryId': blog_entry_id,
        }

        try:
            res = self._get(method_name, params)

            # drop tag <p>...</p>
            title = res['title']
            res['title'] = drop_tags(title)
            # add url to result
            res['url'] = self.get_blog_url(blog_entry_id)

            return res
        except HandleNotFound:
            return []

    def get_blog_url(self, blog_entry_id):
        """
        Returns a link to the blog.

        `blog_entry_id`: Id of the blog entry.
        """

        main_url = 'https://codeforces.com/blog/entry/'
        blog_url = main_url + str(blog_entry_id)

        return blog_url

class HandleNotFound(Exception):
    pass

class BlogEntryIdNotFound(Exception):
    pass

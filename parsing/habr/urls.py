class URL:
    _habr = 'https://habr.com/ru'

    @staticmethod
    def user_profile(nickname):
        return f'{URL._habr}/users/{nickname}/'

    @staticmethod
    def user_posts(nickname, page):
        return f'{URL._habr}/users/{nickname}/posts/page{page}/'

    @staticmethod
    def user_comments(nickname, page):
        return f'{URL._habr}/users/{nickname}/comments/page{page}/'

    @staticmethod
    def user_favorites(nickname, page):
        return f'{URL._habr}/users/{nickname}/favorites/page{page}/'

    @staticmethod
    def post(post_id):
        return f'{URL._habr}/post/{post_id}/'

    @staticmethod
    def blog(post_id, company):
        return f'{URL._habr}/company/{company}/blog/{post_id}/'

    @staticmethod
    def company(company):
        return f'{URL._habr}/company/{company}/'

    @staticmethod
    def comment(comment_id, from_id, company=''):
        return f'{URL._habr}/post/{from_id}/#comment_{comment_id}'

class URL:
    _habr = 'https://habr.com/ru'
    
    @staticmethod
    def user_posts(nickname):
        path = f'{URL._habr}/users/{nickname}/posts/'
        return path

    @staticmethod
    def user_comments(nickname):
        path = f'{URL._habr}/users/{nickname}/comments/'
        return path

    @staticmethod
    def user_favorites(nickname):
        path = f'{URL._habr}/users/{nickname}/favorites/'
        return path

    @staticmethod
    def post_comment(post_id, com_id):
        path = f'{URL._habr}/post/{post_id}/{com_id}/'
        return path
    
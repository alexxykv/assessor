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
    def company_employes(company):
        return f'{URL._habr}/company/{company}/workers/all/rating/'

    @staticmethod
    def company_subscribers(company, page):
        return f'{URL._habr}/company/{company}/fans/all/rating/page{page}/'

    @staticmethod
    def company_posts(company, page):
        return f'{URL._habr}/company/{company}/blog/page{page}/'

    @staticmethod
    def comment(comment_id, from_id, company=''):
        return f'{URL._habr}/post/{from_id}/#comment_{comment_id}'

    @staticmethod
    def hub(hub_name):
        return f'{URL._habr}/hub/{hub_name}/'

    @staticmethod
    def hub_authors(hub_name):
        return f'{URL._habr}/hub/{hub_name}/authors/'

    @staticmethod
    def hub_companies(hub_name):
        return f'{URL._habr}/hub/{hub_name}/companies/'

    @staticmethod
    def hub_top_posts(hub_name, page):
        return f'{URL._habr}/hub/{hub_name}/top/page{page}/'

    @staticmethod
    def hub_last_posts(hub_name, page):
        return f'{URL._habr}/hub/{hub_name}/page{page}/'
    
    @staticmethod
    def search(req, target_type, page, order_by):
        return f'{URL._habr}/search/page{page}/?target_type={target_type}&order_by={order_by}&q={req}&flow='
    
from .utils import get_HTMLtext, fetch
from .regex import RegexCompany
from .urls import URL

class Company:
    def __init__(self, company):
        self.url = URL.company(company)
        text = get_HTMLtext(self.url)
        self.company = company
        self.name = self._get_name(text)
        self.rating = self._get_rating(text)
        self.founded = self._get_founded(text)
        self.site = self._get_site(text)
        self.count_employes = self._get_count_employes(text)
        self.registered = self._get_registered(text)
        self.representative = self._get_representative(text)

    def _get_name(self, text):
        name = fetch(RegexCompany.NAME, text)
        return name[0] if name else ''

    def _get_rating(self, text):
        rating = fetch(RegexCompany.RATING, text)
        return rating[0].replace('\xa0', '').replace(',', '.') if rating else ''

    def _get_founded(self, text):
        founded = fetch(RegexCompany.FOUNDED, text)
        return founded[0] if founded else ''

    def _get_site(self, text):
        site = fetch(RegexCompany.SITE, text)
        return site[0] if site else ''

    def _get_count_employes(self, text):
        count_employes = fetch(RegexCompany.COUNT_EMPLOYES, text)
        return count_employes[0] if count_employes else ''

    def _get_registered(self, text):
        registered = fetch(RegexCompany.REGISTERED, text)
        return registered[0] if registered else ''

    def _get_representative(self, text):
        representative = fetch(RegexCompany.REPRESENTATIVE, text)
        return representative[0] if representative else ''

    @staticmethod
    def get(company_url):
        company = Company(company_url)
        return company.__dict__

    @staticmethod
    def get_employes(company):
        url = URL.company_employes(company)
        text = get_HTMLtext(url)
        nicknames = fetch(RegexCompany.EMPLOYES_NICKNAME, text)
        ratings = fetch(RegexCompany.EMPLOYES_RATING, text)
        karma = fetch(RegexCompany.EMPLOYES_KARMA, text)
        result = []
        for i in range(len(nicknames)):
            result.append({
                'nickname': nicknames[i],
                'rating': ratings[i].replace('\xa0', '').replace(',', '.'),
                'karma': karma[i].replace('\xa0', '').replace(',', '.')
            })
        return result

    @staticmethod
    def get_subscribers(company, page=1):
        url = URL.company_subscribers(company, page)
        text = get_HTMLtext(url)
        nicknames = fetch(RegexCompany.SUBSCRIBER_NICKNAME, text)
        ratings = fetch(RegexCompany.SUBSCRIBER_RATING, text)
        karma = fetch(RegexCompany.SUBSCRIBER_KARMA, text)
        result = []
        for i in range(len(nicknames)):
            result.append({
                'nickname': nicknames[i],
                'rating': ratings[i].replace('\xa0', '').replace(',', '.'),
                'karma': karma[i].replace('\xa0', '').replace(',', '.')
            })
        return result

    @staticmethod
    def get_last_posts(company, page=1):
        url = URL.company_posts(company, page)
        text = get_HTMLtext(url)
        posts = fetch(RegexCompany.POSTS, text)
        result = []
        for i in range(len(posts)):
            result.append({
                'type': posts[i][0],
                'id': posts[i][1],
                'title': posts[i][2]
            })
        return result
    
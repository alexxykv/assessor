import re


class DataHandler:

    SITES = {
        'github.com': r'https://github.com/(.*?)/.*',
        'habr.com': r'https://habr.com/ru/users/(.*?)/.*',
        'linkedin.com': r'https://www.linkedin.com/in/(.*?)/.*',
        'codeforces.com': r'https://codeforces.com/profile/(.*?)/.*',
        'vk.com': r'https://vk.com/i?d?(.*?)/.*',
        'kaggle.com': r'https://www.kaggle.com/(.*?)/.*',
    }

    @staticmethod
    def process(raw_data):
        data = {}
        urls = []
        convert_url = '/result/convert?'

        for key, value in raw_data.items():
            if key == 'csrfmiddlewaretoken':
                continue

            convert_url += f'{key}={value[0]}&'

            if key.startswith('site'):
                url = value[0]
                if not url.endswith('/'):
                    url += '/'
                urls.append(url)
                continue

            data[key] = value[0]

        data['sites'] = DataHandler.identify_sites(urls)
        data['convert_url'] = convert_url[:-1]

        return data

    @staticmethod
    def identify_sites(urls):
        sites = {}

        for url in urls:
            for domen in DataHandler.SITES:
                if domen in url:
                    nickname = DataHandler.fetch_nickname(url, domen)
                    if nickname:
                        sites[domen] = {
                            'url': url,
                            'nickname': nickname,
                        }

        return sites

    @staticmethod
    def fetch_nickname(url, domen):
        pattern = DataHandler.SITES[domen]
        fetched = re.findall(pattern, url)

        if fetched:
            return fetched[0]
        return ''

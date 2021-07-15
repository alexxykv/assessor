from parsing.github import request_construct as rc


def srch(nickname):
        url = f'https://api.github.com/search/users?q={nickname}'
        resp = rc.get_json_resp(url)

        users = []
        for item in resp['items']:
                users.append({
                    'url': item['html_url'] + '/',
                    'nickname': item['login'].lower(),
                })

        return users

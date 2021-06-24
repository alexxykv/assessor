import re
from sher import run


def get_screen_names(urls: list, vk):
    """ Getting screen names from urls and VK """

    screen_names = {'vk.com': vk['screen_name']} if vk else {}
    for url in urls:
        array = url.split('/')
        domain = re.findall(r'//([^/]*\.[^/:]+)', url)[0]
        if url[len(url) - 1] == '/':
            screen_names[domain] = array[-2]
        else:
            screen_names[domain] = array[-1]
    return screen_names


def get_info(request, fields):
    """ Getting the transmitted data from requests """

    info = {}
    for field in fields:
        value = request.get(field)
        if value:
            info[field] = value
    return info


def get_urls(request):
    """ Getting urls """

    urls = []
    for i in range(1, 11):
        value = request.get(f'site_{i}')
        if value:
            urls.append(value)

    return urls


def get_convert_url(info, urls):
    convert_url = '/result/convert?'
    for field, value in info.items():
        convert_url += field + '=' + value + '&'

    for i, url in enumerate(urls):
        convert_url += f'site_{i + 1}' + '=' + url + '&'

    return convert_url[:-1]


def sherlock(screen_names):
    """ Finding user profile in another sites """

    res = {}
    for nick in screen_names.values():
        res[nick] = run.search(nick)

    return res

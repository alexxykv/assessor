import re
import requests


def fetch(regex, text):
    data = re.findall(regex, text)
    return data


def get_HTMLtext(url):
    """

    """

    response = requests.get(url, cookies={'web_override': "'false'"})
    status = response.status_code

    if status == 200:
        text = response.text
        return text
    else:
        return response


def stats_handler(stats):
    replacement = [('\xa0', ''), ('–', '-'), (',', '.')]
    for i in range(len(stats)):
        for old, new in replacement:
            stats[i] = stats[i].replace(old, new)

        stats[i] = convert_to_number(stats[i])
        
    return stats


def voitings_handler(voitings):
    voitings = voitings.replace('–', '-')
    return int(voitings)


def views_handler(views):
    if views.endswith('k'):
        views = views.replace('k', '')
        views = views.replace(',', '.')
        views = float(views)
        return int(views * 1000)
    else:
        return int(views)


def coms_count_handler(count):
    if (count == 'Комментировать'):
        return 0
    else:
        return int(count)


def convert_to_number(string):
    if string.isdigit():
        return int(string)
    else:
        return float(string)

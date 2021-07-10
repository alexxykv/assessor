import re
from vk_finder import finder
from parsing.github import gitpars
from linkedin_api import Linkedin
from parsing.codeforces.codeforces import Codeforce
from parsing.habr.user import User
from .utils import habr_avg, habr_evaluation, git_evaluation


def get_pars(urls, sherlock, screen_names):
    """ Starting parsing """

    sherlock_fields = ['GitHub', 'habr']
    pars_dict = {'github.com': github_pars, 'habr.com': habr_pars, 'www.linkedin.com': linkedin_pars,
                 'codeforces.com': codeforces_pars}

    # Starting parsing sites from form
    result = {}
    for url in urls:
        domain = re.findall(r'//([^/]*\.[^/:]+)', url)[0]
        if domain in pars_dict:
            result[domain] = pars_dict[domain](screen_names[domain])

    # Starting parsing sites from sherlock
    for nick, urls in sherlock.items():
        for key, url in urls.items():
            domain = re.findall(r'//([^/]*\.[^/:]+)', url)[0].replace('www.', '')  # Fix it
            if domain not in result and key in sherlock_fields:
                result[domain] = pars_dict[domain](nick)
    return result


def vk_pars(info):
    # Taking all user with using info
    users = finder.find(info)
    # return only first user
    return users[0] if users else None


def github_pars(nickname):
    avg_values = {
        'followers': 98,
        'count_lang': 4,
        'stars': 227,
        'count_all_repos': 37,
        'contr_y2': 21,
        'contr_y1': 18,
        'contr_y0': 14
    }
    url = 'https://github.com/' + nickname
    user = gitpars.GithubParser(url)
    languages = user.languages
    user_repos = user.user_repos
    forked_repos = user.forked_repos
    result = {
        'user': user,
        'count': {
            'all_repos': len(user_repos) + len(forked_repos),
            'user_repos': len(user_repos),
            'forked_repos': len(forked_repos),
            'languages': len(languages)
        },
        'contributions_year': user.average_contributions(3),
        'avg_values': avg_values
    }
    result['analysis'] = {
        'followers': result['user'].followers - avg_values['followers'],
        'count_lang': result['count']['languages'] - avg_values['count_lang'],
        'stars': result['user'].stars - avg_values['stars'],
        'count_all_repos': result['count']['all_repos'] - avg_values['count_all_repos'],
    }
    result['ratio'] = git_evaluation(avg_values, result)
    return result


def habr_pars(nickname):
    avg_values = {
        'karma': 46.6,
        'rating': 87.6,
        'followers': 20.0,
        'contribs': 123.2,
        'voitings': 44.1,
        'favs_count': 59.2,
        'views': 14.6
    }
    result = {
        'main': User.get(nickname),
        'posts': User.get_posts(nickname),
        'avg_values': dict((k, str(v)) for k, v in avg_values.items())
    }
    if not result['main']['stats']:
        result['main']['stats'] = {
            'karma': 0,
            'rating': 0,
            'followers': 0,
            'following': 0
        }
    result['avgs'] = habr_avg(result['posts'], result['main']['contribution'])
    result['ratio'] = habr_evaluation(avg_values, result, result['avgs'])
    result['analysis'] = {
        'karma': round(float(result['main']['stats']['karma']) - avg_values['karma'], 2),
        'rating': round(float(result['main']['stats']['rating']) - avg_values['rating'], 2),
        'followers': int(float(result['main']['stats']['followers']) - avg_values['followers']),
        'contribs': round(result['avgs']['contribs'] - avg_values['contribs'], 2),
        'voitings': round(result['avgs']['voitings'] - avg_values['voitings'], 2),
        'favs_count': round(result['avgs']['favs_count'] - avg_values['favs_count'], 2),
        'views': str(round(result['avgs']['views'] - avg_values['views'], 2)) + 'k',
    }
    result['avgs'] = dict((k, str(v)) for k, v in result['avgs'].items())
    result['avgs']['views'] = result['avgs']['views'] + 'k'

    return result


def linkedin_pars(nickname):
    api_link = Linkedin('+79065350750', '1qaz2wsx3edC')
    profile = api_link.get_profile(nickname)
    contact = api_link.get_profile_contact_info(nickname)
    network = api_link.get_profile_network_info(nickname)
    linkedin = profile | contact | network
    linkedin['skills'] = api_link.get_profile_skills(nickname)
    linkedin['url'] = 'https://www.linkedin.com/in/' + linkedin['profile_id']
    # linkedin['updates'] = api_link.get_profile_updates(nickname, max_results=2)
    # print(json.dumps(linkedin['updates']))
    return linkedin


def codeforces_pars(nickname):
    code = Codeforce()
    code_user = code.user_info([nickname])

    if len(code_user) != 0:
        return {
            'user': code_user[0],
            'blogs': code.user_blog_entries(nickname)
        }
    return None


if __name__ == '__main__':
    pass

def habr_avg(posts, contributions):
    """ Getting habr average values """

    result = {}
    avgs = {
        'voitings': 0,
        'favs_count': 0,
        'views': 0
    }
    # Average for posts
    for post in posts:
        avgs['voitings'] += float(post['voitings'][1:])
        avgs['favs_count'] += float(post['favs_count'])
        views = post['views']
        if views[len(post['views']) - 1] == 'k':
            avgs['views'] += float(post['views'].replace('k', ''))
        else:
            avgs['views'] += float(post['views']) / 1000
    len_posts = len(posts)
    for key, value in avgs.items():
        result[key] = round(value / len_posts, 1) if len_posts != 0 else 0

    # Average for contributions
    avgs['contribs'] = 0
    for contrib in contributions:
        avgs['contribs'] += float(contrib['value'])

    len_contribs = len(contributions)
    result['contribs'] = round(avgs['contribs'] / len_contribs, 1) if len_contribs != 0 else 0

    return result


def habr_evaluation(habr_avg_values, habr, avgs):
    # Metrics ratio HABR
    karma = 100 * float(habr['main']['stats']['karma']) / habr_avg_values['karma'] * 0.2
    rating = 100 * float(habr['main']['stats']['rating']) / habr_avg_values['rating'] * 0.2
    followers = 100 * float(habr['main']['stats']['followers']) / habr_avg_values['followers'] * 0.1
    contribs = 100 * avgs['contribs'] / habr_avg_values['contribs'] * 0.175
    voitings = 100 * avgs['voitings'] / habr_avg_values['voitings'] * 0.1
    favs_count = 100 * avgs['favs_count'] / habr_avg_values['favs_count'] * 0.1
    views = 100 * avgs['views'] / habr_avg_values['views'] * 0.125
    habr_ratio = {
        'karma': 20 if karma >= 20 else karma,
        'rating': 20 if rating >= 20 else rating,
        'followers': 10 if followers >= 10 else followers,
        'contribs': 17.5 if contribs >= 17.5 else contribs,
        'voitings': 10 if voitings >= 10 else voitings,
        'favs_count': 10 if favs_count >= 10 else favs_count,
        'views': 12.5 if views >= 12.5 else views,
    }
    return round(sum(habr_ratio.values()))


def git_evaluation(git_avg_values, github):
    # Metrics ratio GITHUB
    # Stars - 15%, y2019,2020,2021 - 15% (45%), Lang - 10%
    # Followers - 15%, All repos - 15%
    followers = 100 * github['user'].followers / git_avg_values['followers'] * 0.15
    langs = 100 * github['count']['languages'] / git_avg_values['count_lang'] * 0.10
    stars = 100 * github['user'].stars / git_avg_values['stars'] * 0.15
    all_repos = 100 * github['count']['all_repos'] / git_avg_values['count_all_repos'] * 0.15
    y2 = 100 * github['contributions_year'][2] / git_avg_values['contr_y2'] * 0.15
    y1 = 100 * github['contributions_year'][1] / git_avg_values['contr_y1'] * 0.15
    y0 = 100 * github['contributions_year'][0] / git_avg_values['contr_y0'] * 0.15
    git_ratio = {
        "followers": 15 if followers >= 15 else followers,
        "langs": 10 if langs >= 10 else langs,
        "stars": 15 if stars >= 15 else stars,
        "all_repos": 15 if all_repos >= 15 else all_repos,
        "cont_year_y2": 15 if y2 >= 15 else y2,
        "cont_year_y1": 15 if y1 >= 15 else y1,
        "cont_year_y0": 15 if y0 >= 15 else y0
    }
    return round(sum(git_ratio.values()))

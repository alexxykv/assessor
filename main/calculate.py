class Calculate:

    def __init__(self):
        pass

    @staticmethod
    def avg_habr_contributions(contributions):
        count = len(contributions)
        value = 0

        for contribution in contributions:
            value += contribution['value']

        if count != 0:
            return round(value / count)
        return 0

    @staticmethod
    def avg_habr_posts(posts):
        count = len(posts)
        voitings, favs_count, coms_count, views = [0] * 4

        for post in posts:
            voitings += post['voitings']
            favs_count += post['favs_count']
            coms_count += post['coms_count']
            views += post['views']

        if count != 0:
            return {
                'voitings': round(voitings / count),
                'favs_count': round(favs_count / count),
                'coms_count': round(coms_count / count),
                'views': round(views / count),
            }
        return {'voitings': 0, 'favs_count': 0, 'coms_count': 0, 'views': 0}

    @staticmethod
    def habr_analysis(user_info, avg_own, avg_all):
        return {
            'karma': round(float(user_info['stats']['karma']) - avg_all['karma']),
            'rating': round(float(user_info['stats']['rating']) - avg_all['rating']),
            'followers': int(float(user_info['stats']['followers']) - avg_all['followers']),
            'voitings': round(avg_own['voitings'] - avg_all['voitings']),
            'contribs': round(avg_own['contribs'] - avg_all['contribs']),
            'favs_count': round(avg_own['favs_count'] - avg_all['favs_count']),
            'views': str(round(avg_own['views'] - avg_all['views'])) + 'k',
        }

    @staticmethod
    def habr_evaluation(user_info, avg_own, avg_all):
        # Metrics ratio HABR
        karma = 100 * float(user_info['stats']['karma']) / avg_all['karma'] * 0.2
        rating = 100 * float(user_info['stats']['rating']) / avg_all['rating'] * 0.2
        followers = 100 * float(user_info['stats']['followers']) / avg_all['followers'] * 0.1
        contribs = 100 * avg_own['contribs'] / avg_all['contribs'] * 0.175
        favs_count = 100 * avg_own['favs_count'] / avg_all['favs_count'] * 0.1
        views = 100 * avg_own['views'] / avg_all['views'] * 0.125

        habr_ratio = {
            'karma': 25 if karma >= 25 else karma,
            'rating': 25 if rating >= 25 else rating,
            'followers': 10 if followers >= 10 else followers,
            'contribs': 17.5 if contribs >= 17.5 else contribs,
            'favs_count': 10 if favs_count >= 10 else favs_count,
            'views': 12.5 if views >= 12.5 else views,
        }

        return round(sum(habr_ratio.values()))

    @staticmethod
    def git_evaluation(user, avg_all):
        # Metrics ratio GITHUB
        # Stars - 15%, y2019,2020,2021 - 15% (45%), Lang - 10%
        # Followers - 15%, All repos - 15%
        followers = 100 * user.followers / avg_all['followers'] * 0.15
        langs = 100 * len(user.languages) / avg_all['count_lang'] * 0.10
        stars = 100 * user.stars / avg_all['stars'] * 0.15
        all_repos = 100 * (len(user.user_repos) + len(user.forked_repos)) / avg_all['count_all_repos'] * 0.15
        contributions_year = user.average_contributions(3)
        y2 = 100 * contributions_year[2] / avg_all['contr_y2'] * 0.15
        y1 = 100 * contributions_year[1] / avg_all['contr_y1'] * 0.15
        y0 = 100 * contributions_year[0] / avg_all['contr_y0'] * 0.15

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

    @staticmethod
    def git_analysis(user, avg_all):
        return {
            'followers': user.followers - avg_all['followers'],
            'count_lang': len(user.languages) - avg_all['count_lang'],
            'stars': user.stars - avg_all['stars'],
            'count_all_repos': len(user.user_repos) + len(user.forked_repos) - avg_all['count_all_repos'],
        }
    
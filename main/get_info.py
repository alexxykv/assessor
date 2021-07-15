# from vk_finder import finder


class Data:
    @staticmethod
    def get_habr_main(habr):
        return {
            'karma': str(habr['stats']['karma']) if habr['stats'] else 0,
            'rating': str(habr['stats']['rating']) if habr['stats'] else 0,
            'followers': str(habr['stats']['followers']) if habr['stats'] else 0,
            'following': habr['stats']['following'] if habr['stats'] else 0,
            'work_name': habr['work']['name'] if habr['work'] else '',
            'nickname': habr['nickname'],
            'url': habr['url']

        }

    @staticmethod
    def get_habr_contributions(habr):
        contributions = []
        for i in habr['contribution']:
            contributions.append(
                {
                    'title': i['name'],
                    'url': i['url'],
                    'value': i['value']
                }
            )
        return contributions

    @staticmethod
    def get_habr_avg(habr_posts, contributions):
        lenght = len(habr_posts)
        lenght_contribs = len(contributions)
        avg_voitings = 0
        avg_favs_count = 0
        avg_views = 0
        avg_contribs = 0
        avgs = {
            'voitings': 0,
            'favs_count': 0,
            'views': 0,
            'contribs': 0
        }
        if lenght != 0:
            for post in habr_posts:
                views = post['views']
                if views[len(post['views']) - 1] == 'k':
                    views = float(post['views'].replace('k', ''))
                else:
                    views = float(post['views']) / 1000
                avg_voitings += int(post['voitings'].replace('–', '-'))
                avg_favs_count += int(post['favs_count'])
                avg_views += views
            avgs = {
                'voitings': round(avg_voitings / lenght, 1),
                'favs_count': round(avg_favs_count / lenght, 1),
                'views': round(avg_views / lenght, 1),
            }
        if lenght_contribs != 0:
            for i in contributions:
                avg_contribs += float(i['value'])
            avgs['contribs'] = round(avg_contribs / lenght_contribs, 1)
        return avgs

    @staticmethod
    def get_git_lang(user):
        data_lang = {}
        for k,i in user.languages.items():
            data_lang[k] = i
        return data_lang

    @staticmethod
    def get_git_userRepos(user):
        return user.user_repos

    @staticmethod
    def get_vk(info):
        return finder.find(info)

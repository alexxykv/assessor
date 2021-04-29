from parsing.habr.user import User

class Data:

    def get_habr_main(nick):
        habr = User.get(nick)
        return {
            'karma': habr['stats']['karma'],
            'rating': habr['stats']['rating'],
            'followers': habr['stats']['followers'],
            'following': habr['stats']['following'],
            'work_name': habr['work']['name'] if habr['work'] else '',
            'nickname': habr['nickname'],
            'url': habr['url']

        }

    def get_habr_contributions(nick):
        habr = User.get(nick)
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

    def get_habr_posts(nick):
        habr_posts = User.get_posts(nick)
        posts = []

        for post in habr_posts:
            posts.append({
                'title': post['title'],
                'voitings': post['voitings'],
                'favs_count': post['favs_count'],
                'views': post['views'],
                'url': post['url']
            })
        return posts

    def get_habr_avg(nick):
        habr_posts = User.get_posts(nick)
        lenght = len(habr_posts)
        avg_voitings = 0
        avg_favs_count = 0
        avg_views = 0

        for post in habr_posts:
            avg_voitings += int(post['voitings'][1::])
            avg_favs_count += int(post['favs_count'])
            avg_views += float(post['views'][:len(post['views']) - 1])

        avgs = {
            'voitings': str(round(avg_voitings / lenght, 1)).replace(',', '.'),
            'favs_count': str(round(avg_favs_count / lenght, 1)).replace(',', '.'),
            'views': str(round(avg_views / lenght, 1)) + "k"
        }

        return avgs

    def get_git_lang(user):
        data_lang = {}
        for k,i in user.languages.items():
            data_lang[k] = i
        return data_lang

    def get_git_userRepos(user):
        return user.user_repos

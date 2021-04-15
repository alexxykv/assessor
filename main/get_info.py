from parsing.habr.user import User

class Data:

    def get_habr_main(nick):
        habr = User.get(nick)
        return {
            'karma': habr['stats']['karma'],
            'rating': habr['stats']['rating'],
            'followers': habr['stats']['followers'],
            'following': habr['stats']['following'],
            'work_name': habr['work']['name'],
            'nickname': habr['nickname']

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
                'views': post['views']
            })
        return posts

    def get_git_lang(user):
        data_lang = {}
        for k,i in user.languages().items():
            data_lang[k] = i
        return data_lang

    def get_git_userRepos(user):
        return user.user_repos

from parsing.habr.user import User

class Data:

    def get_habr_main(nick):
        habr = User.get(nick)
        return [habr['stats']['karma'], habr['stats']['rating'],
                habr['stats']['followers'], habr['stats']['following'], habr['work']['name']]

    def get_habr_contributions(nick):
        habr = User.get(nick)
        contributions = []
        for i in habr['contribution']:
            contributions.append([i['url'], i['value']])
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

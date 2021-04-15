from django.shortcuts import render
from .forms import MainForm
from .url_check import CheckUrl
from .get_info import Data

def getting_sites(form):
    sites = []
    for i in range(1, 11):
        site = form.cleaned_data.get(f"site_{i}")
        if len(site) != 0:
            sites.append(site)
    return sites

def index(request):
    error = ''
    github = {}
    habr = {}
    if request.method == "POST":
        form = MainForm(request.POST or None)
        if form.is_valid():
            urls = CheckUrl(getting_sites(form)).check()
            if 'github.com' in urls:
                user = urls['github.com']
                user_repos = Data.get_git_userRepos(user)
                github = {
                    'data_lang': Data.get_git_lang(user),
                    'nick': user.nickname,
                    'user_repos': user_repos,
                    'count_user_repos': len(user_repos),
                    'count_fork': len(user.forked_repos),
                    'followers': user.followers(),
                    'stars': user.stars(),
                    'profile_url': user.profile_url
                }

            if 'habr.com' in urls:
                nick = urls['habr.com']
                habr = {
                    'main': Data.get_habr_main(nick),
                    'contributions': Data.get_habr_contributions(nick),
                    'posts': Data.get_habr_posts(nick)
                }

            data = {
                'form': form,
                'habr': habr,
                'github': github
            }
            return render(request, 'main/result.html', data)
        else:
            error = 'Форма была неверной'

    form = MainForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/index.html', data)

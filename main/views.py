from django.shortcuts import render, redirect
from .forms import MainForm
from .url_check import CheckUrl
from .get_info import Data


def index(request):
    return render(request, 'main/index.html', {'form': MainForm()})


def result(request):
    github = {}
    habr = {}
    if request.method == "POST":
        form = MainForm(request.POST or None)
        if form.is_valid():
            urls = CheckUrl(getting_sites(form)).check()
            info = {
                'first_name': form.cleaned_data.get("firstName"),
                'last_name': form.cleaned_data.get("middleName"),
                'date_birth': form.cleaned_data.get("date_birth"),
                'city': form.cleaned_data.get("city")
            }
            user_vk = Data.get_vk(info)
            github = add_github(github, urls)
            habr = add_habr(habr, urls)
            data = {
                'form': form,
                'habr': habr,
                'github': github,
                'info': info,
                'photo': user_vk[0]['photo_200'] if user_vk else '/static/main/img/anon.png'
            }
            return render(request, 'main/result.html', data)
    return redirect('/')


def add_habr(habr, urls):
    if 'habr.com' in urls:
        nick = urls['habr.com']
        habr = {
            'main': Data.get_habr_main(nick),
            'contributions': Data.get_habr_contributions(nick),
            'posts': Data.get_habr_posts(nick),
            'avgs': Data.get_habr_avg(nick)
        }
    else:
        habr = None
    return habr


def add_github(github, urls):
    if 'github.com' in urls:
        user = urls['github.com']
        user_repos = Data.get_git_userRepos(user)
        github = {
            'data_lang': Data.get_git_lang(user),
            'nick': user.nickname,
            'user_repos': user_repos,
            'count_user_repos': len(user_repos),
            'count_fork': len(user.forked_repos),
            'followers': user.followers,
            'stars': user.stars,
            'profile_url': user.url,
            'contributions_year': user.average_contributions(3),
            'photo': user.photo
        }
    else:
        github = None
    return github


def getting_sites(form):
    sites = []
    for i in range(1, 11):
        site = form.cleaned_data.get(f"site_{i}")
        if len(site) != 0:
            sites.append(site)
    return sites

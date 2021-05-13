from django.shortcuts import render, redirect
from .forms import MainForm
from .url_check import CheckUrl
from .get_info import Data
from datetime import date


def index(request):
    return render(request, 'main/index.html', {'form': MainForm()})


def result(request):
    github = {}
    habr = {}
    sites = []
    info = {}
    form = None
    flag = False
    if request.method == 'GET':
        first_name = request.GET.get('first_name')
        last_name = request.GET.get('last_name')
        if first_name is not None and last_name is not None:
            for i in range(1, 11):
                sites.append(request.GET.get(f'site_{i}'))
            date_time = request.GET.get('date_birth').split('.')
            info = {
                'first_name': first_name,
                'last_name': last_name,
                'patronymic': request.GET.get('patronymic'),
                'date_birth': date(int(date_time[2]), int(date_time[1]), int(date_time[0])) if date_time[0] != '' else None,
                'city': request.GET.get('city'),
                'phone_number': request.GET.get('phone_number'),
                'email': request.GET.get('email'),
                'sites': sites
            }
            flag = True

    if request.method == "POST":
        form = MainForm(request.POST or None)
        if form.is_valid():
            sites = [form.cleaned_data.get(f'site_{i}') for i in range(1, 11)]
            info = {
                'first_name': form.cleaned_data.get("firstName"),
                'last_name': form.cleaned_data.get("lastName"),
                'patronymic': form.cleaned_data.get("patronymic"),
                'date_birth': form.cleaned_data.get("date_birth"),
                'city': form.cleaned_data.get("city"),
                'phone_number': form.cleaned_data.get("phone_number"),
                'email': form.cleaned_data.get("email"),
                'sites': sites
            }
            flag = True
    if flag:
        urls = CheckUrl(getting_sites(sites)).check()
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
        if info['date_birth']:
            data['date_birth'] = str(info['date_birth'].timetuple()[2]) \
                                 + '.' + str(info['date_birth'].timetuple()[1]) \
                                 + '.' + str(info['date_birth'].timetuple()[0])
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


def getting_sites(data):
    sites = []
    for i in range(0, 10):
        site = data[i]
        if site is not None and site != '':
            sites.append(site)
    return sites
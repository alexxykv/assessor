from django.shortcuts import render, redirect
from .forms import MainForm
from .url_check import CheckUrl
from .get_info import Data
from datetime import date
from parsing.habr.user import User
from django.http import HttpResponse
from sher import run
import urllib.parse
import pdfcrowd


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
            sites = [request.GET.get(f'site_{i}') if request.GET.get(f'site_{i}') else '' for i in range(1, 11)]
            info = {
                'first_name': '',
                'last_name': '',
                'patronymic': '',
                'date_birth': None,
                'city': '',
                'phone_number': '',
                'email': ''
            }
            for item in request.GET.items():
                info[item[0]] = item[1]
            if request.GET.get('date_birth'):
                date_array = request.GET.get('date_birth').split('-')
                info['date_birth'] = date(int(date_array[0]), int(date_array[1]), int(date_array[2]))
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
                'email': form.cleaned_data.get("email")
            }
            flag = True
    if flag:
        user_vk = Data.get_vk(info)
        sherlock = run.search(user_vk[0]['screen_name'])
        urls = CheckUrl(getting_sites(sites), sherlock).check()
        github = add_github(github, urls)
        habr = add_habr(habr, urls)

        data = {
            'form': form,
            'habr': habr,
            'github': github,
            'vk': user_vk[0],
            'sherlock': sherlock,
            'info': info,
            'photo': user_vk[0]['photo_200'] if user_vk else '/static/main/img/anon.png'
        }
        convert_url = '/result/convert?'
        for item in info.items():
            if item[1] != '' and item[1]:
                convert_url += item[0] + '=' + str(item[1]) + '&'
        i = 1
        for site in sites:
            if site != '':
                convert_url += f'site_{i}' + '=' + site + '&'
            i += 1
        info['convert_url'] = convert_url[:-1]
        return render(request, 'main/result.html', data)
    return redirect('/')


def add_habr(habr, urls):
    if 'habr.com' in urls:
        nick = urls['habr.com']
        user = User.get(nick)
        posts = User.get_posts(nick)
        habr = {
            'main': Data.get_habr_main(user),
            'contributions': Data.get_habr_contributions(user),
            'posts': posts,
            'avgs': Data.get_habr_avg(posts)
        }
        return habr
    return None


def add_github(github, urls):
    if 'github.com' in urls:
        # Metrics
        avg_values = {
            'followers': 98,
            'count_lang': 4,
            'stars': 227,
            'count_all_repos': 37,
            'contr_y2': 21,
            'contr_y1': 18,
            'contr_y0': 14
        }

        user = urls['github.com']
        user_repos = Data.get_git_userRepos(user)
        langs = Data.get_git_lang(user)
        github = {
            'avg_values': {
                '2': avg_values['contr_y2'],
                '1': avg_values['contr_y1'],
                '0': avg_values['contr_y0']
            },
            'data_lang': langs,
            'nick': user.nickname,
            'user_repos': user_repos,
            'forked_repos': user.forked_repos,
            'count_all_repos': len(user_repos) + len(user.forked_repos),
            'count_forked_repos': len(user.forked_repos),
            'count_user_repos': len(user_repos),
            'count_fork': len(user.forked_repos),
            'count_lang': len(langs),
            'followers': user.followers,
            'stars': user.stars,
            'profile_url': user.url,
            'contributions_year': user.average_contributions(3),
            'photo': user.photo
        }
        github['analysis'] = {
            'followers': github['followers'] - avg_values['followers'],
            'count_lang': github['count_lang'] - avg_values['count_lang'],
            'stars': github['stars'] - avg_values['stars'],
            'count_all_repos': github['count_all_repos'] - avg_values['count_all_repos'],
        }
        github['ratio'] = str(evaluation(avg_values, github))
        return github
    return None


def evaluation(git_avg_values, github):
    # Metrics ratio GITHUB
    # Stars - 15%, y2019,2020,2021 - 15% (45%), Lang - 10%
    # Followers - 15%, All repos - 15%
    git_ratio = {
        "followers": 100 * github['followers'] / git_avg_values['followers'] * 0.15,
        "langs": 100 * github['count_lang'] / git_avg_values['count_lang'] * 0.10,
        "stars": 100 * github['stars'] / git_avg_values['stars'] * 0.15,
        "all_repos": 100 * github['count_all_repos'] / git_avg_values['count_all_repos'] * 0.15,
        "cont_year_y2": 100 * github['contributions_year'][2] / git_avg_values['contr_y2'] * 0.15,
        "cont_year_y1": 100 * github['contributions_year'][1] / git_avg_values['contr_y1'] * 0.15,
        "cont_year_y0": 100 * github['contributions_year'][0] / git_avg_values['contr_y0'] * 0.15
    }
    return round(sum(git_ratio.values()), 2)


def getting_sites(data):
    sites = []
    for i in range(0, 10):
        site = data[i]
        if site is not None and site != '':
            sites.append(site)
    return sites


def convert(request):
    req = '/result?'
    for item in request.GET.items():
        req += str(item[0]) + '=' + str(item[1]) + '&'
    try:
        client = pdfcrowd.HtmlToPdfClient('dibiloid335', 'e6e7f5a5560117dc615690ca43311a71')
        site = f'http://84.201.152.104:8000{req[:-1]}'
        response = HttpResponse(content_type='application/pdf')
        response['Cache-Control'] = 'max-age=0'
        response['Accept-Ranges'] = 'none'
        response['Content-Disposition'] = "attachment; filename*=UTF-8''" + urllib.parse.quote('result.pdf', safe='')

        client.convertUrlToStream(site, response)
        return response
    except pdfcrowd.Error as why:
        return HttpResponse(why.getMessage(),
                            status=why.getCode(),
                            content_type='text/plain')

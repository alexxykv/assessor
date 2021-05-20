from django.shortcuts import render, redirect
from .forms import MainForm
from .url_check import CheckUrl
from .get_info import Data
from datetime import date
from parsing.habr.user import User
from django.http import HttpResponse
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


def convert(request):
    req = '/result?'
    for item in request.GET.items():
        req += str(item[0]) + '=' + str(item[1]) + '&'
    try:
        client = pdfcrowd.HtmlToPdfClient('zhopka2009', '6feb4fabe37724a3a159eac16fed6ff4')
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
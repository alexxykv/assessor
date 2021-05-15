from django.shortcuts import render, redirect
from .forms import MainForm
from .url_check import CheckUrl
from .get_info import Data
from datetime import date
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
            sites = [request.GET.get(f'site_{i}') for i in range(1, 11)]
            date_time = request.GET.get('date_birth').split('.') if request.GET.get('date_birth') else None
            info = {
                'first_name': first_name,
                'last_name': last_name,
                'patronymic': request.GET.get('patronymic'),
                'date_birth': date(int(date_time[2]), int(date_time[1]), int(date_time[0])) if date_time else None,
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


def convert(request):
    try:
        client = pdfcrowd.HtmlToPdfClient('zhopka2009', '6feb4fabe37724a3a159eac16fed6ff4')
        date_time = request.GET.get('date_birth').split('.')
        first_name = request.GET.get('first_name')
        last_name = request.GET.get('last_name')
        patronymic = request.GET.get('patronymic')
        date_birth = date(int(date_time[2]), int(date_time[1]), int(date_time[0])) if date_time[0] != '' else None
        email = request.GET.get('email')
        city = request.GET.get('city')
        phone_number = request.GET.get('phone_number')
        sites = [request.GET.get(f'site_{i}') for i in range(1, 11)]
        site = f'http://84.201.152.104:8000/result?first_name={first_name}&last_name={last_name}&patronymic={patronymic}&city={city}&date_birth={date_birth}&phone_number={phone_number}&email={email}&site_1={sites[0]}&site_2=${sites[1]}&site_3=${sites[2]}&site_4=${sites[3]}&site_5=${sites[4]}&site_6=${sites[5]}&site_7=${sites[6]}&site_8=${sites[7]}&site_9=${sites[8]}&site_10=${sites[9]}'
        response = HttpResponse(content_type='application/pdf')
        response['Cache-Control'] = 'max-age=0'
        response['Accept-Ranges'] = 'none'
        response['Content-Disposition'] = "attachment; filename*=UTF-8''" + urllib.parse.quote('result.pdf', safe='')

        client.convertUrlToStream(site, response)
        return response
    except pdfcrowd.Error as why:
        # send the error in the HTTP response
        return HttpResponse(why.getMessage(),
                            status=why.getCode(),
                            content_type='text/plain')
from django.shortcuts import render
from .forms import MainForm
from .checkUrl import CheckUrl
from parsing.habr.user import User


def index(request):
    error = ''
    info_array = {}
    habr_array = []
    contributions = []
    posts = []
    if request.method == "POST":
        form = MainForm(request.POST or None)
        if form.is_valid():
            sites = []
            for i in range(1, 11):
                site = form.cleaned_data.get(f"site_{i}")
                if len(site) != 0:
                    sites.append(site)

            chels_dict = CheckUrl(sites).check()
            if 'github.com' in chels_dict:
                git_chel = chels_dict['github.com']
                for i in git_chel.languages():
                    info_array[i[0]] = i[1]

            if 'habr.com' in chels_dict:
                habr_nick = chels_dict['habr.com']
                # MAIN INFO
                habr_chel = User.get(habr_nick)
                habr_array.append(habr_chel['stats']['karma'])  # Карма
                habr_array.append(habr_chel['stats']['rating']) # Рейтинг
                habr_array.append(habr_chel['stats']['followers'])  # Фолловеры
                habr_array.append(habr_chel['stats']['following']) # Подписки
                for i in habr_chel['contribution']:
                    contributions.append([i['url'], i['value']])

                # POSTS
                habr_posts = User.get_posts(habr_nick)
                for post in habr_posts:
                    posts.append({
                        'title': post['title'],
                        'voitings': post['voitings'],
                        'favs_count': post['favs_count'],
                        'views': post['views']
                    })



            data = {
                'form': form,
                'info_array': info_array,
                'habr_array': habr_array,
                'contributions': contributions,
                'posts': posts
            }
            return render(request, 'main/result.html', data)
        else:
            error = 'Форма была неверной'

    form = MainForm()

    data = {
        'form': form,
        'error': error,
        'info_array': info_array
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def result(request):
    return render(request, 'main/result.html')

def alpha_result(request):
    return render(request, 'alpha_main/alpha_result.html')

def alpha(request):
    error = ''
    info_array = {}
    habr_array = []
    contributions = []
    posts = []
    if request.method == "POST":
        form = MainForm(request.POST or None)
        if form.is_valid():
            sites = []
            for i in range(1, 11):
                site = form.cleaned_data.get(f"site_{i}")
                if len(site) != 0:
                    sites.append(site)

            chels_dict = CheckUrl(sites).check()
            if 'github.com' in chels_dict:
                git_chel = chels_dict['github.com']
                for i in git_chel.languages():
                    info_array[i[0]] = i[1]

            if 'habr.com' in chels_dict:
                habr_nick = chels_dict['habr.com']
                # MAIN INFO
                habr_chel = User.get(habr_nick)
                habr_array.append(habr_chel['stats']['karma'])  # Карма
                habr_array.append(habr_chel['stats']['rating'])  # Рейтинг
                habr_array.append(habr_chel['stats']['followers'])  # Фолловеры
                habr_array.append(habr_chel['stats']['following'])  # Подписки
                for i in habr_chel['contribution']:
                    contributions.append([i['url'], i['value']])

                # POSTS
                habr_posts = User.get_posts(habr_nick)
                for i in habr_posts:
                    info = {}
                    info['title'] = i['title']
                    info['voitings'] = Post.get(i['id'])['voitings']
                    info['favs_count'] = Post.get(i['id'])['favs_count']
                    info['views'] = Post.get(i['id'])['views']
                    posts.append(info)

            data = {
                'form': form,
                'info_array': info_array,
                'habr_array': habr_array,
                'contributions': contributions,
                'posts': posts
            }
            return render(request, 'alpha_main/alpha_result.html', data)
        else:
            error = 'Форма была неверной'

    form = MainForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'alpha_main/index.html', data)

from django.shortcuts import render
from .forms import MainForm
from .checkUrl import CheckUrl
from parsing.habr.user import User

def getting_sites(form):
    sites = []
    for i in range(1, 11):
        site = form.cleaned_data.get(f"site_{i}")
        if len(site) != 0:
            sites.append(site)
    return sites

def habr_pars(urls, contributions, posts):
    habr_nick = urls['habr.com']

    # MAIN INFO
    habr = User.get(habr_nick)
    habr_array = [habr['stats']['karma'], habr['stats']['rating'], habr['stats']['followers'],
                  habr['stats']['following']]

    # CONTRIBUTIONS
    for i in habr['contribution']:
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

def git_pars(urls, info_array):
    github = urls['github.com']
    for i in github.languages():
        info_array[i[0]] = i[1]

def index(request):
    error = ''
    info_array = {}   # Содержит языки программирования и проценты использования их | GitHub
    habr_array = []   # Содержит базовую информацию о человеке | Habr
    contributions = []   # Вклады | Habr
    posts = []   # Посты | Habr
    if request.method == "POST":
        form = MainForm(request.POST or None)
        if form.is_valid():
            urls = CheckUrl(getting_sites(form)).check()
            if 'github.com' in urls:
                git_pars(urls, info_array)

            if 'habr.com' in urls:
                habr_pars(urls, contributions, posts)

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
        'error': error
    }
    return render(request, 'main/index.html', data)

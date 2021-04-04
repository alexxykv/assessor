import re
from django.shortcuts import render
from .forms import MainForm
from parsing.github import gitpars
from .checkUrl import CheckUrl
from parsing.habr.user import User


def index(request):
    error = ''
    info_array = {}
    info2_array = []
    if request.method == "POST":
        form = MainForm(request.POST or None)
        if form.is_valid():
            sites = []
            for i in range(1, 11):
                site = form.cleaned_data.get(f"site_{i}")
                if len(site) != 0:
                    sites.append(site)

            # chels_dict = CheckUrl(sites).check()
            # habr_chel = chels_dict['habr.com']
            # info2_array.append(habr_chel)
            #
            # git_chel = chels_dict['github.com']
            # for i in git_chel.languages():
            #     info_array[i[0]] = i[1]
            #     print(i)

            data = {
                'form': form,
                'info_array': info_array,
                'info2_array': info2_array
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
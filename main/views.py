from django.shortcuts import render, redirect
from .models import Main
from .forms import MainForm
from parsing import gitpars
from parsing import habr
import json

def index(request):
    error = ''
    flag = False
    info_array = []
    if request.method == "POST":
        form = MainForm(request.POST or None)
        if form.is_valid():
            # file = open("test.txt", "w")
            # file.write(form.cleaned_data.get('name'))
            # file.close()
            # form.save() # Сохранить в БД
            chel = gitpars.GithubParser("https://github.com/ash2k")
            chel2 = json.loads(habr.parser.get_user("https://habr.com/ru/users/lounah/"))
            info_array.append(chel.languages())
            info_array.append(chel2)

            flag = True
            pass
        else:
            error = 'Форма была неверной'

    form = MainForm()

    data = {
        'form': form,
        'error': error,
        'info_array': info_array,
        'flag': flag
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')
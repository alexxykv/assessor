from django.shortcuts import render, redirect
from .models import Main
from .forms import MainForm

def index(request):
    error = ''
    if request.method == "POST":
        form = MainForm(request.POST or None)
        if form.is_valid():
            # file = open("test.txt", "w")
            # file.write(form.cleaned_data.get('name'))
            # file.close()
            form.save() # Сохранить в БД
        else:
            error = 'Форма была неверной'

    form = MainForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')
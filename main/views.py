from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MainForm
# 
from .processor import Processor
from .search import Search
from .data_handler import DataHandler
#
from urllib import parse
import pdfcrowd
import json
import os
# 

def index(request):
    return render(request, 'main/index.html', {'form': MainForm()})


def result(request):
    if request.method == 'POST':
        raw_data = dict(request.POST)

    if request.method == 'GET':
        raw_data = dict(request.GET)

    data = DataHandler.process(raw_data)
    
    # print(data)

    search = Search(data)
    search.run()

    # print(data)

    processor = Processor(data)
    processor.run()

    context = { 'info': data }
    context.update(processor.result)

    # print(json.dumps(context))

    return render(request, 'main/result.html', context=context)


def convert(request):
    req = '/result?'
    for item in request.GET.items():
        req += str(item[0]) + '=' + str(item[1]) + '&'
    try:
        login = os.environ.get('PDFCROWD_LOGIN')
        token = os.environ.get('PDFCROWD_TOKEN')
        client = pdfcrowd.HtmlToPdfClient(login, token)
        site = f'http://84.252.137.33:8000{req[:-1]}'
        response = HttpResponse(content_type='application/pdf')
        response['Cache-Control'] = 'max-age=0'
        response['Accept-Ranges'] = 'none'
        response['Content-Disposition'] = "attachment; filename*=UTF-8''" + parse.quote('result.pdf', safe='')

        client.convertUrlToStream(site, response)
        return response
    except pdfcrowd.Error as why:
        return HttpResponse(why.getMessage(),
                            status=why.getCode(),
                            content_type='text/plain')


def e_handler500(request):
    return render(request, 'main/errors/500.html')


def e_handler404(request, exception):
    return render(request, 'main/errors/404.html')

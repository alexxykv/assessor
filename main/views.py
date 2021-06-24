from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import MainForm
from .get_info import get_info, get_urls, get_screen_names, get_convert_url, sherlock
from .pars import get_pars, vk_pars
from django.http import HttpResponse
import urllib.parse
import pdfcrowd
import re


class ResultView(TemplateView):
    """
    Class for processing requests to the results page
    """

    template_name = 'main/result.html'
    form_fields = ['last_name', 'first_name', 'patronymic', 'date_birth', 'city', 'phone', 'email']

    def __init__(self, **kwargs):
        """
        Initialization

        `data`: Information transmitted with response
        `info`: Main information
        `urls`: Links to the user
        `screen_names`: User's nicknames
        `vk`: Vk user
        `sherlock`: Dictionary with found accounts
        `convert_url`: Url address for getting a pdf report
        """

        super().__init__(**kwargs)
        self.data = {}
        self.info = {}
        self.urls = []
        self.screen_names = {}
        self.vk = None
        self.sherlock = {}
        self.convert_url = ''

    def get(self, request, *args, **kwargs):
        """ Processing a GET request """

        method = request.GET
        self._get(method)
        return render(request, ResultView.template_name, self.data)

    def post(self, request):
        """ Processing a POST request """

        method = request.POST
        form = MainForm(method or None)
        if form.is_valid():
            self._get(method)
            return render(request, ResultView.template_name, self.data)
        return redirect('/')

    def _get(self, method):
        self.info = get_info(method, ResultView.form_fields)  # Получает всю информацию из формы
        self.urls = get_urls(method)  # Получает сайты с формы
        self.vk = vk_pars(self.info)  # Находим пользователя в VK
        self.screen_names = get_screen_names(self.urls,
                                             self.vk)  # Получает скрин неймы из всех сайтов из формы и скрин нейм из вк
        self.sherlock = sherlock(self.screen_names)  # Находим всех пользователей с никами из screen_names
        self.convert_url = get_convert_url(self.info, self.urls)  # Собираем ссылку с данными для pdf

        self.parse()

    def parse(self):
        """ Parsing sites """

        # Calling the parsing methods
        pars = get_pars(self.urls, self.sherlock, self.screen_names)

        self.data = {
            'info': self.info,
            'to_pdf': self.convert_url,
            'vk': self.vk,
            'github': pars.get('github.com'),
            'habr': pars.get('habr.com'),
            'linkedin': pars.get('www.linkedin.com'),
            'codeforces': pars.get('codeforces.com')
        }


def index(request):
    return render(request, 'main/index.html', {'form': MainForm()})


def convert(request):
    req = re.search(r'\'(.*)\'', str(request)).group().replace('\'', '')
    try:
        client = pdfcrowd.HtmlToPdfClient('dibiloid335', 'e6e7f5a5560117dc615690ca43311a71')
        site = 'http://84.201.152.104:8000' + req
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


def e_handler500(request):
    return render(request, 'main/errors/500.html')


def e_handler404(request, exception):
    return render(request, 'main/errors/404.html')

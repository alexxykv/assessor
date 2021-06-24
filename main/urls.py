from django.urls import path
from main.views import ResultView
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('result', ResultView.as_view(), name='result'),
    path('result/convert', views.convert, name='convert')
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('result', views.result, name='result'),
    path('result2/', views.result2, name='result2'),
    path('result/convert', views.convert, name='convert')
]

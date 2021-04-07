from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('result', views.result, name='result'),
    path('alpha', views.alpha, name="alpha"),
    path('alpha_result', views.alpha_result, name="alpha_result")

]

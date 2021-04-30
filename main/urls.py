from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('vk_result', views.vk_result, name='vk_result')
]

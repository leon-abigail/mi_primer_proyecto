
from django.urls import path
from django.http import HttpResponse
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hola_mundo/', views.hola_mundo, name='hola_mundo'),
]

from django.urls import path
from django.http import HttpResponse
from .import views

urlpatterns = [
   path("hola-mundo/", views.hola_mundo, name="hola_mundo"),
]

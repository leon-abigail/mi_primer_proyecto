from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.listar_productos, name='listar_productos'),
    path('productos/nuevo/', views.cargar_producto, name='cargar_producto'),

]

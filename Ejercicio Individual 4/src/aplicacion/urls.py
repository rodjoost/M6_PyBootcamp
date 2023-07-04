from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='index'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('inicio/', views.inicio, name='index'),
    path('registro/', views.registro, name='registro'), 
]

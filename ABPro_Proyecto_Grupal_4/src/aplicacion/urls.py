from django.urls import path
from . import views

urlpatterns=[
    path('', views.landing_page, name='landing_page'),
    path('home/', views.home, name='home'),
    path('formulario/',views.formulario, name='formulario'),
    path('mostrar_proveedor/',views.mostrar_proveedor, name='mostrar_proovedor'),

]

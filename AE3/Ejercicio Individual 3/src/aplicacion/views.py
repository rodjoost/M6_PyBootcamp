from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})


def inicio(request):
    return render(request, "index.html")
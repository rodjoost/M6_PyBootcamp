from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.contrib import messages

# Create your views here.


def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})


def inicio(request):
    return render(request, "index.html")

"""
def registro(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirecciona a pagina luego de registro exitoso
    else:
        form = UserRegistrationForm()
    return render(request, 'registro.html', {'form': form})
"""

def registro(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Se ha creado el usuario {username}')
            return redirect('index')
    else:
        form = UserRegistrationForm()
    
    context = {'form': form}
    return render(request, 'registro.html', context)

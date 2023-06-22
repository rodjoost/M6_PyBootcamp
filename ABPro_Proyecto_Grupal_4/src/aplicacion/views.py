from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Clientes, Proveedor 
from .forms import UserRegistrationForm, ProveedorForm


# Create your views here.
def home(request):
    clientes = Clientes.objects.all()
    usuarios_extra = ["Gabriel", "Pedro", "Juan", "Diego", "Pedro"]
    context = {
        "clientes": clientes,
        "usuarios_extra": usuarios_extra
    }
    return render (request,'clientes.html',context=context)

# Create your views here.

def landing_page(request):

    return render(request,'index.html')

def formulario(request):
    form = ProveedorForm()

    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            print(form)
            proveedor = Proveedor()
            proveedor.nombre = form.cleaned_data['nombre']
            proveedor.email = form.cleaned_data['email']
            proveedor.celular = form.cleaned_data['celular']
            proveedor.save()
        else:
            print("Datos invalidos")
        return redirect('/mostrar_proveedor')
    context = {'form': form}

    return render(request, 'formulario.html', context=context)

def mostrar_proveedor(request):

    datos = Proveedor.objects.all()

    context = {'proveedor': datos}

    return render(request, 'mostrar_proveedor.html', context=context)
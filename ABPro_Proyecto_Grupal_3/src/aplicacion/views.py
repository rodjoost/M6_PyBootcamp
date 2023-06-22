from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Clientes


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


from django.shortcuts import render

# Create your views here.
from Girekstudio.models import *
from Home.models import *
from django.contrib import messages


def index(request):
    contexto = {
                'marca_benitez': Marca_benitez.objects.all().first(),
                'empresas': Empresas.objects.all(),

    }

    return render(request, 'index.html', contexto)

def empresa(request):
    contexto = {
                'marca_benitez': Marca_benitez.objects.all().first(),

    }

    return render(request, 'about.html', contexto)



def trabaja(request):
    contexto = {
                'marca_benitez': Marca_benitez.objects.all().first(),

    }

    return render(request, 'trabaja.html', contexto)

def contacto(request):
    contexto = {
                'marca_benitez': Marca_benitez.objects.all().first(),

    }

    return render(request, 'contact-us.html', contexto)



from django.shortcuts import render

# Create your views here.
from Delifrus.models import *

def index_delifrus(request):
    contexto ={
        'marca': Marca.objects.all().first(),
        'categorias': Clasif_producto.objects.all(),
        'productos': Producto.objects.all().order_by('-id'),


    }
    return render(request, 'delifrus/index_delifrus.html', contexto)

def nosotros_delifrus(request):
    contexto ={
        'marca': Marca.objects.all().first(),


    }
    return render(request, 'delifrus/about.html', contexto)


def productos_delifrus(request):
    contexto ={
        'marca': Marca.objects.all().first(),


    }
    return render(request, 'delifrus/product.html', contexto)

def contacto_delifrus(request):
    contexto ={
        'marca': Marca.objects.all().first(),


    }
    return render(request, 'delifrus/contact.html', contexto)
from django.shortcuts import render

# Create your views here.
from Niska.models import *

def index_niska(request):
    contexto ={
        'editable': Editable.objects.all().first(),
        'marca': Marca.objects.all().first(),
        'categorias': Clasif_producto.objects.all(),
        'productos': Producto.objects.all().order_by('-id'),
    }
    return render(request, 'niska/index_niska.html', contexto)

def nosotros_niska(request):
    contexto ={
        'editable': Editable.objects.all().first(),
        'marca': Marca.objects.all().first(),
    }
    return render(request, 'niska/about.html', contexto)


def productos_niska(request):
    contexto ={
        'editable': Editable.objects.all().first(),
        'marca': Marca.objects.all().first(),
        'categorias': Clasif_producto.objects.all(),
        'productos': Producto.objects.all().order_by('-id'),
    }
    return render(request, 'niska/product.html', contexto)


def productos_cate_niska(request, id):

    contexto = {
        'editable': Editable.objects.all().first(),
        'marca': Marca.objects.all().first(),
        'categorias': Clasif_producto.objects.all(),
        'productos': Producto.objects.filter(clasif_id=id),
    }
    return render(request, 'niska/demo-seo-2-shop.html', contexto)

def producto_id_niska(request, n):
    product = Producto.objects.get(id=n)
    contexto = {
        'editable': Editable.objects.all().first(),
        'marca': Marca.objects.all().first(),
        'categorias': Clasif_producto.objects.all(),
        'product': Producto.objects.get(id=n),
        'producto_imagen' : Producto_Imagen.objects.filter(producto=product),
    }
    return render(request, 'niska/product_detail.html', contexto)

def contacto_niska(request):
    contexto ={
        'editable': Editable.objects.all().first(),
        'marca': Marca.objects.all().first(),


    }
    return render(request, 'niska/contact.html', contexto)
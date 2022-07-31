from django.shortcuts import render

# Create your views here.
from Delifrus.models import *

def index_delifrus(request):
    contexto ={
        'editable': Editable.objects.all().first(),
        'marca': Marca.objects.all().first(),
        'categorias': Clasif_producto.objects.all(),
        'productos': Producto.objects.all().order_by('-id'),
    }
    return render(request, 'delifrus/index_delifrus.html', contexto)

def nosotros_delifrus(request):
    contexto ={
        'editable': Editable.objects.all().first(),
        'marca': Marca.objects.all().first(),
    }
    return render(request, 'delifrus/about.html', contexto)


def productos_delifrus(request):
    contexto ={
        'editable': Editable.objects.all().first(),
        'marca': Marca.objects.all().first(),
        'categorias': Clasif_producto.objects.all(),
        'productos': Producto.objects.all().order_by('-id'),
    }
    return render(request, 'delifrus/product.html', contexto)


def productos_cate_delifrus(request, id):

    contexto = {
        'editable': Editable.objects.all().first(),
        'marca': Marca.objects.all().first(),
        'categorias': Clasif_producto.objects.all(),
        'productos': Producto.objects.filter(clasif_id=id),
    }
    return render(request, 'delifrus/demo-seo-2-shop.html', contexto)

def producto_id_delifrus(request, n):
    product = Producto.objects.get(id=n)
    contexto = {
        'editable': Editable.objects.all().first(),
        'marca': Marca.objects.all().first(),
        'categorias': Clasif_producto.objects.all(),
        'product': Producto.objects.get(id=n),
        'producto_imagen' : Producto_Imagen.objects.filter(producto=product),
    }
    return render(request, 'delifrus/product_detail.html', contexto)

def contacto_delifrus(request):
    contexto ={
        'editable': Editable.objects.all().first(),
        'marca': Marca.objects.all().first(),


    }
    return render(request, 'delifrus/contact.html', contexto)
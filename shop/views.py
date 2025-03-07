from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from shop.models import *


def index_colexin(request):
    contexto ={
        'marca': Marca.objects.all().first(),
        'categories': Category.objects.all(),
        'products': Product.objects.all().order_by('-id'),
    }
    return render(request, 'colexin/demo-decor-store.html', contexto)

def productos_colexin(request):
    products = Product.objects.all() # Filtra productos por categoría

    query = request.GET.get('q')  # Obtiene el término de búsqueda de la URL
    if query:
        products = products.filter(name__icontains=query)  #  productos que contengan el término de búsqueda

    contexto = {
        'marca': Marca.objects.all().first(),
        'categories': Category.objects.all(),
        'products': products,
        'query': query,  # Para mantener el valor en la barra de búsqueda
    }
    return render(request, 'colexin/demo-decor-store-products.html', contexto)




def productos_cate_colexin(request, cate):
    category = get_object_or_404(Category, name=cate)  # Obtiene la categoría o muestra 404 si no existe
    products = Product.objects.filter(category=category)  # Filtra productos por categoría

    query = request.GET.get('q')  # Obtiene el término de búsqueda de la URL
    if query:
        products = products.filter(name__icontains=query)  # Filtra productos que contengan el término de búsqueda

    contexto = {
        'marca': Marca.objects.all().first(),
        'categories': Category.objects.all(),
        'category': category,
        'products': products,
        'query': query,  # Para mantener el valor en la barra de búsqueda
    }
    return render(request, 'colexin/demo-decor-store-products_cate.html', contexto)

def producto_id_colexin(request, n):
    product = Product.objects.get(id=n)
    contexto = {
        'marca': Marca.objects.all().first(),
        'categorias': Category.objects.all(),
        'categories': Category.objects.all(),
        'product': Product.objects.get(id=n),
    }
    return render(request, 'colexin/demo-decor-store-single-product.html', contexto)
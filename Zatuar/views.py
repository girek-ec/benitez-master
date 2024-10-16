from itertools import product

from PIL.ImageEnhance import Color
from django.core.mail import EmailMultiAlternatives
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

# Create your views here.
from Home.models import *
from django.shortcuts import *
from Zatuar.models import *


def index_zatuar(request):
    contexto = {
        "sliders": Slider.objects.all().order_by("orden"),
        'zatuar': Zatuar_marca.objects.all().first(),
        'contacto': Contacto_empresa.objects.all().first(),
        'redes': Redes_sociales.objects.all().first(),
        'personalizacion': Personalizaion_Poducto.objects.all(),
        'proceso': Proceso.objects.all().first(),
        'galeri_proces': Galeria_Proceso.objects.all(),
        'catalogo': Descarga.objects.all().first(),
        'identidad': Identidad.objects.all(),
        'detalles': Detalles.objects.first(),
        'linea': Linea_Product.objects.all(),
        'clientes': Cliente.objects.all(),
    }
    return render(request, "zatuar/index_zatuar.html", contexto)

def empresa_zatuar(request):
    contexto={
        'zatuar': Zatuar_marca.objects.all().first(),
        'beneficio':Beneficios.objects.all(),
        'proceso': Proceso.objects.all().first(),
        'contacto':Contacto_empresa.objects.all().first(),
        'redes': Redes_sociales.objects.all().first(),
    }
    return render(request, "zatuar/empresa.html", contexto)


def linea(request):
    contexto = {
        'clasif_producto': Clasif_producto.objects.all(),
        'product': Product.objects.all().order_by('-id'),
        'producto_personalizacion':Producto_Personalizacion.objects.all(),
        'zatuar': Zatuar_marca.objects.all().first(),
        'contacto': Contacto_empresa.objects.all().first(),
        'redes': Redes_sociales.objects.all().first(),
        'linea': Linea_Product.objects.all(),
    }
    return render(request,"zatuar/productos.html", contexto)

def linea_cate(request, lineaa):
    contexto = {
        'clasif_producto': Clasif_producto.objects.filter(linea__linea=lineaa),
        'product': Product.objects.filter(clasif__linea__linea=lineaa),
        'zatuar': Zatuar_marca.objects.all().first(),
        'contacto': Contacto_empresa.objects.all().first(),
        'linea': Linea_Product.objects.all(),
        'redes': Redes_sociales.objects.all().first(),

    }
    return render(request, 'zatuar/productos.html', contexto,)


def producto_zatuar(request):
    contexto = {
        'clasif_producto': Clasif_producto.objects.all(),
        'product': Product.objects.all().order_by('-id'),
        'producto_personalizacion':Producto_Personalizacion.objects.all(),
        'zatuar': Zatuar_marca.objects.all().first(),
        'contacto': Contacto_empresa.objects.all().first(),
        'redes': Redes_sociales.objects.all().first(),
        'linea': Linea_Product.objects.all(),
    }
    return render(request, "zatuar/productos.html", contexto)


def producto_cate_zatuar(request, id):
    contexto = {
        'product': Product.objects.filter(clasif_id=id),
        'clasif_producto': Clasif_producto.objects.all(),
        'colors': Colores.objects.all(),
        'zatuar': Zatuar_marca.objects.all().first(),
        'contacto': Contacto_empresa.objects.all().first(),
        'redes': Redes_sociales.objects.all().first(),
        'linea': Linea_Product.objects.all(),

    }
    return render(request, 'zatuar/productos.html', contexto, )


def producto_id_zatuar(request, id):
    contexto = {
        'clasif_producto': Clasif_producto.objects.all(),
        'product': Product.objects.get(id=id),
        'imagenes_productos' : Producto_Imagen.objects.filter(producto_id=id),
        'tallas_productos': Tallas_Product.objects.filter(producto_id=id),
        'colores_productos': Color_Product.objects.filter(producto_id=id),
        'fichapdf': Ficha_Product.objects.all(),
        'materiales': Materiales.objects.get(product=id),
        'texturas': Texturs.objects.get(product=id),
        'zatuar': Zatuar_marca.objects.all().first(),
        'contacto': Contacto_empresa.objects.all().first(),
        'redes': Redes_sociales.objects.all().first(),

    }
    return render(request, 'zatuar/product.html', contexto, )

def clientes_zatuar(request):
    contexto={
        'client':Cliente.objects.all(),
        'zatuar': Zatuar_marca.objects.all().first(),
        'contacto': Contacto_empresa.objects.all().first(),
        'redes': Redes_sociales.objects.all().first(),

    }
    return render(request, 'zatuar/clientes.html', contexto)

def clientes_id_zatuar(request,id):
    client=Cliente.objects.get(id=id)
    zatuar=Zatuar_marca.objects.get()
    contacto=Contacto_empresa.objects.all().first()
    redes= Redes_sociales.objects.all().first()
    return render(request,'zatuar/product-client.html',
                              {'client': client,
                               'zatuar':zatuar,
                               'contacto':contacto,
                               'redes':redes,
                      })


def error404_zatuar(request, exception):
    return render(request, "zatuar/page-404.html", status=404)

def contacto_zatuar(request):
    contexto = {
        'zatuar': Zatuar_marca.objects.all().first(),
        'contacto': Contacto_empresa.objects.all().first(),
        'redes': Redes_sociales.objects.all().first(),
    }
    return render(request, 'zatuar/contact-us.html', contexto)














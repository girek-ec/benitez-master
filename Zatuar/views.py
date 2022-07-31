from itertools import product

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
    }
    return render(request, "zatuar/productos.html", contexto)


def producto_cate_zatuar(request, id):
    contexto = {
        'clasif_producto': Clasif_producto.objects.all(),
        'product': Product.objects.filter(clasif_id=id),
        'zatuar': Zatuar_marca.objects.all().first(),
        'contacto': Contacto_empresa.objects.all().first(),
        'redes': Redes_sociales.objects.all().first(),

    }
    return render(request, 'zatuar/productos.html', contexto, )


def producto_id_zatuar(request, id):
    contexto = {
        'clasif_producto': Clasif_producto.objects.all(),
        'product': Product.objects.get(id=id),
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
    galeria_cliente=Galeria_Cliente.objects.filter(cliente=client)
    zatuar=Zatuar_marca.objects.get()
    contacto=Contacto_empresa.objects.all().first()
    redes= Redes_sociales.objects.all().first()
    return render(request,'zatuar/product-client.html',
                              {'client': client,
                               'galeria_cliente':galeria_cliente,
                               'zatuar':zatuar,
                               'contacto':contacto,
                               'redes':redes,
                      })


def error404_zatuar(request):
    return render(request, "zatuar/page-404.html")

def contacto_zatuar(request):
    contexto = {
        'zatuar': Zatuar_marca.objects.all().first(),
        'contacto': Contacto_empresa.objects.all().first(),
        'redes': Redes_sociales.objects.all().first(),
    }
    if request.POST:
        enviar_email(request,request.POST['subject'],request.POST['email'],"zatuar.ec@gmail.com",request.POST['message'],request.POST['name'])
    return render(request, 'zatuar/contact-us.html', contexto)



def enviar_email(request,asunto,from_email,to,mensaje,nombre):
    asunto = asunto
    from_email = from_email
    to = to
    text_content = 'Este mnsaje es importante.'
    html_content = '<p>This is an <strong>important</strong> message.</p>' \
                   '<img src="http://zatuar.com/static/img/zatuar/favizatuar.png"><br>' + mensaje
    msg = EmailMultiAlternatives(asunto, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    # print from_email













from itertools import product
from unicodedata import category

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from Girekstudio.models import *
from Home.models import *
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages


# Create your views here.
from benitez import settings



def index_girekstudio(request):
    contexto = {
        'editable': Editables.objects.all().first(),
        'planes': Planes.objects.all(),
        'proyecto': Proyecto.objects.all().order_by('orden'),
        'servicios': Servicio.objects.all().order_by("orden"),
        'equipos': Equipo.objects.all(),
        'frases': Frase.objects.all(),
        'clientes': Cliente.objects.all(),
        'marca': Marca.objects.all().first(),
        'contacto_empresa': Contacto_empresa.objects.all().first(),
    }

    return render(request, 'girekstudio/demo-branding-agency.html', contexto)

def estudio_girekstudio(request):
    contexto = {
        'marca': Marca.objects.all().first(),
        'editable': Editables.objects.all().first(),
        'clientes': Cliente.objects.all(),
        'frases': Frase.objects.all(),
        'servicios': Servicio.objects.all().order_by("orden"),
        'contacto_empresa': Contacto_empresa.objects.all().first(),
        'equipos': Equipo.objects.all(),

    }
    return render(request, 'girekstudio/demo-branding-agency-about.html', contexto)

def servicios_girekstudio(request):
    contexto = {
        'marca': Marca.objects.all().first(),
        'editable': Editables.objects.all().first(),
        'clientes': Cliente.objects.all(),
        'servicios': Servicio.objects.all().order_by("orden"),
        'listservicios' : Lista_servicio.objects.all(),
        'planes' :  Planes.objects.all(),
        'planes_listas' : Plan_list.objects.all(),
        'contacto_empresa': Contacto_empresa.objects.all().first(),
    }
    return render(request, 'girekstudio/demo-branding-agency-services.html', contexto)


def serviciosdescripcion_girekstudio(request, n,):
    contexto = {
        'marca': Marca.objects.all().first(),
        'clientes': Cliente.objects.all(),
        'editable': Editables.objects.all().first(),
        'servicio' : Servicio.objects.get(id=n),
        'servicios': Servicio.objects.all().order_by("orden"),
        'imag_video_serv' : Imag_Video_Servicio.objects.filter(servicio__titulo=servicios_girekstudio),
        'listservicios': Lista_servicio.objects.all(),
        'planes' : Planes.objects.filter(categoria_id=n),
        'planes_listas': Plan_list.objects.filter(plan_serv=n),
        'contacto_empresa': Contacto_empresa.objects.all().first(),
    }
    return render(request, 'girekstudio/demo-branding-agency-services-detail.html', contexto)




def contacto_girekstudio(request):
    contexto = {
        'marca': Marca.objects.all().first(),
        'editable': Editables.objects.all().first(),
        'servicios': Servicio.objects.all().order_by("orden"),
        'clientes': Cliente.objects.all(),
        'contacto_empresa': Contacto_empresa.objects.all(),
        'sucursales' : Sucursales.objects.all(),
        'contacto_empresa': Contacto_empresa.objects.all().first(),

    }
    return render(request, 'girekstudio/demo-branding-agency-contact.html', contexto)



def portafolio_girekstudio(request):
    contexto = {
        'marca': Marca.objects.all().first(),
        'editable': Editables.objects.all().first(),
        'proyectos':  Proyecto.objects.all().order_by('orden'),
        'servicios': Servicio.objects.all().order_by("orden"),
        'portafolios':  Portafolio.objects.all(),
        'clientes':  Cliente.objects.all(),
        'contacto_empresa': Contacto_empresa.objects.all().first(),
    }
    return render(request, 'girekstudio/demo-branding-agency-portfolio.html', contexto)

def portafolioimagen_girekstudio(request, n):
    # proyecto= Proyecto.objects.get(id=n),
    contexto = {
        'marca': Marca.objects.all().first(),
        'editable': Editables.objects.all().first(),
        'portaf': Portafolio.objects.all(),
        'servicios': Servicio.objects.all().order_by("orden"),
        'proyecto': Proyecto.objects.get(id=n),
        'imagenesproyecto': Imagenesproyecto.objects.filter(proyecto=n).order_by('id'),
        'clientes': Cliente.objects.all(),
        'contacto_empresa': Contacto_empresa.objects.all().first(),
    }



    return render(request, 'girekstudio/demo-branding-agency-single-project-slider.html', contexto)


def tienda_girekstudio(request):
    contexto = {
        'marca': Marca.objects.all().first(),
        'editable': Editables.objects.all().first(),
        'servicios': Servicio.objects.all().order_by("orden"),
        'categorias': Clasif_producto.objects.all(),
        'productos': Producto.objects.all().order_by('-id'),
        'contacto_empresa': Contacto_empresa.objects.all(),

    }

    return render(request, 'girekstudio/demo-branding-agency-store.html', contexto)

def producto_cate_girekstudio(request, id):

    contexto = {
        'marca': Marca.objects.all().first(),
        'editable': Editables.objects.all().first(),
        'categorias': Clasif_producto.objects.all(),
        'servicios': Servicio.objects.all().order_by("orden"),
        'productos': Producto.objects.filter(clasif_id=id),
        'producto_imagen' : Producto_Imagen.objects.filter(producto=product),
        'contacto_empresa': Contacto_empresa.objects.all(),
    }

    return render(request, 'girekstudio/demo-branding-agency-store.html', contexto)

def producto_id_girekstudio(request, n):
    product = Producto.objects.get(id=n)
    contexto = {
        'marca': Marca.objects.all().first(),
        'editable': Editables.objects.all().first(),
        'categorias': Clasif_producto.objects.all(),
        'servicios': Servicio.objects.all().order_by("orden"),
        'product': Producto.objects.get(id=n),
        'producto_imagen' : Producto_Imagen.objects.filter(producto=product),
        'contacto_empresa': Contacto_empresa.objects.all(),
    }

    return render(request, 'girekstudio/demo-branding-agency-product.html', contexto)

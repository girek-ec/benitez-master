from itertools import product

from django.db.models import Count, Q
from unicodedata import category

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

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
        'servicios': Servicio.objects.all(),
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
        'imag_video_serv' : Imag_Video_Servicio.objects.filter(servicio=n),
        'listservicios': Lista_servicio.objects.all(),
        'planes' : Planes.objects.filter(categoria_id=n).order_by('orden'),
        'contacto_empresa': Contacto_empresa.objects.all().first(),
    }
    return render(request, 'girekstudio/demo-branding-agency-services-detail.html', contexto)


def contacto_girekstudio(request):
    contexto = {
        'marca': Marca.objects.all().first(),
        'editable': Editables.objects.all().first(),
        'servicios': Servicio.objects.all().order_by("orden"),
        'clientes': Cliente.objects.all(),
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
        'contacto_empresa': Contacto_empresa.objects.all().first(),

    }

    return render(request, 'girekstudio/demo-branding-agency-store.html', contexto)

def producto_cate_girekstudio(request, id):

    contexto = {
        'marca': Marca.objects.all().first(),
        'editable': Editables.objects.all().first(),
        'categorias': Clasif_producto.objects.all(),
        'servicios': Servicio.objects.all().order_by("orden"),
        'productos': Producto.objects.filter(clasif_id=id),
        'producto_imagen' : Producto_Imagen.objects.all(),
        'contacto_empresa': Contacto_empresa.objects.all().first(),
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
        'contacto_empresa': Contacto_empresa.objects.all().first(),
    }

    return render(request, 'girekstudio/demo-branding-agency-product.html', contexto)



def blog_girekstudio(request, categoria_slug=None):
    publicaciones = (
        Blog.objects.filter(activo=True, fecha_publicacion__lte=timezone.now())
        .select_related('categoria')
        .prefetch_related('galeria')
    )
    categoria_actual = None

    if categoria_slug:
        categoria_actual = get_object_or_404(
            CategoriaBlog,
            slug=categoria_slug,
            activo=True,
        )
        publicaciones = publicaciones.filter(categoria=categoria_actual)

    categorias = (
        CategoriaBlog.objects.filter(activo=True)
        .annotate(
            total_publicaciones=Count(
                'publicaciones',
                filter=Q(
                    publicaciones__activo=True,
                    publicaciones__fecha_publicacion__lte=timezone.now(),
                ),
            )
        )
        .filter(total_publicaciones__gt=0)
    )
    pagina = Paginator(publicaciones, 16).get_page(request.GET.get('page'))

    contexto = {
        'marca': Marca.objects.all().first(),
        'editable': Editables.objects.all().first(),
        'contacto_empresa': Contacto_empresa.objects.all().first(),
        'servicios': Servicio.objects.all().order_by('orden'),
        'clientes': Cliente.objects.all(),
        'frases': Frase.objects.all(),
        'publicaciones': pagina,
        'categorias_blog': categorias,
        'categoria_actual': categoria_actual,
    }
    return render(request, 'girekstudio/lista.html', contexto)


def blog_detalle_girekstudio(request, slug):
    publicacion = get_object_or_404(
        Blog.objects
        .select_related('categoria')
        .prefetch_related('galeria'),
        slug=slug,
        activo=True,
        fecha_publicacion__lte=timezone.now(),
    )

    # Publicaciones relacionadas:
    # únicamente de la misma categoría y excluyendo la publicación actual
    relacionados = (
        Blog.objects.filter(
            categoria=publicacion.categoria,
            activo=True,
            fecha_publicacion__lte=timezone.now(),
        )
        .exclude(pk=publicacion.pk)
        .select_related('categoria')
        .order_by('-fecha_publicacion')[:12]
    )

    contexto = {
        'marca': Marca.objects.all().first(),
        'editable': Editables.objects.all().first(),
        'contacto_empresa': Contacto_empresa.objects.all().first(),
        'servicios': Servicio.objects.all().order_by('orden'),
        'clientes': Cliente.objects.all(),
        'frases': Frase.objects.all(),
        'publicacion': publicacion,
        'relacionados': relacionados,
    }

    return render(
        request,
        'girekstudio/detalle.html',
        contexto
    )
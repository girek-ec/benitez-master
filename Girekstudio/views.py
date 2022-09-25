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
                'servicio': Servicio.objects.all().order_by("orden"),
                'servicios': Servicio.objects.all().order_by("orden"),
                'marca': Marca.objects.all().first(),
                'contacto_empresa': Contacto_empresa.objects.all(),



                }
    if request.POST:
        email = Suscripcion_Email.objects.create(email=request.POST['email'])
        email.save()
        messages.add_message(request, messages.SUCCESS, "Gracias por preferirnos!")
    return render(request, 'girekstudio/index_girekstudio.html', contexto)

def estudio_girekstudio(request):
    contexto = {
        'marca': Marca.objects.all().first(),
        'clientes': Cliente.objects.all(),
        'frases': Frase.objects.all(),
        'servicios': Servicio.objects.all().order_by("orden"),
        'contacto_empresa': Contacto_empresa.objects.all(),

    }
    if request.POST:
        email = Suscripcion_Email.objects.create(email=request.POST['email'])
        email.save()
        messages.add_message(request, messages.SUCCESS, "Gracias por preferirnos!")

    return render(request, 'girekstudio/demo-seo-2-about.html', contexto)

def servicios_girekstudio(request):
    contexto = {
        'marca': Marca.objects.all().first(),
        'clientes': Cliente.objects.all(),
        'servicios': Servicio.objects.all().order_by("orden"),
        'contacto_empresa': Contacto_empresa.objects.all(),

    }
    if request.POST:
        email = Suscripcion_Email.objects.create(email=request.POST['email'])
        email.save()
        messages.add_message(request, messages.SUCCESS, "Gracias por preferirnos!")

    return render(request, 'girekstudio/demo-seo-2-services.html', contexto)


def serviciosdescripcion_girekstudio(request, n):
    contexto = {
        'marca': Marca.objects.all().first(),
        'clientes': Cliente.objects.all(),
        'servicio' : Servicio.objects.get(id=n),
        'imag_video_serv' : Imag_Video_Servicio.objects.filter(servicio__titulo=servicios_girekstudio),
        'planes' : Planes.objects.filter(categoria_id=n),
        'contacto_empresa': Contacto_empresa.objects.all(),
    }
    if request.POST:
        email = Suscripcion_Email.objects.create(email=request.POST['email'])
        email.save()
        messages.add_message(request, messages.SUCCESS, "Gracias por preferirnos!")


    return render(request, 'girekstudio/demo-seo-2-services-detail.html', contexto)




def contacto_girekstudio(request):
    if request.method == "POST":
        subject = request.POST['subject']
        email = request.POST['email']
        celular = request.POST['celular']
        message = request.POST['message']

        template = render_to_string('girekstudio/email_template.html',{
            'subject': subject,
            'email': email,
            'celular': celular,
            'message': message,

        })

        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['girekstudio@gmail.com']
        )

        email.fail_silently = False
        email.send()

        messages.success(request, 'Se ha enviado tu correo.' )

    contexto = {
        'marca': Marca.objects.all().first(),
        'clientes': Cliente.objects.all(),
        'contacto_empresa': Contacto_empresa.objects.all(),

    }
    if request.POST:
        email = Suscripcion_Email.objects.create(email=request.POST['email'])
        email.save()
        messages.add_message(request, messages.SUCCESS, "Gracias por preferirnos!")

    return render(request, 'girekstudio/demo-seo-2-contact-us.html', contexto)



def portafolio_girekstudio(request):
    contexto = {
        'marca': Marca.objects.all().first(),
        'proyectos':  Proyecto.objects.all().order_by('orden'),
        'portafolios':  Portafolio.objects.all(),
        'clientes':  Cliente.objects.all(),
        'contacto_empresa': Contacto_empresa.objects.all(),
    }
    if request.POST:
        email = Suscripcion_Email.objects.create(email=request.POST['email'])
        email.save()
        messages.add_message(request, messages.SUCCESS, "Gracias por preferirnos!")

    return render(request, 'girekstudio/demo-seo-2-proyectos.html', contexto)

def portafolioimagen_girekstudio(request, n):
    # proyecto= Proyecto.objects.get(id=n),
    contexto = {
        'marca': Marca.objects.all().first(),
        'portaf': Portafolio.objects.all(),
        'proyecto': Proyecto.objects.get(id=n),
        'imagenesproyecto': Imagenesproyecto.objects.filter(proyecto=n),
        'clientes': Cliente.objects.all(),
        'contacto_empresa': Contacto_empresa.objects.all(),
    }



    return render(request, 'girekstudio/demo-seo-2-proyecto-id.html', contexto)


def tienda_girekstudio(request):
    contexto = {
        'marca': Marca.objects.all().first(),
        'categorias': Clasif_producto.objects.all(),
        'productos': Producto.objects.all().order_by('-id'),
        'contacto_empresa': Contacto_empresa.objects.all(),

    }
    if request.POST:
        email = Suscripcion_Email.objects.create(email=request.POST['email'])
        email.save()
        messages.add_message(request, messages.SUCCESS, "Gracias por preferirnos!")
    return render(request, 'girekstudio/demo-seo-2-shop.html', contexto)

def producto_cate_girekstudio(request, id):

    contexto = {
        'marca': Marca.objects.all().first(),
        'categorias': Clasif_producto.objects.all(),
        'productos': Producto.objects.filter(clasif_id=id),
        'contacto_empresa': Contacto_empresa.objects.all(),
    }
    if request.POST:
        email = Suscripcion_Email.objects.create(email=request.POST['email'])
        email.save()
        messages.add_message(request, messages.SUCCESS, "Gracias por preferirnos!")
    return render(request, 'girekstudio/demo-seo-2-shop.html', contexto)

def producto_id_girekstudio(request, n):
    product = Producto.objects.get(id=n)
    contexto = {
        'marca': Marca.objects.all().first(),
        'categorias': Clasif_producto.objects.all(),
        'product': Producto.objects.get(id=n),
        'producto_imagen' : Producto_Imagen.objects.filter(producto=product),
        'contacto_empresa': Contacto_empresa.objects.all(),

    }
    if request.POST:
        email = Suscripcion_Email.objects.create(email=request.POST['email'])
        email.save()
        messages.add_message(request, messages.SUCCESS, "Gracias por preferirnos!")
    return render(request, 'girekstudio/demo-seo-2-shop-product.html', contexto)

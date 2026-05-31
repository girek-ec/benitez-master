from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from Eraly.models import *

def _contexto_eraly():
    """
    Contexto base para todas las vistas
    """
    contexto = {
        'empresa': ConfiguracionEmpresa.objects.first(),
        # 👇 CORREGIDO: ordenar por 'orden'
        'landings_menu': LandingPage.objects.filter(activo=True).order_by('orden'),
        'servicios_menu': ServicioProducto.objects.filter(activo=True).order_by('orden'),
    }
    return contexto

def landing(request, slug):
    contexto = _contexto_eraly()
    contexto.update({
        'landing': LandingPage.objects.filter(
            slug=slug,
            activo=True
        ).first(),
        'beneficios': BeneficioLanding.objects.filter(
            landing__slug=slug
        ).order_by('orden'),
        'tabs': [],
        'planes': PlanLanding.objects.filter(
            landing__slug=slug
        ).prefetch_related('caracteristicas').order_by('orden'),
    })
    return render(request, 'eraly/landing.html', contexto)

def base_eraly(request):
    return render(request, 'eraly/navbar.html', _contexto_eraly())

def index_eraly(request):
    contexto = _contexto_eraly()

    return render(
        request,
        'eraly/eraly-index.html',
        contexto
    )
def soluciones_eraly(request):
    return render(request, 'eraly/eraly-soluciones.html', _contexto_eraly())

def soluciones_eraly_id(request, id):
    contexto = _contexto_eraly()
    contexto.update({
        'solucion': LandingPage.objects.filter(
            id=id,
            activo=True
        ).first(),
        'beneficios': BeneficioLanding.objects.filter(
            landing__id=id
        ).order_by('orden'),
        'tabs': [],
        'planes': PlanLanding.objects.filter(
            landing__id=id
        ).prefetch_related('caracteristicas').order_by('orden'),
    })
    return render(request, 'eraly/eraly-apps.html', contexto)

def productos_eraly(request):
    return render(request, 'eraly/eraly-productos.html', _contexto_eraly())

def _landing_servicio(request, slug, template):
    contexto = _contexto_eraly()

    landing_obj = get_object_or_404(
        LandingPage,
        slug=slug,
        activo=True
    )

    contexto.update({
        'landing': landing_obj,
        'beneficios': BeneficioLanding.objects.filter(
            landing=landing_obj
        ).order_by('orden'),
        'tabs': [],
        'planes': PlanLanding.objects.filter(
            landing=landing_obj
        ).prefetch_related('caracteristicas').order_by('orden'),
    })

    return render(request, template, contexto)




def _servicio_producto(request, tipo, template):
    contexto = _contexto_eraly()

    servicio = get_object_or_404(
        ServicioProducto,
        tipo=tipo,
        activo=True
    )

    contexto.update({

        'servicio': servicio,
        'beneficios_servicio': servicio.beneficios.all(),
        'dominios_servicio': servicio.dominios.all(),
        'tipos_web': servicio.tipos_web.all(),
        'planes_servicio': servicio.planes.prefetch_related('caracteristicas').all(),
        'preguntas_servicio': servicio.preguntas.all(),
    })

    return render(request, template, contexto)


def hosting_eraly(request):
    return _servicio_producto(request, 'hosting', 'eraly/eraly-producto_hosting_dominio.html')

def web_eraly(request):

    return _servicio_producto(request, 'web', 'eraly/eraly-producto_pagweb.html')

def correos_eraly(request):
    return _servicio_producto(request, 'correos', 'eraly/eraly-producto_correos.html')

#def facturacion_eraly(request):
#    return _servicio_producto(request, 'facturacion', 'eraly/eraly-producto_facturacion.html')

def apps_eraly(request):
    return _servicio_producto(request, 'apps', 'eraly/eraly-producto_desarrollo_apps.html')




def contacto_eraly(request):
    return render(request, 'eraly/demo-elearning-contact.html', _contexto_eraly())

def eraly_subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            existe = EralyNewsletter.objects.filter(email=email).exists()
            if not existe:
                EralyNewsletter.objects.create(email=email)
                messages.success(request, 'Te has suscrito correctamente.')
            else:
                messages.warning(request, 'Este correo ya está registrado.')
        else:
            messages.error(request, 'Debes ingresar un correo.')
    return redirect(request.META.get('HTTP_REFERER', '/eraly/'))
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render

from Girekstudio.models import Producto
# Create your views here.

from benitez import settings
from Vortice.models import *
from cart.forms import CartAddProductForm


def index_vortice(request):
    contexto ={
        'vortice':Vortice.objects.all().first(),
        'notificaciones': Notificaciones.objects.all().first(),
        'sliders':Coleccion.objects.all(),
        'secciones': Seccion_Cliente.objects.all(),
        'colecciones':Coleccion.objects.all(),
        'tipo_articulos_menu': Tipo_articulo.objects.all(),
        'products': Prod_prenda.objects.all(),
        'servicios' : Servicios.objects.all(),
        'giftCards' : GiftCard.objects.all(),
        'anios' :  Anio.objects.all(),
        'meses' :  Meses.objects.all(),
        'mesmodas' : MesModa.objects.all(),
        'mesmoda_galerias' : MesModa_galeria.objects.all(),
    }
    return render(request, 'vortice/index_vortice.html', contexto)


def seccion_filtro(request,secc):
    contexto ={
        'vortice':Vortice.objects.all().first(),
        'notificaciones': Notificaciones.objects.all().first(),
        'sliders':Coleccion.objects.all(),
        'secciones': Seccion_Cliente.objects.all(),
        'seccion_id': Seccion_Cliente.objects.get(cliente=secc),
        'colecciones':Coleccion.objects.all(),
        'tipo_articulos_menu': Tipo_articulo.objects.all(),
        'tipo_articulos': Tipo_articulo.objects.filter(coleccion__cliente__cliente=secc),
        'products': Prod_prenda.objects.filter(tipo_produc__coleccion__cliente__cliente=secc),
        'servicios' : Servicios.objects.all(),
        'giftCards' : GiftCard.objects.all(),
        'anios' :  Anio.objects.all(),
        'meses' :  Meses.objects.all(),
        'mesmodas' : MesModa.objects.all(),
        'mesmoda_galerias' : MesModa_galeria.objects.all(),
    } 
    return render(request,'vortice/vortice-shop.html', contexto)

def tipo_filtro(request,seccion,tipo):
    contexto ={
        'vortice':Vortice.objects.all().first(),
        'notificaciones': Notificaciones.objects.all().first(),
        'sliders':Coleccion.objects.all(),
        'secciones': Seccion_Cliente.objects.all(),
        'seccion_id': Seccion_Cliente.objects.get(cliente=seccion),
        'colecciones':Coleccion.objects.all(),
        'tipo_articulos_menu': Tipo_articulo.objects.all(),
        'tipo_articulos': Tipo_articulo.objects.filter(coleccion__cliente__cliente=seccion),
        'products': Prod_prenda.objects.filter(tipo_produc__coleccion__cliente__cliente=seccion, tipo_produc__nombre_articulo=tipo),
        'servicios' : Servicios.objects.all(),
        'giftCards' : GiftCard.objects.all(),
        'anios' :  Anio.objects.all(),
        'meses' :  Meses.objects.all(),
        'mesmodas' : MesModa.objects.all(),
        'mesmoda_galerias' : MesModa_galeria.objects.all(),
    }
    return render(request, 'vortice/prendas.html', contexto)

def coleccion_filtro(request,seccion,coleccion):
    contexto ={
        'vortice':Vortice.objects.all().first(),
        'notificaciones': Notificaciones.objects.all().first(),
        'tipo_articulos_menu': Tipo_articulo.objects.all(),
        'sliders':Coleccion.objects.all(),
        'secciones': Seccion_Cliente.objects.all(),
        'seccion_id': Seccion_Cliente.objects.get(cliente=seccion),
        'colecciones':Coleccion.objects.all(),
        'colecciones_id':Coleccion.objects.filter(cliente__cliente=seccion, tema_colec=coleccion ).first(),
        'tipo_articulos': Tipo_articulo.objects.filter(coleccion__cliente__cliente=seccion, coleccion__tema_colec=coleccion ),
        'products': Prod_prenda.objects.filter(tipo_produc__coleccion__tema_colec=coleccion ), 
        'servicios' : Servicios.objects.all(),
        'giftCards' : GiftCard.objects.all(),
        'anios' :  Anio.objects.all(),
        'meses' :  Meses.objects.all(),
        'mesmodas' : MesModa.objects.all(),
        'mesmoda_galerias' : MesModa_galeria.objects.all(),
    }

    return render(request, 'vortice/shop-collection-sub.html', contexto)

def coleccion_filtro_prenda(request,seccion,coleccion,tipo):
    contexto ={
        'vortice':Vortice.objects.all().first(),
        'notificaciones': Notificaciones.objects.all().first(),
        'tipo_articulos_menu': Tipo_articulo.objects.all(),
        'sliders':Coleccion.objects.all(),
        'secciones': Seccion_Cliente.objects.all(),
        'seccion_id': Seccion_Cliente.objects.get(cliente=seccion),
        'colecciones':Coleccion.objects.all(),
        'colecciones_id':Coleccion.objects.filter(cliente__cliente=seccion, tema_colec=coleccion ).first(),
        'tipo_articulos': Tipo_articulo.objects.filter(coleccion__cliente__cliente=seccion, coleccion__tema_colec=coleccion ),
        'products': Prod_prenda.objects.filter(tipo_produc__coleccion__tema_colec=coleccion, tipo_produc__nombre_articulo=tipo ), 
        'servicios' : Servicios.objects.all(),
        'giftCards' : GiftCard.objects.all(),
        'anios' :  Anio.objects.all(),
        'meses' :  Meses.objects.all(),
        'mesmodas' : MesModa.objects.all(),
        'mesmoda_galerias' : MesModa_galeria.objects.all(),
    }
    return render(request, 'vortice/shop-collection-sub.html', contexto)


def producto_detalle(request, id):
    product = Prod_prenda.objects.get(id=id)  # Obtener el producto específico

    # Determinar si el producto tiene tallas o es talla única
    cart_product_form = CartAddProductForm(has_sizes=product.has_sizes)

    contexto = {
        'vortice': Vortice.objects.all().first(),
        'notificaciones': Notificaciones.objects.all().first(),
        'sliders': Coleccion.objects.all(),
        'secciones': Seccion_Cliente.objects.all(),
        'tipo_articulos_menu': Tipo_articulo.objects.all(),
        'colecciones': Coleccion.objects.all(),
        'tipo_articulos': Tipo_articulo.objects.filter(coleccion__cliente__cliente=id),
        'products': product,  # ✅ Usamos la variable `product` ya obtenida
        'productos': Prod_prenda.objects.all(),
        'servicios': Servicios.objects.all(),
        'giftCards': GiftCard.objects.all(),
        'anios': Anio.objects.all(),
        'meses': Meses.objects.all(),
        'mesmodas': MesModa.objects.all(),
        'mesmoda_galerias': MesModa_galeria.objects.all(),
        'cart_product_form': cart_product_form  # ✅ Formulario con opciones dinámicas
    }

    return render(request, 'vortice/product-description-vertical.html', contexto)



def tienda(request):
    contexto ={
    }
    return render(request,'vortice/product-style-05.html', contexto)

def blog(request):
    contexto ={
        'vortice':Vortice.objects.all().first(),
        'notificaciones': Notificaciones.objects.all().first(),
        'tipo_articulos_menu': Tipo_articulo.objects.all(),
        'sliders':Coleccion.objects.all(),
        'secciones': Seccion_Cliente.objects.all(),
        'colecciones':Coleccion.objects.all(),
        'tipo_articulos': Tipo_articulo.objects.all(),
        'anios': Anio.objects.all(),
        'mes': Meses.objects.all(),
        'mesmoda' : MesModa.objects.all().order_by('-mes'),
    }
    return render(request,'vortice/blog-moda.html', contexto)

def post(request,id):
    contexto ={
        'vortice':Vortice.objects.all().first(),
        'notificaciones': Notificaciones.objects.all().first(),
        'tipo_articulos_menu': Tipo_articulo.objects.all(),
        'sliders':Coleccion.objects.all(),
        'secciones': Seccion_Cliente.objects.all(),
        'colecciones':Coleccion.objects.all(),
        'tipo_articulos': Tipo_articulo.objects.all(),
        'coleccion': Coleccion.objects.all(),
        'anios': Anio.objects.all(),
        'mesmoda' : MesModa.objects.get(id=id),
        'moda': MesModa_galeria.objects.filter(mesmoda__id=id),
        'meses': MesModa.objects.all(),
    }
    return render(request,'vortice/moda-mes.html', contexto)

def nosotros(request,):
    contexto ={
        'vortice':Vortice.objects.all().first(),
        'notificaciones': Notificaciones.objects.all().first(),
        'sliders':Coleccion.objects.all(),
        'secciones': Seccion_Cliente.objects.all(),
        'colecciones':Coleccion.objects.all(),
        'tipo_articulos_menu': Tipo_articulo.objects.all(),
        'products': Prod_prenda.objects.all(),
        'servicios' : Servicios.objects.all(),
        'giftCards' : GiftCard.objects.all(),
        'anios' :  Anio.objects.all(),
        'meses' :  Meses.objects.all(),
        'mesmodas' : MesModa.objects.all(),
        'mesmoda_galerias' : MesModa_galeria.objects.all(),
    }
    return render(request,'vortice/about-us.html', contexto)


def giftcard(request,):
    contexto ={
        'vortice':Vortice.objects.all().first(),
        'notificaciones': Notificaciones.objects.all().first(),
        'secciones': Seccion_Cliente.objects.all(),
        'colecciones':Coleccion.objects.all(),
        'tipo_articulos_menu': Tipo_articulo.objects.all(),
        'products': Prod_prenda.objects.all(),
        'giftCards' : GiftCard.objects.all(),
    }
    return render(request,'vortice/giftcard.html', contexto)


def card(request,id):
    contexto ={
        'vortice':Vortice.objects.all().first(),
        'notificaciones': Notificaciones.objects.all().first(),
        'secciones': Seccion_Cliente.objects.all(),
        'colecciones':Coleccion.objects.all(),
        'tipo_articulos_menu': Tipo_articulo.objects.all(),
        'products': Prod_prenda.objects.all(),
        'giftCards' : GiftCard.objects.get(id=id),
    }
    return render(request,'vortice/card.html', contexto)



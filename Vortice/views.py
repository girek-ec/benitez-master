from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render

# Create your views here.

from benitez import settings
from Vortice.models import *

def index_vortice(request):
    contexto ={
        'vortice':Vortice.objects.all().first(),
        'notificaciones': Notificaciones.objects.all().first(),
        'sliders':Coleccion.objects.all(),
        'secciones': Seccion_Cliente.objects.all(),
        'colecciones':Coleccion.objects.all(),
        'imag_prenda_articulos':Imag_prenda_articulo.objects.all(),
        'tipo_articulos_menu': Tipo_articulo.objects.all(),
        'products': Prod_prenda.objects.all(),
        'colores' : Colores.objects.all(),
        'produc_color' : Produc_Color.objects.all(),
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
        'imag_prenda_articulos':Imag_prenda_articulo.objects.all(),
        'tipo_articulos_menu': Tipo_articulo.objects.all(),
        'tipo_articulos': Tipo_articulo.objects.filter(coleccion__cliente__cliente=secc),
        'products': Prod_prenda.objects.filter(tipo_produc__coleccion__cliente__cliente=secc),
        'colores' : Colores.objects.all(),
        'n_camisetas' : Nu_Talla_Cami.objects.all(),
        'n_zapatos' : Nu_Talla_Zapa.objects.all(),
        'n_productos' : Nu_Talla_Produ.objects.all(),
        't_camisetas' : Talla_Camiseta.objects.all(),
        't_zapatos' : Talla_Zapato.objects.all(),
        't_productos' : Talla_Producto.objects.all(),
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
        'imag_prenda_articulos':Imag_prenda_articulo.objects.all(),
        'tipo_articulos_menu': Tipo_articulo.objects.all(),
        'tipo_articulos': Tipo_articulo.objects.filter(coleccion__cliente__cliente=seccion),
        'products': Prod_prenda.objects.filter(tipo_produc__coleccion__cliente__cliente=seccion, tipo_produc__nombre_articulo=tipo),
        'colores' : Colores.objects.all(),
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
        'imag_prenda_articulos':Imag_prenda_articulo.objects.all(),
        'colecciones':Coleccion.objects.all(),
        'colecciones_id':Coleccion.objects.filter(cliente__cliente=seccion, tema_colec=coleccion ).first(),
        'tipo_articulos': Tipo_articulo.objects.filter(coleccion__cliente__cliente=seccion, coleccion__tema_colec=coleccion ),
        'products': Prod_prenda.objects.filter(tipo_produc__coleccion__tema_colec=coleccion ), 
        'colores' : Colores.objects.all(),
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
        'imag_prenda_articulos':Imag_prenda_articulo.objects.all(),
        'colecciones':Coleccion.objects.all(),
        'colecciones_id':Coleccion.objects.filter(cliente__cliente=seccion, tema_colec=coleccion ).first(),
        'tipo_articulos': Tipo_articulo.objects.filter(coleccion__cliente__cliente=seccion, coleccion__tema_colec=coleccion ),
        'products': Prod_prenda.objects.filter(tipo_produc__coleccion__tema_colec=coleccion, tipo_produc__nombre_articulo=tipo ), 
        'colores' : Colores.objects.all(),
        'servicios' : Servicios.objects.all(),
        'giftCards' : GiftCard.objects.all(),
        'anios' :  Anio.objects.all(),
        'meses' :  Meses.objects.all(),
        'mesmodas' : MesModa.objects.all(),
        'mesmoda_galerias' : MesModa_galeria.objects.all(),
        
        
    }
    return render(request, 'vortice/shop-collection-sub.html', contexto)


def producto_detalle(request,id):
    contexto = {
        'vortice':Vortice.objects.all().first(),
        'notificaciones': Notificaciones.objects.all().first(),
        'sliders':Coleccion.objects.all(),
        'secciones': Seccion_Cliente.objects.all(),
        'tipo_articulos_menu': Tipo_articulo.objects.all(),
        'colecciones':Coleccion.objects.all(),
        'imag_prenda_articulos':Imag_prenda_articulo.objects.all(),
        'tipo_articulos': Tipo_articulo.objects.filter(coleccion__cliente__cliente=id),
        'products': Prod_prenda.objects.get(id=id),
        'colores' : Colores.objects.all(),
        'produc_color' : Produc_Color.objects.filter(produc_prenda=id),
        'n_camisetas' : Nu_Talla_Cami.objects.all(),
        'n_zapatos' : Nu_Talla_Zapa.objects.all(),
        'n_productos' : Nu_Talla_Produ.objects.all(),
        't_camisetas' : Talla_Camiseta.objects.filter(produc=id),
        't_zapatos' : Talla_Zapato.objects.filter(produc=id),
        't_productos' : Talla_Producto.objects.filter(produc=id),
        'servicios' : Servicios.objects.all(),
        'giftCards' : GiftCard.objects.all(),
        'anios' :  Anio.objects.all(),
        'meses' :  Meses.objects.all(),
        'mesmodas' : MesModa.objects.all(),
        'mesmoda_galerias' : MesModa_galeria.objects.all(),
       
    }
    return render(request,'vortice/product-description-vertical.html', contexto)

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
        'imag_prenda_articulos':Imag_prenda_articulo.objects.all(),
        'tipo_articulos': Tipo_articulo.objects.all(),
        'notificaciones': Notificaciones.objects.all().first(),
        'vortice': Vortice.objects.all().first(),
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
        'imag_prenda_articulos':Imag_prenda_articulo.objects.all(),
        'tipo_articulos': Tipo_articulo.objects.all(),
        'notificaciones': Notificaciones.objects.all().first(),
        'vortice': Vortice.objects.all().first(),
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
        'imag_prenda_articulos':Imag_prenda_articulo.objects.all(),
        'tipo_articulos_menu': Tipo_articulo.objects.all(),
        'products': Prod_prenda.objects.all(),
        'colores' : Colores.objects.all(),
        'produc_color' : Produc_Color.objects.all(),
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
        'imag_prenda_articulos':Imag_prenda_articulo.objects.all(),
        'tipo_articulos_menu': Tipo_articulo.objects.all(),
        'products': Prod_prenda.objects.all(),
        'giftCards' : GiftCard.objects.all(),
        'slidercard' : SliderCard.objects.all(),
  
   
        
    }
    return render(request,'vortice/giftcard.html', contexto)


def card(request,id):
    contexto ={
        'vortice':Vortice.objects.all().first(),
        'notificaciones': Notificaciones.objects.all().first(),
        'secciones': Seccion_Cliente.objects.all(),
        'colecciones':Coleccion.objects.all(),
        'imag_prenda_articulos':Imag_prenda_articulo.objects.all(),
        'tipo_articulos_menu': Tipo_articulo.objects.all(),
        'products': Prod_prenda.objects.all(),
        'giftCards' : GiftCard.objects.get(id=id),
  
   
        
    }
    return render(request,'vortice/card.html', contexto)


def nosotros(request,):
    contexto ={
        'vortice':Vortice.objects.all().first(),
        'notificaciones': Notificaciones.objects.all().first(),
        'sliders':Coleccion.objects.all(),
        'secciones': Seccion_Cliente.objects.all(),
        'colecciones':Coleccion.objects.all(),
        'imag_prenda_articulos':Imag_prenda_articulo.objects.all(),
        'tipo_articulos_menu': Tipo_articulo.objects.all(),
        'products': Prod_prenda.objects.all(),
        'colores' : Colores.objects.all(),
        'produc_color' : Produc_Color.objects.all(),
        'servicios' : Servicios.objects.all(),
        'giftCards' : GiftCard.objects.all(),
        'anios' :  Anio.objects.all(),
        'meses' :  Meses.objects.all(),
        'mesmodas' : MesModa.objects.all(),
        'mesmoda_galerias' : MesModa_galeria.objects.all(),
    }
    return render(request,'vortice/about-us.html', contexto)

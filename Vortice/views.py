from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render

# Create your views here.


from Vortice.models import *


def index_vortice(request):
    contexto ={
        'vortice':Vortice.objects.all().first(),
        'promo': Vorti_Promo.objects.all(),
        'slider':Slider.objects.all(),
        'muestra': Muestra_productos.objects.all(),
        'coleccion':Coleccion.objects.all(),
        'prenda':Prenda.objects.all(),
        'seccion': Seccion_Cliente.objects.all(),
        'products': Product.objects.all().order_by('-create_at'),
        'redes': Contacto_redes.objects.all().first(),

    }
    return render(request, 'vortice/index_vortice.html', contexto)


def seccion_filtro_vortice(request,secc):

    contexto ={
        'prendas': Prenda.objects.filter(coleccion__seccion__seccion=secc),
        'articu': Articulo.objects.filter(seccion__seccion=secc),
        'vortice':Vortice.objects.all().first(),
        'seccion': Seccion_Cliente.objects.all(),
        'sec': Seccion_Cliente.objects.get(seccion=secc),
        'prenda': Prenda.objects.all(),
        'coleccion': Coleccion.objects.all(),
        'colecciones':Coleccion.objects.filter(seccion__seccion=secc),
        'productss': Product.objects.filter(prenda__coleccion__seccion__seccion=secc).order_by('-create_at'),
        'redes': Contacto_redes.objects.all().first(),
    }
    return render(request, 'vortice/categories.html', contexto)


def tipo_filtro_vortice(request,seccion,tipo):
    contexto ={
        'articu': Articulo.objects.filter(seccion__seccion=seccion),
        'prenda': Prenda.objects.all(),
        'seccion': Seccion_Cliente.objects.all(),
        'sec': Seccion_Cliente.objects.get(seccion=seccion),
        'vortice':Vortice.objects.all().first(),
        'prendas': Prenda.objects.filter(coleccion__seccion__seccion=seccion),
        'coleccion': Coleccion.objects.all(),
        'colecciones': Coleccion.objects.filter(seccion__seccion=seccion),
        'redes': Contacto_redes.objects.all().first(),
        'product': Product.objects.filter(articulo__seccion__seccion=seccion, articulo__tipo__tipo=tipo).order_by('-create_at'),
        'products': Product.objects.filter(prenda__coleccion__seccion__seccion=seccion, prenda__tipo__tipo=tipo).order_by('-create_at'),
    }
    return render(request, 'vortice/categories.html', contexto)

def coleccion_filtro_vortice(request,seccion,coleccion):
    contexto ={
        'articu': Articulo.objects.filter(seccion__seccion=seccion),
        'prenda': Prenda.objects.all(),
        'seccion': Seccion_Cliente.objects.all(),
        'sec': Seccion_Cliente.objects.get(seccion=seccion),
        'vortice':Vortice.objects.all().first(),
        'prendas': Prenda.objects.filter(coleccion__seccion__seccion=seccion, coleccion__tema=coleccion),
        'coleccion': Coleccion.objects.all(),
        'colecciones': Coleccion.objects.filter(seccion__seccion=seccion),
        'colec': Coleccion.objects.filter(seccion__seccion=seccion, tema=coleccion).first(),
        'redes': Contacto_redes.objects.all(),
        'prod': Product.objects.filter(prenda__coleccion__seccion__seccion=seccion,prenda__coleccion__tema=coleccion).order_by('-create_at'),
        'productss': Product.objects.filter(prenda__coleccion__tema=coleccion ).order_by('-create_at'),
    }
    return render(request, 'vortice/coleccion.html', contexto)

def coleccion_filtro_prenda_vortice(request,seccion,coleccion,tipo):
    contexto ={
        # 'articu': Articulo.objects.filter(seccion__seccion=seccion),
        'prenda': Prenda.objects.all(),
        'seccion': Seccion_Cliente.objects.all(),
        'secc': Seccion_Cliente.objects.filter(seccion=seccion),
        'vortice':Vortice.objects.all().first(),
        'prendaa': Prenda.objects.filter(coleccion__seccion__seccion=seccion, coleccion__tema=coleccion),
        'coleccion': Coleccion.objects.all(),
        'colecciones': Coleccion.objects.filter(seccion__seccion=seccion),
        'colec': Coleccion.objects.filter(seccion__seccion=seccion,tema=coleccion).first(),
        'redes': Contacto_redes.objects.all(),
        'product': Product.objects.filter(articulo__seccion__seccion=seccion, articulo__tipo__tipo=tipo).order_by('-create_at'),
        'products': Product.objects.filter(prenda__coleccion__seccion__seccion=seccion, prenda__coleccion__tema=coleccion, prenda__tipo__tipo=tipo).order_by('-create_at'),
    }
    return render(request, 'vortice/coleccion.html', contexto)


def producto_detalle_vortice(request,id):
    contexto = {
        'vortice': Vortice.objects.all().first(),
        'coleccion': Coleccion.objects.all(),
        'prenda': Prenda.objects.all(),
        'seccion': Seccion_Cliente.objects.all(),
        'camiseta_cuello': Camiseta_cuello.objects.all(),
        'camiseta_talla_hombre': Camiseta_talla_Hombre.objects.all(),
        'camiseta_talla_mujer': Camiseta_talla_Mujer.objects.all(),
        'camiseta_talla_nene': Camiseta_talla_Nene.objects.all(),
        'camiseta_talla_nena': Camiseta_talla_Nena.objects.all(),
        'products': Product.objects.get(id=id),
        'produc': Product.objects.all().order_by('-create_at'),
        'camiseta_imagen_deta':Camiseta_Imagen_detalle.objects.all().first(),
        'redes': Contacto_redes.objects.all(),
    }
    return render(request, 'vortice/product-details.html', contexto)




def contacto_vortice(request):
    contexto = {
        'vortice': Vortice.objects.all().first(),
        'coleccion': Coleccion.objects.all(),
        'prenda': Prenda.objects.all(),
        'seccion': Seccion_Cliente.objects.all(),
        'products': Product.objects.all(),
        'redes': Contacto_redes.objects.all().first(),
    }
    if request.POST:
        enviar_email(request,request.POST['subject'],request.POST['email'],"vortice.ec@gmail.com",request.POST['message'],request.POST['name'])
    return render(request, 'vortice/contact.html', contexto)



def enviar_email(request,asunto,from_email,to,mensaje,nombre):
    asunto = asunto
    from_email = from_email
    to = to
    text_content = 'Este mnsaje es importante.'
    html_content = '<p>This is an <strong>important</strong> message.</p>' \
                   '<img src="http://vortice.ec/static/imagenes/vortice.png"><br>' + mensaje
    msg = EmailMultiAlternatives(asunto, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    # print from_email

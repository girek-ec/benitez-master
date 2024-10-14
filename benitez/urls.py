"""benitez URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Home.views import *
from Girekstudio.views import *
from Vortice.views import *
from Zatuar.views import *
from Niska.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('empresa/', empresa),
    path('trabajo/', trabaja),
    path('contacto/', contacto),

    # web girekstudio/
    path('girekstudio/', index_girekstudio),
    path('girekstudio/estudio/', estudio_girekstudio),
    path('girekstudio/servicios/', servicios_girekstudio),
    path('girekstudio/servicios/<int:n>/', serviciosdescripcion_girekstudio),
    path('girekstudio/portafolio/', portafolio_girekstudio),
    path('girekstudio/portafolio/<int:n>/', portafolioimagen_girekstudio),
    path('girekstudio/tienda/', tienda_girekstudio),
    path('girekstudio/tienda/<int:id>/', producto_cate_girekstudio),
    path('girekstudio/producto/<int:n>/', producto_id_girekstudio),
    path('girekstudio/contacto/', contacto_girekstudio),
    # path('girekstudio/error/', error404),
    # web girekstudio/

    # web zatuar/
    path('zatuar/', index_zatuar),
    path('zatuar/empresa/', empresa_zatuar),
    path('zatuar/linea/', linea),
    path('zatuar/linea/<slug:lineaa>/', linea_cate),
    path('zatuar/productos/', producto_zatuar),
    path('zatuar/productos/<int:id>/', producto_cate_zatuar),
    path('zatuar/producto/<int:id>/', producto_id_zatuar),
    path('zatuar/clientes/', clientes_zatuar),
    path('zatuar/clientes/<int:id>/', clientes_id_zatuar ),
    path('zatuar/contacto/', contacto_zatuar),
    path('zatuar/error/', error404_zatuar),
    # web zatuar/

    # web vortice/
    path('vortice/', index_vortice),
    path('vortice/seccion/<slug:secc>/', seccion_filtro),
    path('vortice/seccion/<slug:seccion>/prenda/<slug:tipo>/', tipo_filtro),
    path('vortice/seccion/<slug:seccion>/coleccion/<slug:coleccion>/', coleccion_filtro),
    path('vortice/seccion/<slug:seccion>/coleccion/<slug:coleccion>/prenda/<slug:tipo>/',coleccion_filtro_prenda),
    path('vortice/producto/<int:id>/', producto_detalle),
    path('vortice/blog/', blog),
    path('vortice/gift/', giftcard),
    path('vortice/gift/<int:id>', card),
    path('vortice/post/<int:id>/', post),
    path('vortice/nosotros/', nosotros),
    # web vortice/

    # web niska/
    path('niska/', index_niska),
    path('niska/empresa/', nosotros_niska ),
    path('niska/productos/', productos_niska),
    # path('niska/productos/<int:id>/', producto_cate_niska),
    path('niska/producto/<int:n>/', producto_id_niska),
    path('niska/contacto/', contacto_niska),
    # web niska/



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin

# Register your models here.
from Girekstudio.models import *
from Home.models import *
from benitez.snippers import Attr


class ImagenesproyectoInline(admin.StackedInline):
    model = Imagenesproyecto
    extra = 0

@admin.register(Editables)
class EditablesAdmin(admin.ModelAdmin):
    list_display = Attr(Editables) + ["vista_previa"]
    list_display_links = Attr(Editables)

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = Attr(Marca) + ["vista_previa"]
    list_display_links = Attr(Marca)

@admin.register(Contacto_empresa)
class Contacto_empresaAdmin(admin.ModelAdmin):
    list_display = Attr(Contacto_empresa)
    list_display_links = Attr(Contacto_empresa)


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = Attr(Servicio) + ["vista_previa"]
    list_display_links = Attr(Servicio)


@admin.register(Imag_Video_Servicio)
class Imag_Video_ServicioAdmin(admin.ModelAdmin):
    list_display = Attr(Imag_Video_Servicio) + ["vista_previa"]
    list_display_links = Attr(Imag_Video_Servicio)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = Attr(Cliente) + ["vista_previa"]
    list_display_links = Attr(Cliente)

@admin.register(Portafolio)
class PortafolioAdmin(admin.ModelAdmin):
    list_display = Attr(Portafolio)
    list_display_links = Attr(Portafolio)


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = Attr(Proyecto) + ["vista_previa"]
    list_display_links = Attr(Proyecto)
    inlines = [ImagenesproyectoInline]


@admin.register(Imagenesproyecto)
class ImagenesproyectoAdmin(admin.ModelAdmin):
    list_display = Attr(Imagenesproyecto) + ["vista_previa"]
    list_display_links = Attr(Imagenesproyecto)



@admin.register(Frase)
class Frasedmin(admin.ModelAdmin):
    list_display = Attr(Frase)
    list_display_links = Attr(Frase)


@admin.register(Planes)
class PlanesAdmin(admin.ModelAdmin):
    list_display = Attr(Planes)
    list_display_links = Attr(Planes)


@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display = Attr(Ciudad)
    list_display_links = Attr(Ciudad)


@admin.register(Clasif_producto)
class Clasif_productoAdmin(admin.ModelAdmin):
    list_display = Attr(Clasif_producto)
    list_display_links = Attr(Clasif_producto)


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = Attr(Proveedor)
    list_display_links = Attr(Proveedor)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = Attr(Producto) + ["vista_previa"]
    list_display_links = Attr(Producto)

@admin.register(Producto_Imagen)
class Producto_ImagenAdmin(admin.ModelAdmin):
    list_display = Attr(Producto_Imagen) + ["vista_previa"]
    list_display_links = Attr(Producto_Imagen)

@admin.register(Suscripcion_Email)
class modelo(admin.ModelAdmin):
    list_display = Attr(Suscripcion_Email)
    list_display_links = Attr(Suscripcion_Email)


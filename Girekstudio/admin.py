from django.contrib import admin

# Register your models here.
from Girekstudio.models import *
from Home.models import *
from benitez.snippers import Attr


class ImagenesproyectoInline(admin.StackedInline):
    model = Imagenesproyecto
    extra = 0

class Lista_servicioInline(admin.StackedInline):
    model = Lista_servicio
    extra = 0

class Imag_Video_ServicioInline(admin.StackedInline):
    model = Imag_Video_Servicio
    extra = 0

class PlanesInline(admin.StackedInline):
    model = Planes
    extra = 0

class Plan_listInline(admin.StackedInline):
    model = Plan_list
    extra = 0


class Producto_ImagenInline(admin.StackedInline):
    model = Producto_Imagen
    extra = 0

@admin.register(Editables)
class EditablesAdmin(admin.ModelAdmin):
    list_display = Attr(Editables)
    list_display_links = Attr(Editables)

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = Attr(Marca)
    list_display_links = Attr(Marca)

@admin.register(Contacto_empresa)
class Contacto_empresaAdmin(admin.ModelAdmin):
    list_display = Attr(Contacto_empresa)
    list_display_links = Attr(Contacto_empresa)

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = Attr(Equipo)
    list_display_links = Attr(Equipo)

@admin.register(Sucursales)
class SucursalesAdmin(admin.ModelAdmin):
    list_display = Attr(Sucursales)
    list_display_links = Attr(Sucursales)


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = Attr(Servicio) + ["vista_previa"]
    list_display_links = Attr(Servicio)
    inlines = [Lista_servicioInline,Imag_Video_ServicioInline,PlanesInline]

@admin.register(Lista_servicio)
class Lista_servicioAdmin(admin.ModelAdmin):
    list_display = Attr(Lista_servicio)
    list_display_links = Attr(Lista_servicio)


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
    inlines = [Plan_listInline]

@admin.register(Plan_list)
class Plan_listAdmin(admin.ModelAdmin):
    list_display = Attr(Plan_list)
    list_display_links = Attr(Plan_list)

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
    inlines = [Producto_ImagenInline]

@admin.register(Producto_Imagen)
class Producto_ImagenAdmin(admin.ModelAdmin):
    list_display = Attr(Producto_Imagen) + ["vista_previa"]
    list_display_links = Attr(Producto_Imagen)

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = Attr(Slider)
    list_display_links = Attr(Slider)
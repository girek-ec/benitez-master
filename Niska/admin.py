from django.contrib import admin

# Register your models here.
from Niska.models import *
from Home.models import *
from benitez.snippers import Attr

@admin.register(Editable)
class EditableAdmin(admin.ModelAdmin):
    list_display = Attr(Editable)
    list_display_links = Attr(Editable)

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = Attr(Marca)
    list_display_links = Attr(Marca)

@admin.register(Clasif_producto)
class Clasif_productoAdmin(admin.ModelAdmin):
    list_display = Attr(Clasif_producto)
    list_display_links = Attr(Clasif_producto)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = Attr(Producto) + ["vista_previa"]
    list_display_links = Attr(Producto)

@admin.register(Producto_Imagen)
class Producto_ImagenAdmin(admin.ModelAdmin):
    list_display = Attr(Producto_Imagen) + ["vista_previa"]
    list_display_links = Attr(Producto_Imagen)
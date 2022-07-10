from django.contrib import admin

# Register your models here.
from Vortice.models import *
from Vortice.snippers import Attr

class Seccion_ClienteAdmin(admin.ModelAdmin):
    list_display = Attr(Seccion_Cliente)+["miniatura"]
    list_display_links = Attr(Seccion_Cliente)
admin.site.register(Seccion_Cliente, Seccion_ClienteAdmin)

class ColeccionAdmin(admin.ModelAdmin):
    list_display = Attr(Coleccion)+["miniatura"]
    list_display_links = Attr(Coleccion)
admin.site.register(Coleccion, ColeccionAdmin)



class ArticuloAdmin(admin.ModelAdmin):
    list_display = Attr(Articulo)+["miniatura"]
    list_display_links = Attr(Articulo)
admin.site.register(Articulo, ArticuloAdmin)

class Imag_prenda_articuloAdmin(admin.ModelAdmin):
    list_display = Attr(Imag_prenda_articulo)+["miniatura"]
    list_display_links = Attr(Imag_prenda_articulo)
admin.site.register(Imag_prenda_articulo, Imag_prenda_articuloAdmin)

class PrendaAdmin(admin.ModelAdmin):
    list_display = Attr(Prenda)+["miniatura"]
    list_display_links = Attr(Prenda)
admin.site.register(Prenda, PrendaAdmin)


class SliderAdmin(admin.ModelAdmin):
    list_display = Attr(Slider)+["miniatura"]
    list_display_links = Attr(Slider)
admin.site.register(Slider, SliderAdmin)

class VorticeAdmin(admin.ModelAdmin):
    list_display = Attr(Vortice)+["miniatura"]
    list_display_links = Attr(Vortice)
admin.site.register(Vortice, VorticeAdmin)

class Vorti_PromoAdmin(admin.ModelAdmin):
    list_display = Attr(Vorti_Promo)+["miniatura"]
    list_display_links = Attr(Vorti_Promo)
admin.site.register(Vorti_Promo, Vorti_PromoAdmin)

class Muestra_productosAdmin(admin.ModelAdmin):
    list_display = Attr(Muestra_productos)+["miniatura"]
    list_display_links = Attr(Muestra_productos)
admin.site.register(Muestra_productos, Muestra_productosAdmin)

class Contacto_redesAdmin(admin.ModelAdmin):
    list_display = Attr(Contacto_redes)
    list_display_links = Attr(Contacto_redes)
admin.site.register(Contacto_redes, Contacto_redesAdmin)



@admin.register(Camiseta_talla_Hombre)
class Camiseta_talla_HombreAdmin(admin.ModelAdmin):
    list_display = Attr(Camiseta_talla_Hombre)
    list_display_links = Attr(Camiseta_talla_Hombre)

@admin.register(Camiseta_talla_Mujer)
class Camiseta_talla_MujerAdmin(admin.ModelAdmin):
    list_display = Attr(Camiseta_talla_Mujer)
    list_display_links = Attr(Camiseta_talla_Mujer)

@admin.register(Camiseta_talla_Nene)
class Camiseta_talla_NeneAdmin(admin.ModelAdmin):
    list_display = Attr(Camiseta_talla_Nene)
    list_display_links = Attr(Camiseta_talla_Nene)

@admin.register(Camiseta_talla_Nena)
class Camiseta_talla_NenaAdmin(admin.ModelAdmin):
    list_display = Attr(Camiseta_talla_Nena)
    list_display_links = Attr(Camiseta_talla_Nena)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["miniatura"]+ Attr(Product)
    list_display_links = Attr(Product)

@admin.register(Camiseta_Imagen_detalle)
class Camiseta_Imagen_detalleAdmin(admin.ModelAdmin):
    list_display = Attr(Camiseta_Imagen_detalle)
    list_display_links = Attr(Camiseta_Imagen_detalle)






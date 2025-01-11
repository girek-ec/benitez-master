from django.contrib import admin

# Register your models here.
from Vortice.models import *
from Vortice.snippers import Attr


class Produc_ColorInline(admin.StackedInline):
    model = Produc_Color
    extra = 0

class Tallas_CamisetaInline(admin.StackedInline):
    model = Talla_Camiseta
    extra = 0

class Talla_ZapatoInline(admin.StackedInline):
    model = Talla_Zapato
    extra = 0

class Talla_ProductoInline(admin.StackedInline):
    model = Talla_Producto
    extra = 0


class MesModa_galeriaInline(admin.StackedInline):
    model = MesModa_galeria
    extra = 0

class VorticeAdmin(admin.ModelAdmin):
    list_display = Attr(Vortice)+["miniatura"]
    list_display_links = Attr(Vortice)
admin.site.register(Vortice, VorticeAdmin)

class NotificacionesAdmin(admin.ModelAdmin):
    list_display = Attr(Notificaciones)
    list_display_links = Attr(Notificaciones)
admin.site.register(Notificaciones, NotificacionesAdmin)

class SliderCardAdmin(admin.ModelAdmin):
    list_display = Attr(SliderCard)+["miniatura"]
    list_display_links = Attr(SliderCard)
admin.site.register(SliderCard, SliderCardAdmin)


class Seccion_ClienteAdmin(admin.ModelAdmin):
    list_display = Attr(Seccion_Cliente)
    list_display_links = Attr(Seccion_Cliente)
admin.site.register(Seccion_Cliente, Seccion_ClienteAdmin)

class ColeccionAdmin(admin.ModelAdmin):
    list_display = Attr(Coleccion)+["miniatura"]
    list_display_links = Attr(Coleccion)
admin.site.register(Coleccion, ColeccionAdmin)

class Imag_prenda_articuloAdmin(admin.ModelAdmin):
    list_display = Attr(Imag_prenda_articulo)
    list_display_links = Attr(Imag_prenda_articulo)
admin.site.register(Imag_prenda_articulo, Imag_prenda_articuloAdmin)

class Tipo_articuloAdmin(admin.ModelAdmin):
    list_display = Attr(Tipo_articulo)+["miniatura"]
    list_display_links = Attr(Tipo_articulo)
admin.site.register(Tipo_articulo, Tipo_articuloAdmin)

class Material_productoAdmin(admin.ModelAdmin):
    list_display = Attr(Material_producto)
    list_display_links = Attr(Material_producto)
admin.site.register(Material_producto, Material_productoAdmin)


class ColoresAdmin(admin.ModelAdmin):
    list_display = Attr(Colores)
    list_display_links = Attr(Colores)
admin.site.register(Colores, ColoresAdmin)

class Produc_ColorAdmin(admin.ModelAdmin):
    list_display = Attr(Produc_Color)
    list_display_links = Attr(Produc_Color)
admin.site.register(Produc_Color, Produc_ColorAdmin)

class Nu_Talla_CamiAdmin(admin.ModelAdmin):
    list_display = Attr(Nu_Talla_Cami)
    list_display_links = Attr(Nu_Talla_Cami)
admin.site.register(Nu_Talla_Cami, Nu_Talla_CamiAdmin)

class Nu_Talla_ZapaAdmin(admin.ModelAdmin):
    list_display = Attr(Nu_Talla_Zapa)
    list_display_links = Attr(Nu_Talla_Zapa)
admin.site.register(Nu_Talla_Zapa, Nu_Talla_ZapaAdmin)

class Nu_Talla_ProduAdmin(admin.ModelAdmin):
    list_display = Attr(Nu_Talla_Produ)
    list_display_links = Attr(Nu_Talla_Produ)
admin.site.register(Nu_Talla_Produ, Nu_Talla_ProduAdmin)

class Talla_CamisetaAdmin(admin.ModelAdmin):
    list_display = Attr(Talla_Camiseta)
    list_display_links = Attr(Talla_Camiseta)
admin.site.register(Talla_Camiseta, Talla_CamisetaAdmin)

class Talla_ZapatoAdmin(admin.ModelAdmin):
    list_display = Attr(Talla_Zapato)
    list_display_links = Attr(Talla_Zapato)
admin.site.register(Talla_Zapato, Talla_ZapatoAdmin)

class Talla_ProductoAdmin(admin.ModelAdmin):
    list_display = Attr(Talla_Producto)
    list_display_links = Attr(Talla_Producto)
admin.site.register(Talla_Producto, Talla_ProductoAdmin)

class Prod_prendaAdmin(admin.ModelAdmin):
    list_display = Attr(Prod_prenda)+["miniatura"]
    list_display_links = Attr(Prod_prenda)
    inlines = [Produc_ColorInline, Tallas_CamisetaInline, Talla_ZapatoInline, Talla_ProductoInline ]
admin.site.register(Prod_prenda, Prod_prendaAdmin)

class ServiciosAdmin(admin.ModelAdmin):
    list_display = Attr(Servicios)
    list_display_links = Attr(Servicios)
admin.site.register(Servicios, ServiciosAdmin)

class GiftCardAdmin(admin.ModelAdmin):
    list_display = Attr(GiftCard)+["miniatura"]
    list_display_links = Attr(GiftCard)
admin.site.register(GiftCard, GiftCardAdmin)

class Anioadmin(admin.ModelAdmin):
    list_display = Attr(Anio)
    list_display_links = Attr(Anio)
admin.site.register(Anio, Anioadmin)

class MesesAdmin(admin.ModelAdmin):
    list_display = Attr(Meses)
    list_display_links = Attr(Meses)
admin.site.register(Meses, MesesAdmin)

class MesModaAdmin(admin.ModelAdmin):
    list_display = Attr(MesModa)+["miniatura"]
    list_display_links = Attr(MesModa)
    inlines = [MesModa_galeriaInline]
admin.site.register(MesModa, MesModaAdmin)

class MesModa_galeriaAdmin(admin.ModelAdmin):
    list_display = Attr(MesModa_galeria)+["miniatura"]
    list_display_links = Attr(MesModa_galeria)
admin.site.register(MesModa_galeria, MesModa_galeriaAdmin)

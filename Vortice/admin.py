from django.contrib import admin

# Register your models here.
from Vortice.models import *
from Vortice.snippers import Attr


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

class Prod_prendaAdmin(admin.ModelAdmin):
    list_display = Attr(Prod_prenda)+["miniatura"]
    list_display_links = Attr(Prod_prenda)
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

from django.contrib import admin

# Register your models here.
from Home.models import *
from Zatuar.models import *
from Zatuar.snippers import Attr


class SliderAdmin(admin.ModelAdmin):
    list_display = Attr(Slider)
    list_display_links = Attr(Slider)
admin.site.register(Slider,SliderAdmin)

class Zatuar_marcaAdmin(admin.ModelAdmin):
    list_display = Attr(Zatuar_marca)
    list_display_links = Attr(Zatuar_marca)
admin.site.register(Zatuar_marca, Zatuar_marcaAdmin)

class Contacto_empresaAdmin(admin.ModelAdmin):
    list_display = Attr(Contacto_empresa)
    list_display_links = Attr(Contacto_empresa)
admin.site.register(Contacto_empresa,Contacto_empresaAdmin)

class Redes_SocialesAdmin(admin.ModelAdmin):
    list_display = Attr(Redes_sociales)
    list_display_links = Attr(Redes_sociales)
admin.site.register(Redes_sociales,Redes_SocialesAdmin)

class BeneficiosAdmin(admin.ModelAdmin):
    list_display = Attr(Beneficios)
    list_display_links = Attr(Beneficios)
admin.site.register(Beneficios,BeneficiosAdmin)

class IdentidadAdmin(admin.ModelAdmin):
    list_display = Attr( Identidad)
    list_display_links = Attr( Identidad)
admin.site.register(Identidad,IdentidadAdmin)

class Personalizacion_ProductoAdmin(admin.ModelAdmin):
    list_display = Attr(Personalizaion_Poducto)
    list_display_links = Attr(Personalizaion_Poducto)
admin.site.register(Personalizaion_Poducto,Personalizacion_ProductoAdmin)

class ProcesoAdmin(admin.ModelAdmin):
    list_display = Attr(Proceso)
    list_display_links = Attr(Proceso)
admin.site.register(Proceso,ProcesoAdmin)

class Galeria_ProcesoAdmin(admin.ModelAdmin):
    list_display = Attr(Galeria_Proceso)
    list_display_links = Attr(Galeria_Proceso)
    list_filter = ['imagen', 'titulo']
admin.site.register(Galeria_Proceso,Galeria_ProcesoAdmin)

class DescargaAdmin(admin.ModelAdmin):
    list_display = Attr(Descarga)
    list_display_links = Attr(Descarga)
admin.site.register(Descarga,DescargaAdmin)

class DetallesAdmin(admin.ModelAdmin):
    list_display = Attr(Detalles)
    list_display_links = Attr(Detalles)
admin.site.register(Detalles,DetallesAdmin)

class ProductAdminn(admin.ModelAdmin):
    list_display = Attr(Product)+["miniatura"]
    list_display_links = Attr(Product)
admin.site.register(Product,ProductAdminn)

class Linea_ProductAdminn(admin.ModelAdmin):
    list_display = Attr(Linea_Product)+["miniatura"]
    list_display_links = Attr(Linea_Product)
admin.site.register(Linea_Product, Linea_ProductAdminn)


class Clasif_productoAdmin(admin.ModelAdmin):
    list_display = Attr(Clasif_producto)
    list_display_links = Attr(Clasif_producto)
admin.site.register(Clasif_producto,Clasif_productoAdmin)

class Producto_ImagenAdmin(admin.ModelAdmin):
    list_display = Attr(Producto_Imagen)+["miniatura"]
    list_display_links = Attr(Producto_Imagen)
admin.site.register(Producto_Imagen,Producto_ImagenAdmin)

class Producto_PersonalizacionAdmin(admin.ModelAdmin):
    list_display = Attr(Producto_Personalizacion)
    list_display_links = Attr(Producto_Personalizacion)
admin.site.register(Producto_Personalizacion,Producto_PersonalizacionAdmin)

class Producto_clienteAdmin(admin.ModelAdmin):
    list_display = Attr(Producto_cliente)
    list_display_links = Attr(Producto_cliente)
admin.site.register(Producto_cliente, Producto_clienteAdmin)


class GaleriaInline(admin.StackedInline):
    model = Galeria_Cliente
    extra = 2

class ClienteAdmin(admin.ModelAdmin):
    list_display = Attr(Cliente)
    list_display_links = Attr(Cliente)
    inlines =[GaleriaInline]
admin.site.register(Cliente,ClienteAdmin)

class Galeria_ClienteAdmin(admin.ModelAdmin):
    list_display = Attr(Galeria_Cliente)
    list_display_links = Attr(Galeria_Cliente)
admin.site.register(Galeria_Cliente,Galeria_ClienteAdmin)
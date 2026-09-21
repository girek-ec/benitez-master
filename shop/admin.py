from django.contrib import admin
from django.utils.html import format_html

from .models import Product, Category, Marca,BlogColexin,  CategoriaBlogColexin, ImagenBlogColexin
from .snippers import Attr


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = Attr(Marca)
    list_display_links = Attr(Marca)

# Registro de la clase Category en el admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]  # Muestra solo 'name' en la lista


# Registro de la clase Product en el admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Primero mostramos la miniatura, luego los otros campos
    list_display = ['miniatura', 'name', 'category', 'price', 'available', 'created', 'updated']

    # Filtros para el admin
    list_filter = ['category']

    # Campos que pueden ser editados directamente desde la lista
    list_editable = ['name','category','price', 'available']

    # No permitir que los campos editables sean enlaces
    list_display_links = ['miniatura']  # Establece 'miniatura' y 'name' como enlaces para la edición

    # Función para mostrar la miniatura de la imagen en el admin
    @admin.display(description="Imagen")
    def miniatura(self, obj):
        if obj.image_1 and hasattr(obj.image_1, 'url'):
            return format_html('<img src="{}" width="50" height="50" style="border-radius:5px;"/>', obj.image_1.url)
        return "Sin imagen"


class ImagenBlogColexinInline(admin.TabularInline):
    model = ImagenBlogColexin
    extra = 1
    fields = (
        "imagen",
        "titulo",
        "orden",
    )


@admin.register(CategoriaBlogColexin)
class CategoriaBlogColexinAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "slug",
        "activo",
    )

    list_filter = ("activo",)
    search_fields = ("nombre",)
    prepopulated_fields = {
        "slug": ("nombre",),
    }


@admin.register(BlogColexin)
class BlogColexinAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "categoria",
        "fecha_publicacion",
        "activo",
        "destacado",
        "vista_previa",
    )

    list_filter = (
        "activo",
        "destacado",
        "categoria",
        "fecha_publicacion",
    )

    search_fields = (
        "titulo",
        "subtitulo",
        "contenido",
    )

    date_hierarchy = "fecha_publicacion"

    prepopulated_fields = {
        "slug": ("titulo",),
    }

    list_editable = (
        "activo",
        "destacado",
    )

    inlines = [ImagenBlogColexinInline]


@admin.register(ImagenBlogColexin)
class ImagenBlogColexinAdmin(admin.ModelAdmin):
    list_display = (
        "blog",
        "titulo",
        "orden",
        "vista_previa",
    )

    list_filter = ("blog",)

    search_fields = (
        "blog__titulo",
        "titulo",
    )
from django.contrib import admin
from django.utils.html import format_html

from .models import Product, Category, Marca
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

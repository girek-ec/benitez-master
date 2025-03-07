from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.formats.base_formats import XLSX
from django.utils.html import format_html

from Vortice.models import *
from Vortice.snippers import Attr

# Clase base personalizada para ModelAdmin
class BaseAdmin(admin.ModelAdmin):
    def __init__(self, model, *args, **kwargs):
        self.list_display = Attr(model)
        self.list_display_links = [Attr(model)[0]]  # Usar solo el primer campo como enlace
        super().__init__(model, *args, **kwargs)

# Inline para MesModa_galeria
class MesModa_galeriaInline(admin.StackedInline):
    model = MesModa_galeria
    extra = 0

# Admin para Vortice
@admin.register(Vortice)
class VorticeAdmin(BaseAdmin):
    list_display = list(BaseAdmin.list_display) + ["miniatura"]

# Admin para Notificaciones
@admin.register(Notificaciones)
class NotificacionesAdmin(BaseAdmin):
    pass

# Admin para Seccion_Cliente
@admin.register(Seccion_Cliente)
class Seccion_ClienteAdmin(BaseAdmin):
    pass

# Admin para Coleccion
@admin.register(Coleccion)
class ColeccionAdmin(BaseAdmin):
    list_display = list(BaseAdmin.list_display) + ["miniatura"]


# Admin para Tipo_articulo
@admin.register(Tipo_articulo)
class Tipo_articuloAdmin(BaseAdmin):
    list_display = list(BaseAdmin.list_display) + ["miniatura"]

# Admin para Material_producto
@admin.register(Material_producto)
class Material_productoAdmin(BaseAdmin):
    pass


class ProdPrendaResource(resources.ModelResource):
    # Campos personalizados para las relaciones
    tipo_produc = fields.Field(column_name='Tipo de Producto')
    coleccion = fields.Field(column_name='Colección')
    seccion = fields.Field(column_name='Sección')
    tipo_material = fields.Field(attribute='tipo_material', column_name='Material')

    class Meta:
        model = Prod_prenda
        fields = (
            'id',
            'tipo_produc',
            'coleccion',
            'seccion',
            'nombre_produc',
            'descripcion_produc',
            'tipo_material',
            'price',
            'has_sizes',
            'imagen_produc_01',
            'imagen_produc_02',
            'video_produc',
        )
        export_order = fields

    # EXPORTACIÓN
    def dehydrate_tipo_produc(self, obj):
        if obj.tipo_produc:
            return obj.tipo_produc.nombre_articulo
        return ""

    def dehydrate_coleccion(self, obj):
        if obj.tipo_produc and obj.tipo_produc.coleccion:
            return obj.tipo_produc.coleccion.tema_colec
        return ""

    def dehydrate_seccion(self, obj):
        if obj.tipo_produc and obj.tipo_produc.coleccion and obj.tipo_produc.coleccion.cliente:
            return obj.tipo_produc.coleccion.cliente.cliente
        return ""

    def dehydrate_tipo_material(self, obj):
        return obj.tipo_material.material if obj.tipo_material else ""

    # IMPORTACIÓN
    def before_import_row(self, row, **kwargs):
        # Manejar el campo Tipo de Producto
        tipo_producto = row.get('Tipo de Producto')
        if tipo_producto:
            # Usar filter().first() para evitar el error "get() returned more than one"
            tipo_producto_obj = Tipo_articulo.objects.filter(nombre_articulo=tipo_producto).first()
            if tipo_producto_obj:
                row['tipo_produc'] = tipo_producto_obj.id
            else:
                # Si no existe, crear un nuevo objeto
                tipo_producto_obj = Tipo_articulo.objects.create(nombre_articulo=tipo_producto)
                row['tipo_produc'] = tipo_producto_obj.id
        else:
            row['tipo_produc'] = None

        # Manejar el campo Colección
        coleccion = row.get('Colección')
        if coleccion:
            # Usar filter().first() para evitar el error "get() returned more than one"
            coleccion_obj = Coleccion.objects.filter(tema_colec=coleccion).first()
            if coleccion_obj:
                row['coleccion'] = coleccion_obj.id
            else:
                # Si no existe, crear un nuevo objeto
                coleccion_obj = Coleccion.objects.create(tema_colec=coleccion)
                row['coleccion'] = coleccion_obj.id
        else:
            row['coleccion'] = None

        # Manejar el campo Sección
        seccion = row.get('Sección')
        if seccion:
            # Usar filter().first() para evitar el error "get() returned more than one"
            seccion_obj = Seccion_Cliente.objects.filter(cliente=seccion).first()
            if seccion_obj:
                row['seccion'] = seccion_obj.id
            else:
                # Si no existe, crear un nuevo objeto
                seccion_obj = Seccion_Cliente.objects.create(cliente=seccion)
                row['seccion'] = seccion_obj.id
        else:
            row['seccion'] = None

        # 📌 Obtener el material, asegurando que sea una cadena vacía si es None
        material = row.get('Material', '')  # ✅ Si es None, se convierte en una cadena vacía
        material = material.strip() if material else None  # ✅ Evita error con None

        if material:
            # ✅ Buscar si el material existe en la base de datos o crearlo si no existe
            material_obj, created = Material_producto.objects.get_or_create(material=material)

            # 🔥 Aquí está el cambio importante: Asignar la **instancia** y no el string
            row['tipo_material'] = material_obj.id  # ✅ PASAR EL ID, NO EL STRING
        else:
            row['tipo_material'] = None  # ✅ Permitir que sea nulo si no hay material


    def get_export_format(self):

        return XLSX()



# Modifica la clase Prod_prendaAdmin para usar ImportExportModelAdmin
@admin.register(Prod_prenda)
class Prod_prendaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ProdPrendaResource
    list_display = ['id', 'miniatura', 'tipo_produc', 'nombre_produc', 'descripcion_produc', 'tipo_material', 'price', 'has_sizes']
    list_filter = ['tipo_produc', 'tipo_material']
    search_fields = ['nombre_produc', 'tipo_produc__nombre_articulo', 'tipo_material__material']
    list_editable = ['tipo_produc', 'nombre_produc', 'tipo_material', 'price', 'has_sizes']
    list_display_links = ['miniatura', 'id']

    @admin.display(description="Imagen")
    def miniatura(self, obj):
        if obj.imagen_produc_01:
            return format_html('<img src="{}" width="50" height="50"/>', obj.imagen_produc_01.url)
        return "Sin imagen"


    @admin.display(description="Descripción")
    def descripcion_produc(self, obj):
        return f"{obj.descripcion_produc[:10]}..." if obj.descripcion_produc else "Sin descripción"


# Admin para Servicios
@admin.register(Servicios)
class ServiciosAdmin(BaseAdmin):
    pass

# Admin para GiftCard
@admin.register(GiftCard)
class GiftCardAdmin(BaseAdmin):
    list_display = list(BaseAdmin.list_display) + ["miniatura"]

# Admin para Anio
@admin.register(Anio)
class Anioadmin(BaseAdmin):
    pass

# Admin para Meses
@admin.register(Meses)
class MesesAdmin(BaseAdmin):
    pass

# Admin para MesModa
@admin.register(MesModa)
class MesModaAdmin(BaseAdmin):
    list_display = list(BaseAdmin.list_display) + ["miniatura"]
    inlines = [MesModa_galeriaInline]

# Admin para MesModa_galeria
@admin.register(MesModa_galeria)
class MesModa_galeriaAdmin(BaseAdmin):
    list_display = list(BaseAdmin.list_display) + ["miniatura"]
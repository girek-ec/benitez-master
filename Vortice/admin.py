from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.formats.base_formats import XLSX
from django.utils.html import format_html

from Vortice.models import *
from Vortice.snippers import Attr


class OrdenForeignKeyMixin:
    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        if db_field.name == "cliente":
            kwargs["queryset"] = Seccion_Cliente.objects.order_by("cliente")

        elif db_field.name == "coleccion":
            kwargs["queryset"] = Coleccion.objects.select_related(
                "cliente"
            ).order_by(
                "cliente__cliente",
                "tema_colec"
            )

        elif db_field.name in ["tipo_articulo", "tipo_produc"]:
            kwargs["queryset"] = Tipo_articulo.objects.select_related(
                "coleccion",
                "coleccion__cliente"
            ).order_by(
                "coleccion__cliente__cliente",
                "coleccion__tema_colec",
                "nombre_articulo"
            )

        elif db_field.name == "detalle_prenda":
            kwargs["queryset"] = DetallePrendaColeccion.objects.select_related(
                "tipo_articulo",
                "tipo_articulo__coleccion",
                "tipo_articulo__coleccion__cliente"
            ).order_by(
                "tipo_articulo__coleccion__cliente__cliente",
                "tipo_articulo__coleccion__tema_colec",
                "tipo_articulo__nombre_articulo"
            )

        elif db_field.name == "tipo_material":
            kwargs["queryset"] = Material_producto.objects.order_by("material")

        elif db_field.name == "anio":
            kwargs["queryset"] = Anio.objects.order_by("anio")

        elif db_field.name == "mes":
            kwargs["queryset"] = Meses.objects.select_related(
                "anio"
            ).order_by(
                "anio__anio",
                "nombre_mes"
            )

        elif db_field.name == "mesmoda":
            kwargs["queryset"] = MesModa.objects.select_related(
                "mes",
                "coleccion"
            ).order_by(
                "mes__anio__anio",
                "mes__nombre_mes",
                "titulo"
            )

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class BaseAdmin(OrdenForeignKeyMixin, admin.ModelAdmin):
    def __init__(self, model, *args, **kwargs):
        self.list_display = Attr(model)
        self.list_display_links = [Attr(model)[0]]
        super().__init__(model, *args, **kwargs)

    def get_list_display(self, request):
        return list(Attr(self.model))


class MesModa_galeriaInline(OrdenForeignKeyMixin, admin.StackedInline):
    model = MesModa_galeria
    extra = 0


@admin.register(Vortice)
class VorticeAdmin(BaseAdmin):
    list_display = list(BaseAdmin.list_display) + ["miniatura"]


@admin.register(Notificaciones)
class NotificacionesAdmin(BaseAdmin):
    pass


@admin.register(Seccion_Cliente)
class Seccion_ClienteAdmin(BaseAdmin):
    ordering = ["cliente"]


@admin.register(Coleccion)
class ColeccionAdmin(BaseAdmin):
    ordering = ["cliente__cliente", "tema_colec"]
    list_filter = ["cliente"]
    list_display = list(BaseAdmin.list_display) + ["miniatura"]


@admin.register(Tipo_articulo)
class Tipo_articuloAdmin(BaseAdmin):
    ordering = ["coleccion__cliente__cliente", "coleccion__tema_colec", "nombre_articulo"]
    list_filter = ["coleccion"]
    search_fields = ["nombre_articulo", "coleccion__tema_colec", "coleccion__cliente__cliente"]

    def get_list_display(self, request):
        return super().get_list_display(request) + ["miniatura"]

    @admin.display(description="Imagen")
    def miniatura(self, obj):
        if obj.imagen_articulo:
            return format_html(
                '<img src="{}" width="100" style="object-fit: contain;" />',
                obj.imagen_articulo.url
            )
        return "-"


@admin.register(DetallePrendaColeccion)
class DetallePrendaColeccionAdmin(OrdenForeignKeyMixin, admin.ModelAdmin):
    list_display = ["id", "tipo_articulo", "activo"]
    list_filter = ["tipo_articulo", "activo"]
    search_fields = [
        "tipo_articulo__nombre_articulo",
        "tipo_articulo__coleccion__tema_colec",
        "tipo_articulo__coleccion__cliente__cliente",
        "detalle",
    ]
    ordering = [
        "tipo_articulo__coleccion__cliente__cliente",
        "tipo_articulo__coleccion__tema_colec",
        "tipo_articulo__nombre_articulo",
    ]


@admin.register(Material_producto)
class Material_productoAdmin(BaseAdmin):
    ordering = ["material"]


class ProdPrendaResource(resources.ModelResource):
    tipo_produc = fields.Field(column_name="Tipo de Producto")
    coleccion = fields.Field(column_name="Colección")
    seccion = fields.Field(column_name="Sección")
    tipo_material = fields.Field(attribute="tipo_material", column_name="Material")
    detalle_prenda = fields.Field(column_name="Detalle de Prenda")

    class Meta:
        model = Prod_prenda
        import_id_fields = ('id',)
        fields = (
            "id",
            "visible",
            "tipo_produc",
            "coleccion",
            "seccion",
            "nombre_produc",
            "detalle_prenda",
            "descripcion_produc",
            "tipo_material",
            "price",
            "has_sizes",
            "is_unique",
            "estado",
            "imagen_produc_01",
            "imagen_produc_02",
            "imagen_produc_03",
            "video_produc",
        )
        export_order = fields

    def dehydrate_tipo_produc(self, obj):
        return obj.tipo_produc.nombre_articulo if obj.tipo_produc else ""

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

    def dehydrate_detalle_prenda(self, obj):
        if obj.detalle_prenda:
            return obj.detalle_prenda.id
        return ""

    def before_import_row(self, row, **kwargs):
        tipo_producto = row.get("Tipo de Producto")
        coleccion = row.get("Colección")
        seccion = row.get("Sección")

        if tipo_producto:
            tipo_producto_obj = Tipo_articulo.objects.filter(
                nombre_articulo=tipo_producto
            )

            if coleccion:
                tipo_producto_obj = tipo_producto_obj.filter(
                    coleccion__tema_colec=coleccion
                )

            if seccion:
                tipo_producto_obj = tipo_producto_obj.filter(
                    coleccion__cliente__cliente=seccion
                )

            tipo_producto_obj = tipo_producto_obj.first()

            if tipo_producto_obj:
                row["tipo_produc"] = tipo_producto_obj.id
            else:
                row["tipo_produc"] = None
        else:
            row["tipo_produc"] = None

        material = row.get("Material", "")
        material = material.strip() if material else None

        if material:
            material_obj, created = Material_producto.objects.get_or_create(
                material=material
            )
            row["tipo_material"] = material_obj.id
        else:
            row["tipo_material"] = None

        detalle_prenda = row.get("Detalle de Prenda", "")

        if detalle_prenda:
            detalle_obj = DetallePrendaColeccion.objects.filter(
                id=detalle_prenda
            ).first()
            row["detalle_prenda"] = detalle_obj.id if detalle_obj else None
        else:
            row["detalle_prenda"] = None




@admin.register(Prod_prenda)
class Prod_prendaAdmin(OrdenForeignKeyMixin, ImportExportModelAdmin):
    resource_class = ProdPrendaResource
    formats = [XLSX]

    list_display = [
        "id",
        "miniatura",
        "visible",
        "tipo_produc",
        "nombre_produc",
        "detalle_prenda",
        "descripcion_corta",
        "tipo_material",
        "price",
        "has_sizes",
    ]

    list_filter = [
        "visible",
        "tipo_produc",
        "detalle_prenda",
        "tipo_material",
        "estado",
    ]

    search_fields = [
        "nombre_produc",
        "tipo_produc__nombre_articulo",
        "tipo_produc__coleccion__tema_colec",
        "detalle_prenda__detalle",
        "tipo_material__material",
    ]

    list_editable = [
        "visible",
        "tipo_produc",
        "nombre_produc",
        "detalle_prenda",
        "tipo_material",
        "price",
        "has_sizes",
    ]

    list_display_links = ["miniatura", "id"]

    ordering = [
        "tipo_produc__coleccion__cliente__cliente",
        "tipo_produc__coleccion__tema_colec",
        "tipo_produc__nombre_articulo",
        "nombre_produc",
    ]

    @admin.display(description="Imagen")
    def miniatura(self, obj):
        if obj.imagen_produc_01:
            return format_html(
                '<img src="{}" width="50" height="50"/>',
                obj.imagen_produc_01.url
            )
        return "Sin imagen"

    @admin.display(description="Descripción")
    def descripcion_corta(self, obj):
        if obj.detalle_prenda and obj.detalle_prenda.detalle:
            return f"{obj.detalle_prenda.detalle[:30]}..."
        if obj.descripcion_produc:
            return f"{obj.descripcion_produc[:30]}..."
        return "Sin descripción"


@admin.register(Servicios)
class ServiciosAdmin(BaseAdmin):
    pass


@admin.register(GiftCard)
class GiftCardAdmin(BaseAdmin):
    list_display = list(BaseAdmin.list_display) + ["miniatura"]


@admin.register(Anio)
class Anioadmin(BaseAdmin):
    ordering = ["anio"]


@admin.register(Meses)
class MesesAdmin(BaseAdmin):
    ordering = ["anio__anio", "nombre_mes"]
    list_filter = ["anio"]


@admin.register(MesModa)
class MesModaAdmin(BaseAdmin):
    ordering = ["mes__anio__anio", "mes__nombre_mes", "titulo"]
    list_filter = ["mes", "coleccion"]
    list_display = list(BaseAdmin.list_display) + ["miniatura"]
    inlines = [MesModa_galeriaInline]


@admin.register(MesModa_galeria)
class MesModa_galeriaAdmin(BaseAdmin):
    ordering = ["mesmoda__titulo"]
    list_display = list(BaseAdmin.list_display) + ["miniatura"]


@admin.register(Banco)
class BancoAdmin(BaseAdmin):
    ordering = ["nombre"]
    list_display = list(BaseAdmin.list_display)
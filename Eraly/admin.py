from django.contrib import admin
from django.utils.html import format_html

from Eraly.models import *
from benitez.snippers import Attr


# ============================================================
# CONFIGURACIÓN GENERAL DEL ADMIN
# ============================================================

@admin.register(ConfiguracionEmpresa)
class ConfiguracionEmpresaAdmin(admin.ModelAdmin):
    """Configuración de la empresa - solo una instancia"""

    list_display = ("id", "nombre", "email", "telefono", "whatsapp")
    list_display_links = ("id", "nombre")

    def has_add_permission(self, request):
        # Solo permite una instancia
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


# ============================================================
# CLASE BASE PARA ADMIN
# ============================================================

class BaseAdmin(admin.ModelAdmin):
    """Clase base que usa Attr para list_display automático"""

    def __init__(self, model, admin_site):
        self.list_display = Attr(model)
        if self.list_display:
            self.list_display_links = [self.list_display[0]]
        super().__init__(model, admin_site)

    def get_list_display(self, request):
        return list(Attr(self.model))


# ============================================================
# INLINES
# ============================================================

class BeneficioLandingInline(admin.StackedInline):
    """Beneficios dentro de LandingPage"""
    model = BeneficioLanding
    extra = 0
    fields = ('titulo', 'descripcion', 'icono','imagen','imagen2' ,'orden')
    ordering = ('orden',)



class CaracteristicaPlanInline(admin.TabularInline):
    """Características dentro de PlanLanding"""
    model = CaracteristicaPlan
    extra = 0
    fields = ('texto', 'incluido', 'orden')
    ordering = ('orden',)



class PlanLandingInline(admin.StackedInline):
    """Planes dentro de LandingPage"""
    model = PlanLanding
    extra = 0
    fields = ('nombre', 'precio', 'periodo','destacado', 'orden')
    ordering = ('orden',)


# ============================================================
# ADMIN LANDING PAGE
# ============================================================

@admin.register(LandingPage)
class LandingPageAdmin(BaseAdmin):
    """Administración de páginas de aterrizaje"""

    list_display = ['id', 'nombre', 'slug', 'activo', 'orden']
    list_display_links = ['id', 'nombre']
    list_editable = ['activo', 'orden']
    list_filter = ['activo']
    search_fields = ['nombre', 'slug']
    prepopulated_fields = {'slug': ('nombre',)}
    ordering = ['orden', 'id']

    inlines = [BeneficioLandingInline, PlanLandingInline]

    fieldsets = (
        ('Información básica', {
            'fields': ('nombre', 'slug', 'activo', 'orden')
        }),
        ('Contenido principal', {
            'fields': ('titulo_seo', 'titulo_hero', 'subtitulo_hero', 'imagen_hero')
        }),
        ('Configuración avanzada', {
            'classes': ('collapse',),
            'fields': (
                'titulo_beneficios',
                'subtitulo_beneficios',
                'subtitulo2_beneficios',
                'categoria_titulo',
                'categoria_icono',
                'descripcion_seccion',
                'cta_titulo',
                'cta_texto',
                'cta_boton_texto',
                'cta_boton_url',
            )
        }),
    )


# ============================================================
# ADMIN BENEFICIO LANDING
# ============================================================

@admin.register(BeneficioLanding)
class BeneficioLandingAdmin(BaseAdmin):
    """Administración de beneficios"""

    list_display = ['id', 'titulo', 'landing', 'icono', 'orden']
    list_display_links = ['id', 'titulo']
    list_editable = ['orden']
    list_filter = ['landing']
    search_fields = ['titulo', 'descripcion']
    ordering = ['landing', 'orden']

# ============================================================
# ADMIN PLAN LANDING
# ============================================================

@admin.register(PlanLanding)
class PlanLandingAdmin(BaseAdmin):
    """Administración de planes de precios"""

    list_display = ['id', 'nombre', 'landing', 'precio', 'periodo','destacado', 'orden']
    list_display_links = ['id', 'nombre']
    list_editable = ['precio', 'destacado', 'orden']
    list_filter = ['landing', 'destacado']
    search_fields = ['nombre']
    ordering = ['landing', 'orden']

    inlines = [CaracteristicaPlanInline]

    fieldsets = (
        ('Información del plan', {
            'fields': ('nombre', 'landing', 'precio',  'periodo','destacado', 'orden')
        }),
        ('Descripción', {
            'fields': ('descripcion',)
        }),
    )

# ============================================================
# ADMIN CARACTERÍSTICA PLAN
# ============================================================

@admin.register(CaracteristicaPlan)
class CaracteristicaPlanAdmin(BaseAdmin):
    """Administración de características de planes"""

    list_display = ['id', 'plan', 'texto', 'incluido', 'periodo','orden']
    list_display_links = ['id', 'texto']
    list_editable = ['texto', 'incluido', 'orden']
    list_filter = ['plan', 'incluido']
    search_fields = ['texto']
    ordering = ['plan', 'orden']


# ============================================================
# ADMIN NEWSLETTER
# ============================================================

@admin.register(EralyNewsletter)
class EralyNewsletterAdmin(admin.ModelAdmin):
    """Administración de suscriptores al newsletter"""

    list_display = ['id', 'email', 'activo', 'fecha']
    list_display_links = ['id', 'email']
    list_editable = ['activo']
    list_filter = ['activo', 'fecha']
    search_fields = ['email']
    ordering = ['-fecha']
    readonly_fields = ['fecha']

    actions = ['exportar_csv']

    def exportar_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="suscriptores.csv"'

        writer = csv.writer(response)
        writer.writerow(['Email', 'Activo', 'Fecha suscripción'])

        for suscriptor in queryset:
            writer.writerow([
                suscriptor.email,
                'Sí' if suscriptor.activo else 'No',
                suscriptor.fecha.strftime('%d/%m/%Y %H:%M')
            ])

        return response

    exportar_csv.short_description = "📎 Exportar a CSV"

    def has_add_permission(self, request):
        return False


# ============================================================
# ADMIN SERVICIOS WEB / PRODUCTOS ERALY
# ============================================================
class TipoServicioWebInline(admin.StackedInline):
    model = TipoServicioWeb
    extra = 0

    fields = (
        'titulo',
        'descripcion',
        'etiqueta',
        'icono',
        'color',
        'orden',
    )

    ordering = ('orden',)
class BeneficioServicioInline(admin.StackedInline):
    model = BeneficioServicio
    extra = 0
    fields = (
        'titulo',
        'descripcion',
        'icono',
        'orden',
    )
    ordering = ('orden',)


class DominioServicioInline(admin.TabularInline):
    model = DominioServicio
    extra = 0
    fields = (
        'extension',
        'precio',
        'periodo',
        'orden',
    )
    ordering = ('orden',)


class PlanServicioInline(admin.StackedInline):
    model = PlanServicio
    extra = 0
    fields = (
    'tipo_web',
    'nombre',
    'descripcion',
    'precio',
    'periodo',
    'destacado',
    'etiqueta',
    'icono',
    'color',
    'boton_texto',
    'boton_url',
    'orden',
    )
    ordering = ('orden',)


class PreguntaServicioInline(admin.StackedInline):
    model = PreguntaServicio
    extra = 0
    fields = (
        'pregunta',
        'respuesta',
        'orden',
    )
    ordering = ('orden',)


class CaracteristicaPlanServicioInline(admin.TabularInline):
    model = CaracteristicaPlanServicio
    extra = 0
    fields = (
        'texto',
        'incluido',
        'orden',
    )
    ordering = ('orden',)


@admin.register(ServicioProducto)
class ServicioProductoAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'tipo',
        'titulo',
        'activo',
        'orden',
    ]

    list_display_links = ['id', 'titulo']

    list_editable = [
        'activo',
        'orden',
    ]

    list_filter = [
        'tipo',
        'activo',
    ]

    search_fields = [
        'titulo',
        'subtitulo',
        'descripcion',
    ]

    ordering = [
        'orden',
        'id',
    ]

    inlines = [
        BeneficioServicioInline,
        DominioServicioInline,
        TipoServicioWebInline,
        PlanServicioInline,
        PreguntaServicioInline,
    ]

    fieldsets = (
        ('Información principal', {
            'fields': (
                'tipo',
                'titulo',
                'subtitulo',
                'descripcion',
                'activo',
                'orden',
            )
        }),
        ('Imágenes', {
            'fields': (
                'imagen_banner',
                'imagen_1',
                'imagen_2',
                'imagen_3',
                'imagen_4',
            )
        }),
        ('Botón principal', {
            'fields': (
                'boton_texto',
                'boton_url',
            )
        }),
    )


@admin.register(BeneficioServicio)
class BeneficioServicioAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'servicio',
        'titulo',
        'icono',
        'orden',
    ]

    list_display_links = [
        'id',
        'titulo',
    ]

    list_editable = [
        'orden',
    ]

    list_filter = [
        'servicio',
    ]

    search_fields = [
        'titulo',
        'descripcion',
    ]

    ordering = [
        'servicio',
        'orden',
    ]


@admin.register(DominioServicio)
class DominioServicioAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'servicio',
        'extension',
        'precio',
        'periodo',
        'orden',
    ]

    list_display_links = [
        'id',
        'extension',
    ]

    list_editable = [
        'precio',
        'periodo',
        'orden',
    ]

    list_filter = [
        'servicio',
    ]

    search_fields = [
        'extension',
    ]

    ordering = [
        'servicio',
        'orden',
    ]


@admin.register(PlanServicio)
class PlanServicioAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'servicio',
        'tipo_web',
        'nombre',
        'precio',
        'periodo',
        'destacado',
        'etiqueta',
        'orden',
    ]

    list_display_links = [
        'id',
        'nombre',
    ]

    list_editable = [
        'precio',
        'destacado',
        'orden',
    ]

    list_filter = [
        'servicio',
        'destacado',
    ]

    search_fields = [
        'nombre',
        'descripcion',
    ]

    ordering = [
        'servicio',
        'orden',
    ]

    inlines = [
        CaracteristicaPlanServicioInline,
    ]


@admin.register(CaracteristicaPlanServicio)
class CaracteristicaPlanServicioAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'plan',
        'texto',
        'incluido',
        'orden',
    ]

    list_display_links = [
        'id',
        'texto',
    ]

    list_editable = [
        'incluido',
        'orden',
    ]

    list_filter = [
        'plan',
        'incluido',
    ]

    search_fields = [
        'texto',
    ]

    ordering = [
        'plan',
        'orden',
    ]


@admin.register(PreguntaServicio)
class PreguntaServicioAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'servicio',
        'pregunta',
        'orden',
    ]

    list_display_links = [
        'id',
        'pregunta',
    ]

    list_editable = [
        'orden',
    ]

    list_filter = [
        'servicio',
    ]

    search_fields = [
        'pregunta',
        'respuesta',
    ]

    ordering = [
        'servicio',
        'orden',
    ]

@admin.register(TipoServicioWeb)
class TipoServicioWebAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'servicio',
        'titulo',
        'etiqueta',
        'orden',
    ]

    list_display_links = [
        'id',
        'titulo',
    ]

    list_editable = [
        'orden',
    ]

    list_filter = [
        'servicio',
    ]

    search_fields = [
        'titulo',
        'descripcion',
    ]

    ordering = [
        'servicio',
        'orden',
    ]
from django.db import models
from django.utils.text import slugify
# Create your models here.


class ConfiguracionEmpresa(models.Model):
    """Configuración general del sitio"""
    nombre = models.CharField(max_length=100, default="EralySoft")
    logo_principal = models.ImageField(upload_to='eraly/', help_text="Logo blanco para fondo oscuro")
    logo_alternativo = models.ImageField(upload_to='eraly/', help_text="Logo oscuro para fondo claro")
    favicon = models.ImageField(upload_to='eraly/')

    # Contacto
    email = models.EmailField(default="info@eralysoft.com")
    email_soporte = models.EmailField(default="soporte@eralysoft.com")
    telefono = models.CharField(max_length=20, default="099 999 9999")
    telefono_2 = models.CharField(max_length=20, blank=True)
    whatsapp = models.CharField(max_length=20, default="593999999999")
    direccion = models.TextField(default="Quito - Ecuador")
    horario = models.CharField(max_length=200, default="Lun-Vie 9am-6pm, Sáb 9am-1pm")

    # SEO
    meta_titulo = models.CharField(max_length=200, default="EralySoft - Soluciones Tecnológicas para tu Negocio")
    meta_descripcion = models.TextField( default="Sistemas POS, páginas web, hosting, dominios, correos corporativos y facturación electrónica SRI")
    meta_keywords = models.CharField(max_length=500, default="POS, facturación electrónica, páginas web, hosting, Ecuador")

    # Redes Sociales
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    imagen_compartir = models.ImageField(
        upload_to='eraly/',
        blank=True,
        null=True,
        help_text="Imagen para WhatsApp, Facebook y LinkedIn (1200x630)"
    )

    # Contacto página
    contacto_titulo = models.CharField(max_length=120, default="Contáctanos")
    contacto_subtitulo = models.CharField(max_length=180, default="Estamos aquí para ayudarte")
    contacto_banner = models.ImageField(upload_to='eraly/contacto/', blank=True, null=True)

    contacto_badge = models.CharField(max_length=100, default="Soporte 24/7")
    contacto_titulo_soporte = models.CharField(max_length=160, default="¿Necesitas ayuda técnica?")
    contacto_texto_soporte = models.TextField(default="Nuestro equipo de soporte está disponible para atenderte.")

    contacto_titulo_intro = models.CharField(max_length=160, default="Hablemos")
    contacto_texto_intro = models.TextField(default="Cuéntanos tu proyecto y te asesoramos sin compromiso.")

    ciudad = models.CharField(max_length=100, default="Machala")
    oficina = models.CharField(max_length=150, default="Oficina principal")
    mapa_iframe = models.TextField(blank=True, help_text="Pegar iframe de Google Maps")

    class Meta:
        verbose_name = "00. Configuración Empresa"
        verbose_name_plural = "00. Configuración Empresa"

    def __str__(self):
        return self.nombre


# models de landing (dedentados — estaban indentados dentro de ConfiguracionEmpresa)
class LandingPage(models.Model):
    nombre = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)
    titulo_seo = models.CharField(max_length=180)
    titulo_hero = models.CharField(max_length=120)
    subtitulo_hero = models.CharField(max_length=180)
    imagen_hero = models.ImageField(upload_to="eraly/", blank=True, null=True)

    titulo_beneficios = models.CharField(max_length=120, default="¿Por qué elegirnos?")
    subtitulo_beneficios = models.CharField(max_length=180, blank=True)
    subtitulo2_beneficios = models.CharField(max_length=180, blank=True)

    categoria_titulo = models.CharField(max_length=160)
    categoria_icono = models.CharField(max_length=80, default="fa-solid fa-utensils")
    titulo_seccion = models.CharField(max_length=160)
    descripcion_seccion = models.TextField(blank=True)

    cta_titulo = models.CharField(max_length=160)
    cta_texto = models.TextField(blank=True)
    cta_boton_texto = models.CharField(max_length=80, default="Solicitar demo")
    cta_boton_url = models.CharField(max_length=200, default="/contacto/")

    activo = models.BooleanField(default=True)
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["orden", "nombre"]
        verbose_name = "10. Solución POS"
        verbose_name_plural = "10. Soluciones POS"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre





class BeneficioLanding(models.Model):
    landing = models.ForeignKey(LandingPage, on_delete=models.CASCADE, related_name="beneficios")
    titulo = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=180)
    descripcion_1 = models.TextField(max_length=400, blank=True, default="")
    icono = models.CharField(max_length=80, default="fa-solid fa-check")
    imagen = models.ImageField(upload_to="eraly/", blank=True, null=True)
    imagen2 = models.ImageField(upload_to="eraly/", blank=True, null=True)
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["orden"]
        verbose_name = "11. Beneficio POS"
        verbose_name_plural = "11. Beneficios POS"

    def __str__(self):
        return self.titulo




class PlanLanding(models.Model):
    landing = models.ForeignKey(LandingPage, on_delete=models.CASCADE, related_name="planes")
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=180)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    periodo = models.CharField(max_length=30, default="/mes")
    destacado = models.BooleanField(default=False)
    etiqueta = models.CharField(max_length=80, blank=True)
    boton_texto = models.CharField(max_length=80, default="Contratar")
    boton_url = models.CharField(max_length=200, default="/contacto/")
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["orden"]
        verbose_name = "12. Plan POS"
        verbose_name_plural = "12. Planes POS"

    def __str__(self):
        return self.nombre


class CaracteristicaPlan(models.Model):
    plan = models.ForeignKey(PlanLanding, on_delete=models.CASCADE, related_name="caracteristicas")
    texto = models.CharField(max_length=160)
    incluido = models.BooleanField(default=True)
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["orden"]
        verbose_name = "13. Característica Plan POS"
        verbose_name_plural = "13. Características Plan POS"

    def __str__(self):
        return self.texto


class EralyNewsletter(models.Model):
    email = models.EmailField(unique=True)
    activo = models.BooleanField(default=True)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Suscriptores Sistema POS'
        verbose_name_plural = 'Suscriptores Sistema POS'

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-fecha']
        verbose_name = "20. Suscriptor"
        verbose_name_plural = "20. Suscriptores"


class ServicioProducto(models.Model):
    TIPO_CHOICES = (
        ('hosting', 'Hosting + Dominio'),
        ('web', 'Páginas Web'),
        ('correos', 'Correos Corporativos'),
        ('facturacion', 'Facturación SRI'),
        ('apps', 'Apps a Medida'),
    )

    tipo = models.CharField(max_length=30, choices=TIPO_CHOICES, unique=True)
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=250)
    descripcion = models.TextField(blank=True)

    imagen_banner = models.ImageField(upload_to="eraly/productos/", blank=True, null=True)
    imagen_1 = models.ImageField(upload_to="eraly/productos/", blank=True, null=True)
    imagen_2 = models.ImageField(upload_to="eraly/productos/", blank=True, null=True)
    imagen_3 = models.ImageField(upload_to="eraly/productos/", blank=True, null=True)
    imagen_4 = models.ImageField(upload_to="eraly/productos/", blank=True, null=True)

    boton_texto = models.CharField(max_length=80, default="Cotizar ahora")
    boton_url = models.CharField(max_length=200, default="/eraly/contacto/")

    activo = models.BooleanField(default=True)
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["orden"]
        verbose_name = "01. Servicio Web"
        verbose_name_plural = "01. Servicios Web"

    def __str__(self):
        return self.titulo


class BeneficioServicio(models.Model):
    servicio = models.ForeignKey(
        ServicioProducto,
        on_delete=models.CASCADE,
        related_name="beneficios"
    )
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    icono = models.CharField(max_length=80, default="fa-solid fa-check")
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["orden"]
        verbose_name = "02. Beneficio del Servicio"
        verbose_name_plural = "02. Beneficios del Servicio"

    def __str__(self):
        return self.titulo


class DominioServicio(models.Model):
    servicio = models.ForeignKey(
        ServicioProducto,
        on_delete=models.CASCADE,
        related_name="dominios"
    )
    extension = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    periodo = models.CharField(max_length=30, default="/año")
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["orden"]
        verbose_name = "03. Dominio del Servicio"
        verbose_name_plural = "03. Dominios del Servicio"

    def __str__(self):
        return self.extension
    
class TipoServicioWeb(models.Model):
    servicio = models.ForeignKey(
        ServicioProducto,
        on_delete=models.CASCADE,
        related_name="tipos_web"
    )

    titulo = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=250)

    etiqueta = models.CharField(
        max_length=80,
        blank=True,
        default=""
    )

    icono = models.CharField(
        max_length=80,
        default="fa-solid fa-globe"
    )

    color = models.CharField(
        max_length=20,
        default="#00839a"
    )

    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["orden"]
        verbose_name = "07. Tipo de Servicio Web"
        verbose_name_plural = "07. Tipos de Servicio Web"

    def __str__(self):
        return self.titulo

class PlanServicio(models.Model):
    servicio = models.ForeignKey(
        ServicioProducto,
        on_delete=models.CASCADE,
        related_name="planes"
    )
    tipo_web = models.ForeignKey(
        TipoServicioWeb,
        on_delete=models.SET_NULL,
        related_name="planes",
        blank=True,
        null=True
    )
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200, blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    periodo = models.CharField(max_length=30, default="/mes")
    destacado = models.BooleanField(default=False)

    etiqueta = models.CharField(max_length=80, blank=True)
    icono = models.CharField(max_length=80, default="fa-solid fa-check")
    color = models.CharField(max_length=20, default="#00839a")

    boton_texto = models.CharField(max_length=80, default="Contratar")
    boton_url = models.CharField(max_length=200, default="/eraly/contacto/")
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["orden"]
        verbose_name = "04. Plan del Servicio"
        verbose_name_plural = "04. Planes del Servicio"

    def __str__(self):
        return f"{self.servicio.get_tipo_display()} - {self.nombre}"


class CaracteristicaPlanServicio(models.Model):
    plan = models.ForeignKey(
        PlanServicio,
        on_delete=models.CASCADE,
        related_name="caracteristicas"
    )
    texto = models.CharField(max_length=180)
    incluido = models.BooleanField(default=True)
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["orden"]
        verbose_name = "05. Característica del Plan"
        verbose_name_plural = "05. Características del Plan"

    def __str__(self):
        return self.texto


class PreguntaServicio(models.Model):
    servicio = models.ForeignKey(
        ServicioProducto,
        on_delete=models.CASCADE,
        related_name="preguntas"
    )
    pregunta = models.CharField(max_length=200)
    respuesta = models.TextField()
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["orden"]
        verbose_name = "06. Pregunta Frecuente"
        verbose_name_plural = "06. Preguntas Frecuentes"


    def __str__(self):
        return self.pregunta


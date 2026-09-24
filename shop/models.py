
from urllib.parse import parse_qs, urlparse
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.text import slugify



class Marca(models.Model):
    favicon = models.ImageField(upload_to='colexin/', help_text='imagenes 200*200', null=True, blank=True)
    logo_color = models.ImageField(upload_to='colexin/', help_text='imagenes 200*200', null=True, blank=True)
    logo_blanco = models.ImageField(upload_to='colexin/', help_text='imagenes 200*200', null=True, blank=True)
    whatsapp = models.CharField(max_length=11, null=True, blank=True)
    celular = models.CharField(max_length=11, null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    facebook= models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    tiktok = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)

    # =====================================================
    # IMÁGENES PARA REDES SOCIALES / OPEN GRAPH
    # =====================================================

    meta_inicio = models.ImageField(
        upload_to='colexin/meta/',
        help_text='Imagen para compartir la página de inicio. Recomendado: 1200 × 630 px',
        null=True,
        blank=True
    )

    meta_about = models.ImageField(
        upload_to='colexin/meta/',
        help_text='Imagen para compartir la página Nosotros. Recomendado: 1200 × 630 px',
        null=True,
        blank=True
    )

    meta_blog = models.ImageField(
        upload_to='colexin/meta/',
        help_text='Imagen para compartir el blog. Recomendado: 1200 × 630 px',
        null=True,
        blank=True
    )

    meta_contacto = models.ImageField(
        upload_to='colexin/meta/',
        help_text='Imagen para compartir la página de contacto. Recomendado: 1200 × 630 px',
        null=True,
        blank=True
    )

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>"%self.logo_color)


    class Meta:
        verbose_name_plural = "2. Colexin"

class Category(models.Model):
    icono = models.ImageField(upload_to='colexin', blank=True)
    name = models.CharField(max_length=200)


    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def miniatura(self):
        if self.icono:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.icono.url))
        return "Sin imagen"

class Product(models.Model):
    # Otros campos de tu modelo
    principal = models.BooleanField(default=False)
    slider = models.BooleanField(default=False)
    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image_1 = models.ImageField(upload_to='colexin', blank=True)
    image_2 = models.ImageField(upload_to='colexin', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name

    def miniatura(self):
        if self.image_1:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.image_1.url))
        return "Sin imagen"

class CategoriaBlogColexin(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    activo = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]
        verbose_name = "BLOG COLEXIN- 01 Categoría"
        verbose_name_plural = "BLOG COLEXIN- 01 Categorías"


class BlogColexin(models.Model):
    categoria = models.ForeignKey(
        CategoriaBlogColexin,
        on_delete=models.PROTECT,
        related_name="publicaciones_colexin",
    )

    titulo = models.CharField(max_length=180)

    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
    )

    subtitulo = models.CharField(
        max_length=300,
        blank=True,
    )

    imagen_principal = models.ImageField(
        upload_to="colexin/blog/principal/",
        help_text="Imagen vertical recomendada: 800 x 1145 px",
    )

    imagen_horizontal = models.ImageField(
        upload_to="colexin/blog/horizontal/",
        null=True,
        blank=True,
        help_text="Imagen horizontal recomendada: 1920 x 1080 px",
    )

    contenido = models.TextField(
        help_text="Puede escribir directamente código HTML.",
    )

    video_youtube = models.URLField(
        max_length=500,
        blank=True,
        help_text=(
            "Pegue el enlace completo de YouTube. "
            "Ejemplo: https://youtu.be/xxxxxxxxxxx"
        ),
    )

    activo = models.BooleanField(
        default=True,
        help_text="Visible en el sitio web",
    )

    destacado = models.BooleanField(
        default=False,
        help_text="Mostrar como publicación destacada",
    )

    fecha_publicacion = models.DateTimeField(default=timezone.now)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_base = slugify(self.titulo)[:180] or "publicacion"
            slug_nuevo = slug_base
            numero = 2

            existentes = BlogColexin.objects.exclude(pk=self.pk)

            while existentes.filter(slug=slug_nuevo).exists():
                slug_nuevo = f"{slug_base}-{numero}"
                numero += 1

            self.slug = slug_nuevo

        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse(
            "blog_detalle_colexin",
            kwargs={"slug": self.slug},
        )

    @property
    def video_embed_url(self):
        if not self.video_youtube:
            return ""

        parsed = urlparse(self.video_youtube)
        host = parsed.netloc.lower().replace("www.", "")
        video_id = ""

        if host == "youtu.be":
            video_id = parsed.path.strip("/").split("/")[0]

        elif host in (
            "youtube.com",
            "m.youtube.com",
            "music.youtube.com",
        ):
            if parsed.path == "/watch":
                video_id = parse_qs(parsed.query).get("v", [""])[0]

            elif parsed.path.startswith(("/embed/", "/shorts/")):
                partes = parsed.path.strip("/").split("/")

                if len(partes) > 1:
                    video_id = partes[1]

        if not video_id:
            return ""

        return f"https://www.youtube.com/embed/{video_id}"

    def vista_previa(self):
        if not self.imagen_principal:
            return "-"

        return mark_safe(
            '<img width="140" height="80" '
            'style="object-fit:cover" src="{}">'.format(
                self.imagen_principal.url
            )
        )

    class Meta:
        ordering = ["-fecha_publicacion"]
        verbose_name = "BLOG COLEXIN- 02 Publicación"
        verbose_name_plural = "BLOG COLEXIN- 02 Publicaciones"


class ImagenBlogColexin(models.Model):
    blog = models.ForeignKey(
        BlogColexin,
        on_delete=models.CASCADE,
        related_name="galeria",
    )

    imagen = models.ImageField(
        upload_to="colexin/blog/galeria/",
    )

    titulo = models.CharField(
        max_length=150,
        blank=True,
        help_text="Descripción opcional de la imagen",
    )

    orden = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.blog} - imagen {self.orden}"

    def vista_previa(self):
        if not self.imagen:
            return "-"

        return mark_safe(
            '<img width="120" height="80" '
            'style="object-fit:cover" src="{}">'.format(
                self.imagen.url
            )
        )

    class Meta:
        ordering = ["orden", "id"]
        verbose_name = "BLOG COLEXIN- 03 Imagen"
        verbose_name_plural = "BLOG COLEXIN- 03 Galería"
from ckeditor.fields import RichTextField
from django.contrib.admin import BooleanFieldListFilter
from django.db import models
from django.urls import reverse

# Create your models here.
from django.utils.safestring import mark_safe


# Create your models here.

class Notificaciones(models.Model):
    texto_1= models.CharField(max_length=100, null=True, blank=True)
    texto_2 = models.CharField(max_length=100, null=True, blank=True)
    texto_3 = models.CharField(max_length=100, null=True, blank=True)
    texto_4 = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "6. Notificaciones"

class Vortice(models.Model):
    favicon=models.ImageField(upload_to='vortice',null=True,  blank=True, help_text='imagenes 20*20')
    logo_horizontal= models.ImageField(upload_to='vortice',null=True, blank=True, help_text='imagenes 20*20')
    logo_amarillo= models.ImageField(upload_to='vortice', blank=True, null=True, help_text='imagenes 20*20')
    whatsapp= models.CharField(max_length=11, null=True, blank=True)
    celular= models.CharField(max_length=11, null=True, blank=True)
    correo= models.EmailField(null=True, blank=True)
    direccion= models.CharField(max_length=100, null=True, blank=True)
    facebook= models.CharField(max_length=100, null=True, blank=True)
    instagram= models.CharField(max_length=100, null=True, blank=True)
    tiktok= models.CharField(max_length=100, null=True, blank=True)
    x= models.CharField(max_length=100, null=True, blank=True)
    pinterest= models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)
    s1_titulo = models.CharField(max_length=100, null=True, blank=True)
    s2_imagen = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='sobre nosotros imagen principal imagenes 2000 × 1262 px')
    about_titulo_01 = models.CharField(max_length=100, null=True, blank=True)
    about_subtitulo_01 = models.CharField(max_length=100, null=True, blank=True)
    about_titulo_02 = models.CharField(max_length=100, null=True, blank=True)
    about_subtitulo_02 = models.CharField(max_length=100, null=True, blank=True)
    about_03_imagen_01 = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='imagenes 2000 × 1262 px')
    about_titulo_03 = models.CharField(max_length=100, null=True, blank=True)
    about_subtitulo_03 = models.CharField(max_length=100, null=True, blank=True)
    about_03_imagen_2 = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='imagenes 2000 × 1262 px')
    about_03_imagen = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='imagenes logo')
    about_titulo_04 = models.CharField(max_length=100, null=True, blank=True)
    about_subtitulo_04 = models.CharField(max_length=100, null=True, blank=True)
    about_04_imagen = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='imagenes 2000 × 1262 px')
    about_04_imagen_2 = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='imagenes 2000 × 1262 px')
    img_termi_condi = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='imagenes 2000 × 1262 px')
    qr_img = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='imagenes 20*20')
    meta_inicio = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='imagenes 1200x630 px')
    meta_about = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='imagenes 1200x630 px')
    meta_hombre = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='imagenes 1200x630 px')
    meta_mujer= models.ImageField(upload_to='vortice', null=True, blank=True, help_text='imagenes 1200x630 px')
    meta_moda = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='imagenes 1200x630 px')
    meta_gifcard = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='imagenes 1200x630 px')

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>"%self.logo_horizontal)


    class Meta:
        verbose_name_plural = "1. Vortice"


class Seccion_Cliente(models.Model):
    mostrar= models.BooleanField(default=False)
    TIPO_CLIENTE = [
        ('hombre', 'Hombre'),
        ('mujer', 'Mujer'),
        ('unisex', 'Unisex'),
    ]
    cliente = models.CharField(
        max_length=10,
        choices=TIPO_CLIENTE,
        default='unisex',
    )
    imag_cliente_01 = models.FileField(upload_to='vortice', null=True, blank=True, help_text='vertical')
    imag_cliente_02 = models.FileField(upload_to='vortice', null=True, blank=True, help_text='horizontal')

    def __str__(self):
        return '%s '% (self.cliente)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>" % self.imag_cliente_01)

    class Meta:
        verbose_name_plural = "1. Seccion Cliente "



class Coleccion(models.Model):
    nuevo=models.BooleanField(default=False)
    activo = models.BooleanField(default=False)
    slider = models.BooleanField(default=False)
    cliente = models.ForeignKey(Seccion_Cliente, on_delete=models.CASCADE, null=True, blank=True)
    imag_colec_01 =models.FileField(upload_to='vortice', null=True, blank=True, help_text='vertical')
    imag_colec_02 =models.FileField(upload_to='vortice', null=True, blank=True, help_text='slider inicio horizontal')
    tema_colec =models.CharField(max_length=50, null=True, blank=True)
    sub_tema_colec = models.CharField(max_length=250, null=True, blank=True)
    detalle = models.TextField(max_length=500, null=True, blank=True)
    principal = models.BooleanField(default=False)
    imag_01 =models.FileField(upload_to='vortice', null=True, blank=True, help_text='principal Mujer vertical')
    tema_img_02 =models.CharField(max_length=50, null=True, blank=True, help_text='principal Mujer articulo nombre')
    imag_02 =models.FileField(upload_to='vortice', null=True, blank=True, help_text='principal Mujer articulo  horizontal')
    tema_img_03 =models.CharField(max_length=50, null=True, blank=True, help_text='principal Hombre articulo nombre')
    imag_03 =models.FileField(upload_to='vortice', null=True, blank=True, help_text='principal Hombre articulo  horizontal')
    imag_04 =models.FileField(upload_to='vortice', null=True, blank=True, help_text='principal Hombre vertical')

    def __str__(self):
        return '%s %s'% (self.cliente , self.tema_colec )

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>" % self.imag_colec_01)

    class Meta:
        verbose_name_plural = "2. Coleccion "


class Tipo_articulo(models.Model):
    activo_menu = models.BooleanField(default=False)
    activo_menu_colec = models.BooleanField(default=False)
    coleccion = models.ForeignKey(Coleccion, on_delete=models.CASCADE, null=True, blank=True)
    nombre_articulo = models.CharField(max_length=10,null=True, blank=True)
    imagen_articulo = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='100x100')

    def __str__(self):
        return '%s %s' % ( self.coleccion,  self.nombre_articulo)
    
    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>" % self.imagen_articulo)

    class Meta:
        verbose_name_plural = "4. Tipo de Articulo "


class Material_producto(models.Model):
    material = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return '%s' % (self.material)

    class Meta:
        verbose_name_plural = "4. Material de producto"




class Prod_prenda(models.Model):
    visible= models.BooleanField(default=False)
    tipo_produc = models.ForeignKey(Tipo_articulo, on_delete=models.CASCADE, null=True, blank=True)
    nombre_produc = models.CharField(max_length=100, null=True, blank=True)
    descripcion_produc = models.TextField(max_length=400, null=True, blank=True)
    tipo_material = models.ForeignKey(Material_producto, null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=999, decimal_places=2)

    has_sizes = models.BooleanField(default=True)  # ✅ Indica si el producto tiene tallas
    is_unique = models.BooleanField(default=False)  # ✅ Nuevo: Indica si es unidad única con talla única

    imagen_produc_01 = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='vertical')
    imagen_produc_02 = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='horizontal')
    imagen_produc_03 = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='horizontal')
    video_produc = models.FileField(upload_to='vortice', null=True, blank=True, help_text='video')
    ESTADO_CHOICES = [
        ('disp', 'Disponible'),
        ('agot', 'Agotado'),
        ('reserv', 'Reservado'),
    ]
    estado = models.CharField(
        max_length=6,
        choices=ESTADO_CHOICES,
        default='disp',
        verbose_name="Estado del producto",
        help_text="Selecciona si está disponible, agotado o reservado."
    )



    def __str__(self):
        return '%s %s' % ( self.tipo_produc,  self.nombre_produc)

    def miniatura(self):
        if self.imagen_produc_01:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.imagen_produc_01.url))
        return "Sin imagen"



    def get_absolute_url(self):
        return reverse('Vortice.views.producto_detalle',
                       args=[self.id])

    class Meta:
        verbose_name_plural = "5. Producto "


class Servicios(models.Model):
    video=models.FileField(upload_to='vortice',null=True, blank=True, help_text='video 200*200')
    imagen=models.ImageField(upload_to='vortice',null=True, blank=True, help_text='imagenes 200*200')
    servicio= models.CharField(max_length=100, null=True, blank=True)
    detalle= models.TextField(max_length=500, null=True, blank=True)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>"%self.imagen)


    class Meta:
        verbose_name_plural = "10. Servicios"




class GiftCard(models.Model):
    principal = models.BooleanField(default=False)
    activo = models.BooleanField(default=False)
    video=models.FileField(upload_to='vortice',null=True, blank=True, help_text='video 200*200')
    imagen=models.ImageField(upload_to='vortice',null=True, blank=True, help_text='imagenes 200*200')
    titulo= models.CharField(max_length=100, null=True, blank=True)
    detalle= models.TextField(max_length=500, null=True, blank=True)
    precio = models.DecimalField(max_digits=999, decimal_places=2)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>"%self.imagen)


    class Meta:
        verbose_name_plural = "11. GifCard"

class Anio(models.Model):
    anio= models.CharField(max_length=10, null=True, blank=True)
    def __str__(self):
        return '%s' % (self.anio)

    class Meta:
        verbose_name_plural = "12. Años"

class Meses(models.Model):
    anio = models.ForeignKey(Anio, on_delete=models.CASCADE, null=True, blank=True)
    nombre_mes= models.CharField(max_length=10, null=True, blank=True)
    def __str__(self):
        return '%s  %s' % (self.anio , self.nombre_mes)

    class Meta:
        verbose_name_plural = "13. Meses"

class MesModa(models.Model):
    principal = models.BooleanField(default=False)
    activo = models.BooleanField(default=False)
    izquierda = models.BooleanField(default=False)
    derecha = models.BooleanField(default=False)
    mes = models.ForeignKey(Meses, on_delete=models.CASCADE, null=True, blank=True)
    video=models.FileField(upload_to='vortice',null=True, blank=True, help_text='video 200*200')
    imagen=models.ImageField(upload_to='vortice',null=True, blank=True, help_text='imagenes 200*200')
    coleccion = models.ForeignKey(Coleccion, on_delete=models.CASCADE, null=True, blank=True)
    titulo= models.CharField(max_length=100, null=True, blank=True)
    subtitulo= models.CharField(max_length=100, null=True, blank=True)
    detalle= models.TextField(max_length=500, null=True, blank=True)
    def __str__(self):
        return '%s %s' % (self.mes , self.titulo)
    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>"%self.imagen)
    class Meta:
        verbose_name_plural = "14. Mes Moda"


class MesModa_galeria(models.Model):
    mesmoda = models.ForeignKey(MesModa, on_delete=models.CASCADE, null=True, blank=True)
    imagen_1 = models.ImageField(upload_to='vortice',null=True, blank=True, help_text='horizontal')
    imagen_2 = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='vertical')
    imagen_3 = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='vertical')
    imagen_4 = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='horizontal')
    imagen_5 = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='vertical')
    imagen_6 = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='vertical')
    def __str__(self):
        return '%s ' % (self.mesmoda )

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>"%self.imagen_1)
    class Meta:
        verbose_name_plural = "15. Mes Moda Galeria Fotos"


class Banco(models.Model):
    activo = models.BooleanField(default=False)
    nombre = models.CharField(max_length=20, null=True, blank=True)
    ahorro = models.BooleanField(default=True)
    corriente = models.BooleanField(default=False)
    numero= models.CharField(max_length=20, null=True, blank=True)




    class Meta:
        verbose_name_plural = "12. Banco"
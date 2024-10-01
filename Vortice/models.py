from ckeditor.fields import RichTextField
from django.contrib.admin import BooleanFieldListFilter
from django.db import models

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
    about_03_imagen = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='imagenes 2000 × 1262 px')
    about_03_imagen_2 = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='imagenes 2000 × 1262 px')
    about_titulo_04 = models.CharField(max_length=100, null=True, blank=True)
    about_subtitulo_04 = models.CharField(max_length=100, null=True, blank=True)
    about_04_imagen = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='imagenes 2000 × 1262 px')


    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>"%self.logo_horizontal)


    class Meta:
        verbose_name_plural = "1. Vortice"


class Seccion_Cliente(models.Model):
    cliente=models.CharField(max_length=30, null=True, blank=True)
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
    cliente = models.ForeignKey(Seccion_Cliente, on_delete=models.CASCADE, null=True, blank=True)
    imag_colec_01 =models.FileField(upload_to='vortice', null=True, blank=True, help_text='vertical')
    imag_colec_02 =models.FileField(upload_to='vortice', null=True, blank=True, help_text='horizontal')
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



class Imag_prenda_articulo(models.Model):
    tipo = models.CharField(max_length=30, null=True, blank=True)
    imagen = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='100x100')

    def __str__(self):
        return '%s ' % (self.tipo)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>" % self.imagen)

    class Meta:
        verbose_name_plural = "3. Imag_prenda_articulo "


class Tipo_articulo(models.Model):
    activo_menu = models.BooleanField(default=False)
    coleccion = models.ForeignKey(Coleccion, on_delete=models.CASCADE, null=True, blank=True)
    nombre_articulo = models.CharField(max_length=10,null=True, blank=True)
    imagen_articulo = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='100x100')

    def __str__(self):
        return '%s %s' % ( self.coleccion,  self.nombre_articulo)
    
    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>" % self.imagen_articulo)

    class Meta:
        verbose_name_plural = "4. Tipo de Articulo "





class Prod_prenda(models.Model):
    tipo_produc = models.ForeignKey(Tipo_articulo, on_delete=models.CASCADE, null=True, blank=True)
    nombre_produc = models.CharField(max_length=100, null=True, blank=True)
    imagen_produc_01 = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='vertical')
    imagen_produc_02 = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='horizontal')
    video_produc = models.FileField(upload_to='vortice', null=True, blank=True, help_text='video')
    descripcion_produc = models.TextField(max_length=500, null=True, blank=True)
    material_produc = models.TextField(max_length=500, null=True, blank=True)
    precio = models.DecimalField(max_digits=999, decimal_places=2)
    activa_descuento = models.BooleanField (default=False, null=True, blank=True)
    precio_descuent = models.DecimalField(max_digits=999, decimal_places=2, null=True, blank=True)



    def __str__(self):
        return '%s %s' % ( self.tipo_produc,  self.nombre_produc)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>" % self.imagen_produc_01)
    
    class Meta:
        verbose_name_plural = "5. Producto "

   

class Colores(models.Model):
    color = models.CharField(max_length=10,null=True, blank=True)
    codigo = models.CharField(max_length=10,null=True, blank=True)

    def __str__(self):
        return '%s %s' % ( self.color,  self.codigo)


    class Meta:
        verbose_name_plural = "6. Colores"


class Produc_Color(models.Model):
    produc_prenda = models.ForeignKey(Prod_prenda, on_delete=models.CASCADE, null=True, blank=True)
    color = models.ForeignKey(Colores, on_delete=models.CASCADE, null=True, blank=True)
    imagen = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='100x100')
    def __str__(self):
        return '%s %s' % ( self.produc_prenda,  self.color)
    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>" % self.imagen)
    class Meta:
        verbose_name_plural = "7.Color de Productos"


class Nu_Talla_Cami(models.Model):
    n_talla_camisetas = models.CharField(max_length=10,null=True, blank=True)
    
    def __str__(self):
        return '%s' % (self.n_talla_camisetas)
    class Meta:
        verbose_name_plural = "8. Numero  Tallas Camisetas  "

class Nu_Talla_Zapa(models.Model):
    n_talla_zapatos = models.CharField(max_length=10,null=True, blank=True)
    
    def __str__(self):
        return '%s' % ( self.n_talla_zapatos)
    class Meta:
        verbose_name_plural = "8.1 Numero Tallas Zapatos "

class Nu_Talla_Produ(models.Model):
    n_talla_producto = models.CharField(max_length=10,null=True, blank=True)
    
    def __str__(self):
        return '%s' % (self.n_talla_producto)
    class Meta:
        verbose_name_plural = "8.2 Numero Tallas Producto "  

class Talla_Camiseta(models.Model):
    produc = models.ForeignKey(Prod_prenda, on_delete=models.CASCADE, null=True, blank=True)
    talla_camisetas = models.ForeignKey(Nu_Talla_Cami, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return '%s %s' % ( self.produc, self.talla_camisetas)
    class Meta:
        verbose_name_plural = "8.3 Eleccion de Tallas Camisetas  "

class Talla_Zapato(models.Model):
    produc = models.ForeignKey(Prod_prenda, on_delete=models.CASCADE, null=True, blank=True)
    talla_zapatos = models.ForeignKey(Nu_Talla_Zapa, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return '%s %s' % ( self.produc, self.talla_zapatos)
    class Meta:
        verbose_name_plural = "8.4 Eleccion Tallas Zapatos "

class Talla_Producto(models.Model):
    produc = models.ForeignKey(Prod_prenda, on_delete=models.CASCADE, null=True, blank=True)
    talla_producto = models.ForeignKey(Nu_Talla_Produ, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return '%s %s' % ( self.produc, self.talla_producto)
    class Meta:
        verbose_name_plural = "8.5 Eleccion Tallas Producto "

class Servicios(models.Model):
    video=models.FileField(upload_to='vortice',null=True, blank=True, help_text='video 200*200')
    imagen=models.ImageField(upload_to='vortice',null=True, blank=True, help_text='imagenes 200*200')
    servicio= models.CharField(max_length=100, null=True, blank=True)
    detalle= models.TextField(max_length=500, null=True, blank=True)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>"%self.logo_horizontal)


    class Meta:
        verbose_name_plural = "10. Servicios"


class SliderCard(models.Model):
    activo = models.BooleanField(default=False)
    titulo= models.CharField(max_length=100, null=True, blank=True)
    sub_titulo= models.CharField(max_length=100, null=True, blank=True)
    detalle= models.TextField(max_length=500, null=True, blank=True)
    imagen=models.ImageField(upload_to='vortice',null=True, blank=True, help_text='imagenes 200*200')

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>"%self.imagen)


    class Meta:
        verbose_name_plural = "11. SliderCard"


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
    imagen_1=models.ImageField(upload_to='vortice',null=True, blank=True, help_text='horizontal')
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
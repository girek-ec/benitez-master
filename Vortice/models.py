
from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe

class Seccion_Cliente(models.Model):
    seccion=models.CharField(max_length=30, null=True, blank=True)
    icono=models.FileField(upload_to='vortice/' , null=True, blank=True, help_text='cuadrada')
    imagen_vertical = models.FileField(upload_to='vortice/', null=True, blank=True, help_text='vertical')
    imagen_horizontal =models.FileField(upload_to='vortice/', null=True, blank=True,  help_text='horizontal')

    def __str__(self):
        return '%s '% (self.seccion)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>" % self.icono)

    class Meta:
        verbose_name_plural = "1. Clientes "


talla_chosse=(
    ('','') ,('S','S'),('M','M'),('L','L'),('XL','XL'),('30','30'),('31','31'),('32','32'),('33','33'),('34','34'),('35','35'),('36','36'),('37','37'),('38','38'),('39','39'),('40','40'),('41','41'),('42','42'),('43','43')
)


class Coleccion(models.Model):
    principal = models.BooleanField(default=False)
    nuevo=models.BooleanField(default=False)
    activo = models.BooleanField(default=False)
    seccion=models.ForeignKey(Seccion_Cliente, on_delete=models.CASCADE )
    tema=models.CharField(max_length=30, null=True, blank=True)
    imagen=models.FileField(upload_to='vortice/', null=True, blank=True, help_text='100x100')
    color=models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return '%s %s'% (self.seccion,self.tema)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>" % self.imagen)

    class Meta:
        verbose_name_plural = "2. Coleccion "

class Imag_prenda_articulo(models.Model):
    tipo = models.CharField(max_length=30, null=True, blank=True)
    imagen = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='100x100')

    def __str__(self):
        return '%s ' % (self.tipo)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>" % self.imagen)

    class Meta:
        verbose_name_plural = "3. Imag_prenda_articulo "

class Articulo(models.Model):
    seccion = models.ForeignKey(Seccion_Cliente, on_delete=models.CASCADE, null=True, blank=True)
    tipo=models.ForeignKey(Imag_prenda_articulo, on_delete=models.CASCADE, null=True, blank=True)




    def __str__(self):
        return '%s %s' % ( self.seccion,  self.tipo)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>" % self.tipo.imagen)



    class Meta:
        verbose_name_plural = "4. Articulo "



class Prenda(models.Model):
    principal_visible = models.BooleanField(default=False)
    articulo= models.ForeignKey(Articulo, on_delete=models.CASCADE, null=True, blank=True)
    coleccion = models.ForeignKey(Coleccion, on_delete=models.CASCADE, null=True, blank=True)
    tipo=models.ForeignKey(Imag_prenda_articulo, on_delete=models.CASCADE, null=True, blank=True)




    def __str__(self):
        return '%s %s' % ( self.coleccion,  self.tipo)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>" % self.tipo.imagen)



    class Meta:
        verbose_name_plural = "5. Prenda "









class Slider(models.Model):
    orden=models.IntegerField()
    imagen=models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='imagenes 500*900')

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 200px'>"%self.imagen)


    class Meta:
        verbose_name_plural = "2. Slider"


class Muestra_productos(models.Model):
    estado = models.BooleanField(default=False)
    titulo = models.CharField(max_length=100, null=True, blank=True)
    imagen_1 = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='imagenes 504*250')
    titulo_1 = models.CharField(max_length=100, null=True, blank=True)
    sub_titulo_1 = models.CharField(max_length=100, null=True, blank=True)
    link_1 = models.CharField(max_length=100, null=True, blank=True)
    imagen_2 = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='imagenes 250*250')
    titulo_2 = models.CharField(max_length=100, null=True, blank=True)
    sub_titulo_2 = models.CharField(max_length=100, null=True, blank=True)
    link_2 = models.CharField(max_length=100, null=True, blank=True)
    imagen_3 = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='imagenes 250*250')
    titulo_3 = models.CharField(max_length=100, null=True, blank=True)
    sub_titulo_3 = models.CharField(max_length=100, null=True, blank=True)
    link_3 = models.CharField(max_length=100, null=True, blank=True)
    imagen_4 = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='imagenes 504*250')
    titulo_4 = models.CharField(max_length=100, null=True, blank=True)
    sub_titulo_4 = models.CharField(max_length=100, null=True, blank=True)
    link_4 = models.CharField(max_length=100, null=True, blank=True)
    imagen_5 = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='imagenes 504*500')
    titulo_5 = models.CharField(max_length=100, null=True, blank=True)
    sub_titulo_5= models.CharField(max_length=100, null=True, blank=True)
    link_5 = models.CharField(max_length=100, null=True, blank=True)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 200px'>"%self.imagen_1)


    class Meta:
        verbose_name_plural = "3. Galeria productos Imagenes"


class Vortice(models.Model):
    favicon_amarillo=models.ImageField(upload_to='vortice/', help_text='imagenes 20*20', null=True, blank=True)
    favicon_negro = models.ImageField(upload_to='vortice/', help_text='imagenes 20*20', null=True, blank=True)
    logo_horizontal = models.ImageField(upload_to='vortice/',null=True, blank=True, help_text='imagenes 20*20')
    logo_amarillo = models.ImageField(upload_to='vortice/', help_text='imagenes 20*20', null=True, blank=True)
    logo_negro = models.ImageField(upload_to='vortice/', help_text='imagenes 20*20', null=True, blank=True)
    representante = models.CharField(max_length=100, null=True, blank=True)
    whatsapp = models.CharField(max_length=11, null=True, blank=True)
    celular = models.CharField(max_length=11, null=True, blank=True)
    celular2 = models.CharField(max_length=100, null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    titulo = models.CharField(max_length=100, null=True, blank=True)
    nosotros=models.TextField(max_length=500, null=True, blank=True)
    imagen = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='imagenes 20*20')
    imagen_encabezado = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='imagenes 500*400')
    imagen_fondo = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='imagenes 20*20')
    imagen_suscri = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='imagenes 20*20')
    imagen_pie = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='imagenes 20*20')
    imagen_flot_iz_1 = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='imagenes 50*50')
    imagen_flot_iz_2 = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='imagenes 50*50')
    imagen_flot_de_1 = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='imagenes 50*50')
    imagen_flot_de_2 = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='imagenes 50*50')
    wallpaper = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='imagenes 500*400')


    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>"%self.logo_horizontal)


    class Meta:
        verbose_name_plural = "1. Vortice"

class Vorti_Promo(models.Model):
    activo = models.BooleanField(default=False)
    titulo = models.CharField(max_length=100, null=True, blank=True)
    sub_titulo = models.CharField(max_length=100, null=True, blank=True)
    imagen = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='imagenes 50*50')
    enlace= models.CharField(max_length=100, null=True, blank=True)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>"%self.imagen)


    class Meta:
        verbose_name_plural = "9. Promo Vortice"



class Contacto_redes(models.Model):
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)
    ticktock = models.CharField(max_length=100, null=True, blank=True)
    behance = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "8. Contácto Redes Sociales"












class Camiseta_Imagen_detalle(models.Model):
    imagen_cuello_o = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='500x500')
    detalle_cuello_o = models.CharField(max_length=100, null=True, blank=True)
    imagen_cuello_v_hombre = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='500x500')
    detalle_cuello_v_hombre = models.CharField(max_length=100, null=True, blank=True)
    imagen_cuello_v_mujer = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='500x500')
    detalle_cuello_v_mujer = models.CharField(max_length=100, null=True, blank=True)



    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>"%self.imagen_cuello_o)


    class Meta:
        verbose_name_plural = "3. Camiseta_Imagen_detalle "




class Camiseta_cuello(models.Model):
    cliente = models.ForeignKey(Seccion_Cliente, on_delete=models.CASCADE, null=True, blank=True)
    tipo = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return '%s %s' % (self.cliente,self.tipo)


    class Meta:
        verbose_name_plural = "6. Camiseta Cuello"


class Camiseta_talla_Hombre(models.Model):
    cuello_redondo = models.BooleanField(default=False)
    cuello_v = models.BooleanField(default=False)
    talla = models.CharField(max_length=2, null=True, blank=True)
    espalda = models.CharField(max_length=2, null=True, blank=True)
    ancho = models.CharField(max_length=2, null=True, blank=True)
    alto = models.CharField(max_length=2, null=True, blank=True)

    class Meta:
        verbose_name_plural = "6. Camiseta_talla_Hombre "

class Camiseta_talla_Mujer(models.Model):
    cuello_redondo = models.BooleanField(default=False)
    cuello_v = models.BooleanField(default=False)
    talla = models.CharField(max_length=2, null=True, blank=True)
    espalda = models.CharField(max_length=2, null=True, blank=True)
    ancho = models.CharField(max_length=2, null=True, blank=True)
    alto = models.CharField(max_length=2, null=True, blank=True)

    class Meta:
        verbose_name_plural = "6. Camiseta_talla_Mujer "


class Camiseta_talla_Nene(models.Model):
    cuello_redondo = models.BooleanField(default=False)
    cuello_v = models.BooleanField(default=False)
    talla = models.CharField(max_length=2, null=True, blank=True)
    espalda = models.CharField(max_length=2, null=True, blank=True)
    ancho = models.CharField(max_length=2, null=True, blank=True)
    alto = models.CharField(max_length=2, null=True, blank=True)

    class Meta:
        verbose_name_plural = "6. Camiseta talla Nene "

class Camiseta_talla_Nena(models.Model):
    cuello_redondo = models.BooleanField(default=False)
    cuello_v = models.BooleanField(default=False)
    talla = models.CharField(max_length=2, null=True, blank=True)
    espalda = models.CharField(max_length=2, null=True, blank=True)
    ancho = models.CharField(max_length=2, null=True, blank=True)
    alto = models.CharField(max_length=2, null=True, blank=True)

    class Meta:
        verbose_name_plural = "6. Camiseta talla Nena "



class Product(models.Model):
    orden = models.IntegerField(default=0)
    offer = models.BooleanField(default=False)
    new = models.BooleanField(default=False)
    stock = models.BooleanField(default=True)
    activar_camisetas = models.BooleanField(default=False)
    camiseta_cuello_o = models.BooleanField(default=False)
    camiseta_cuello_v_hombre_nene = models.BooleanField(default=False)
    camiseta_cuello_v_mujer_nena = models.BooleanField(default=False)
    camiseta_talla_hombre = models.BooleanField(default=False)
    camiseta_talla_mujer = models.BooleanField(default=False)
    camiseta_talla_nene= models.BooleanField(default=False)
    camiseta_talla_nena = models.BooleanField(default=False)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, null=True, blank=True )
    prenda= models.ForeignKey(Prenda, on_delete=models.CASCADE, null=True, blank=True )
    titulo= models.CharField(max_length=50, null=True, blank=True)
    imagen= models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='360x360')
    imagen_2= models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='360x360')
    imagen_3 = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='360x360')
    imagen_4 = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='360x360')
    youtube = models.FileField(upload_to='vortice/', null=True, blank=True, )
    T_unica = models.BooleanField(default=False)
    T_24 = models.BooleanField(default=False)
    T_26 = models.BooleanField(default=False)
    T_28 = models.BooleanField(default=False)
    T_30 = models.BooleanField(default=False)
    T_32 = models.BooleanField(default=False)
    T_34 = models.BooleanField(default=False)
    T_36 = models.BooleanField(default=False)
    T_38 = models.BooleanField(default=False)
    T_40 = models.BooleanField(default=False)
    precio= models.DecimalField(max_digits=999, decimal_places=2)
    precio_oferta= models.DecimalField(max_digits=999, decimal_places=2, null=True, blank=True)
    descripcion= models.TextField(max_length=500, null=True, blank=True)
    wallpapers = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='imagenes 500*400')
    galeria_producto_1 = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='360x360')
    galeria_producto_2 = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='360x360')
    galeria_producto_3 = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='360x360')
    galeria_producto_4 = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='360x360')
    galeria_producto_5 = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='360x360')
    galeria_producto_6 = models.ImageField(upload_to='vortice/', null=True, blank=True, help_text='360x360')
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return '%s %s' % (self.titulo,self.prenda)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>" % self.imagen)



    class Meta:
        verbose_name_plural = "1. Producto "




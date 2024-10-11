from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class Editable(models.Model):
    slider_fondo = models.ImageField(upload_to='niska/', help_text='slider', null=True, blank=True)
    slider_imagen = models.ImageField(upload_to='niska/', help_text='slider', null=True, blank=True)
    slider_titulo = models.CharField(max_length=80, null=True, blank=True)
    slider_subtitulo = models.CharField(max_length=80, null=True, blank=True)
    slider_detalle = models.TextField(max_length=500, null=True, blank=True)
    sec1_imagen = models.ImageField(upload_to='niska/', help_text='cuadrada', null=True, blank=True)
    sec1_titulo = models.CharField(max_length=80, null=True, blank=True)
    sec1_subtitulo = models.CharField(max_length=80, null=True, blank=True)
    sec1_detalle = models.TextField(max_length=500, null=True, blank=True)
    sec2_titulo = models.CharField(max_length=80, null=True, blank=True)
    sec2_subtitulo = models.CharField(max_length=80, null=True, blank=True)
    sec3_titulo = models.CharField(max_length=80, null=True, blank=True)
    sec3_subtitulo = models.CharField(max_length=80, null=True, blank=True)
    empr_imagen = models.ImageField(upload_to='niska/', help_text='cuadrada', null=True, blank=True)
    empr_titulo = models.CharField(max_length=80, null=True, blank=True)
    empr_detalle = models.TextField(max_length=500, null=True, blank=True)
    empr_imagen2 = models.ImageField(upload_to='niska/', help_text='cuadrada', null=True, blank=True)
    empr_titulo2 = models.CharField(max_length=80, null=True, blank=True)
    empr_detalle2 = models.TextField(max_length=500, null=True, blank=True)
    empr_imagen3 = models.ImageField(upload_to='niska/', help_text='cuadrada', null=True, blank=True)
    empr_titulo3 = models.CharField(max_length=80, null=True, blank=True)
    empr_detalle3 = models.TextField(max_length=500, null=True, blank=True)
    fondo_produ = models.ImageField(upload_to='niska/', help_text='horizontal', null=True, blank=True)
    publicidad = models.ImageField(upload_to='niska/', help_text='vertical', null=True, blank=True)
    contac_imagen = models.ImageField(upload_to='niska/', help_text='cuadrada', null=True, blank=True)
    contac_titulo = models.CharField(max_length=80, null=True, blank=True)
    contac_subtitulo = models.CharField(max_length=80, null=True, blank=True)
    contac_detalle = models.TextField(max_length=500, null=True, blank=True)


    class Meta:
        verbose_name_plural = "1. Editable"



class Marca(models.Model):
    favicon = models.ImageField(upload_to='niska/', help_text='imagenes 20*20', null=True, blank=True)
    logo_horizontal = models.ImageField(upload_to='niska/',null=True, blank=True, help_text='imagenes 20*20')
    logo_blanco = models.ImageField(upload_to='niska/', help_text='imagenes 20*20', null=True, blank=True)
    whatsapp = models.CharField(max_length=11, null=True, blank=True)
    celular = models.CharField(max_length=11, null=True, blank=True)
    celular2 = models.CharField(max_length=100, null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    facebook= models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    tiktok = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>"%self.logo_horizontal)


    class Meta:
        verbose_name_plural = "2. Niska"



class Clasif_producto(models.Model):
    clasificacion_producto=models.CharField(max_length=90, null=True, blank=True)

    def __str__(self):
        return self.clasificacion_producto

    class Meta:
        verbose_name_plural = "PROD- 01. Clasificación de Producto"




class Producto(models.Model):
    clasif=models.ForeignKey(Clasif_producto,on_delete=models.CASCADE)
    nombre_producto=models.CharField(max_length=100, null=True, blank=True)
    stock=models.CharField(max_length=20, default='stock', choices=(("stock", "stock"), ("no_stock", "no_stock")))
    imagen=models.ImageField(upload_to='niska/', null=True, blank=True)
    descripcion=models.TextField(max_length=500, null=True, blank=True)
    embalaje= models.CharField(max_length=100, null=True, blank=True)
    empaque= models.CharField(max_length=100, null=True, blank=True)
    sabores=models.CharField(max_length=100, null=True, blank=True)
    duracion = models.CharField(max_length=100, null=True, blank=True)
    presentaciones=models.CharField(max_length=100, null=True, blank=True)
    ingredientes=models.CharField(max_length=100, null=True, blank=True)
    precio=models.DecimalField(max_digits=5,decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nombre_producto

    def vista_previa(self):
        return mark_safe('<image width="100" height="100"  src="/media/%s">' % self.imagen)


    class Meta:
        verbose_name_plural = "PROD- 02. Producto"

class Producto_Imagen(models.Model):
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE,blank=True, null=True)
    galeria_articulo=models.ImageField(upload_to='niska/',help_text='imagen producto 800x800',null=True,blank=True)

    def __str__(self):
        return self.producto.nombre_producto

    def vista_previa(self):
        return mark_safe('<image width="200" height="200"  src="/media/%s">' % self.galeria_articulo)

    class Meta:
        verbose_name_plural='PROD- 03. Producto Imagenes'

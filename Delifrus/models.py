from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class Marca(models.Model):
    favicon = models.ImageField(upload_to='delifrus', help_text='imagenes 20*20', null=True, blank=True)
    logo_horizontal = models.ImageField(upload_to='delifrus',null=True, blank=True, help_text='imagenes 20*20')
    logo_blanco = models.ImageField(upload_to='delifrus', help_text='imagenes 20*20', null=True, blank=True)
    whatsapp = models.CharField(max_length=11, null=True, blank=True)
    celular = models.CharField(max_length=11, null=True, blank=True)
    celular2 = models.CharField(max_length=100, null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>"%self.logo_horizontal)


    class Meta:
        verbose_name_plural = "1. Delifrus"



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
    imagen=models.ImageField(upload_to='producto/', null=True, blank=True)
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
    galeria_articulo=models.ImageField(upload_to='media',help_text='imagen producto 800x800',null=True,blank=True)

    def __str__(self):
        return self.producto.nombre_producto

    def vista_previa(self):
        return mark_safe('<image width="200" height="200"  src="/media/%s">' % self.galeria_articulo)

    class Meta:
        verbose_name_plural='PROD- 03. Producto Imagenes'

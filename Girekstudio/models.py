from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class Ciudad(models.Model):
    ciudad=models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return "%s"%self.ciudad

    class Meta:
        verbose_name_plural = "PROD- 01. Ciudad"

class Proveedor(models.Model):
    proveedor=models.CharField(max_length=100, null=True, blank=True)
    logo=models.FileField(upload_to='girekstudio/', null=True, blank=True)
    detalle=models.CharField(max_length=300, null=True, blank=True)
    ciudad=models.ForeignKey(Ciudad,on_delete=models.CASCADE, null=True, blank=True)
    direccion=models.CharField(max_length=100, null=True, blank=True)
    telefono=models.CharField(max_length=100, null=True, blank=True)
    correo=models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.proveedor

    class Meta:
        verbose_name_plural = "PROD- 02. Proveedor"

class Clasif_producto(models.Model):
    clasificacion_producto=models.CharField(max_length=90, null=True, blank=True)

    def __str__(self):
        return self.clasificacion_producto

    class Meta:
        verbose_name_plural = "PROD- 03. Clasificación de Producto"




class Producto(models.Model):
    clasif=models.ForeignKey(Clasif_producto,on_delete=models.CASCADE)
    proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    nombre_producto=models.CharField(max_length=100, null=True, blank=True)
    stock=models.CharField(max_length=20, default='stock', choices=(("stock", "stock"), ("no_stock", "no_stock")))
    imagen=models.ImageField(upload_to='girekstudio/', null=True, blank=True)
    descripcion=models.TextField(max_length=500, null=True, blank=True)
    caracteristicas=models.TextField(max_length=500, null=True, blank=True)
    tamanos=models.TextField(max_length=500, null=True, blank=True)
    material=models.TextField(max_length=500, null=True, blank=True)
    precio=models.DecimalField(max_digits=5,decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nombre_producto

    def vista_previa(self):
        return mark_safe('<image width="100" height="100"  src="/media/%s">' % self.imagen)


    class Meta:
        verbose_name_plural = "PROD- 04. Producto"

class Producto_Imagen(models.Model):
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE,blank=True, null=True)
    galeria_articulo=models.ImageField(upload_to='girekstudio',help_text='imagen producto 800x800',null=True,blank=True)

    def __str__(self):
        return self.producto.nombre_producto

    def vista_previa(self):
        return mark_safe('<image width="200" height="200"  src="/media/%s">' % self.galeria_articulo)

    class Meta:
        verbose_name_plural='PROD- 05. Producto Imagenes'





class Marca(models.Model):
    favicon = models.ImageField(upload_to='girekstudio/', null=True, blank=True)
    logo=models.ImageField(upload_to='girekstudio/', null=True, blank=True)
    logo_blanco=models.ImageField(upload_to='girekstudio/', null=True, blank=True)
    logo_gris = models.ImageField(upload_to='girekstudio/', null=True, blank=True)
    logo_negro=models.ImageField(upload_to='girekstudio/', null=True, blank=True)
    imagen = models.ImageField(upload_to='girekstudio/', null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    tiktok = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)
    behance = models.CharField(max_length=100, null=True, blank=True)
    estudio = models.TextField(max_length=800, null=True, blank=True)
    mision = models.TextField(max_length=400, null=True, blank=True)
    vision = models.TextField(max_length=400, null=True, blank=True)
    correo = models.EmailField( null=True, blank=True)
    whatsapp = models.CharField(max_length=15, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    celular = models.CharField(max_length=11, null=True, blank=True)
    valor_1_titulo= models.CharField(max_length=100, null=True, blank=True)
    valor_1_detalle= models.TextField(max_length=700, null=True, blank=True)
    valor_2_titulo = models.CharField(max_length=100, null=True, blank=True)
    valor_2_detalle = models.TextField(max_length=700, null=True, blank=True)
    valor_3_titulo = models.CharField(max_length=100, null=True, blank=True)
    valor_3_detalle = models.TextField(max_length=700, null=True, blank=True)
    valor_4_titulo = models.CharField(max_length=100, null=True, blank=True)
    valor_4_detalle = models.TextField(max_length=700, null=True, blank=True)



    def vista_previa(self):
        return mark_safe('<image width="300" height="150"  src="/media/%s">' % self.logo)

    class Meta:
        verbose_name_plural = "GI- 01 Marca"




class Editables(models.Model):
    sec_1_imagen=models.FileField(upload_to='girekstudio/', null=True, blank=True)
    sec_1_titulo = models.CharField(max_length=100, null=True, blank=True)
    sec_1_detalle = models.TextField(max_length=700, null=True, blank=True)
    sec_1_sub_1_icono_1 = models.CharField(max_length=100, null=True, blank=True)
    sec_1_sub_1_titulo_1 = models.CharField(max_length=100, null=True, blank=True)
    sec_1_sub_1_detalle_1 = models.TextField(max_length=700, null=True, blank=True)
    sec_1_sub_2_icono_1 = models.CharField(max_length=100, null=True, blank=True)
    sec_1_sub_2_titulo_1 = models.CharField(max_length=100, null=True, blank=True)
    sec_1_sub_2_detalle_1 = models.TextField(max_length=700, null=True, blank=True)
    sec_1_sub_3_icono_1 = models.CharField(max_length=100, null=True, blank=True)
    sec_1_sub_3_titulo_1 = models.CharField(max_length=100, null=True, blank=True)
    sec_1_sub_3_detalle_1 = models.TextField(max_length=700, null=True, blank=True)
    sec_2_imagen = models.FileField(upload_to='girekstudio/', null=True, blank=True)
    sec_2_titulo = models.CharField(max_length=100, null=True, blank=True)
    sec_2_detalle = models.TextField(max_length=700, null=True, blank=True)
    sec_2_sub_1_icono_1 = models.CharField(max_length=100, null=True, blank=True)
    sec_2_sub_1_titulo_1 = models.CharField(max_length=100, null=True, blank=True)
    sec_2_sub_1_detalle_1 = models.TextField(max_length=700, null=True, blank=True)
    sec_2_sub_2_icono_1 = models.CharField(max_length=100, null=True, blank=True)
    sec_2_sub_2_titulo_1 = models.CharField(max_length=100, null=True, blank=True)
    sec_2_sub_2_detalle_1 = models.TextField(max_length=700, null=True, blank=True)
    sec_2_sub_3_icono_1 = models.CharField(max_length=100, null=True, blank=True)
    sec_2_sub_3_titulo_1 = models.CharField(max_length=100, null=True, blank=True)
    sec_2_sub_3_detalle_1 = models.TextField(max_length=700, null=True, blank=True)
    sec_3_titulo = models.CharField(max_length=100, null=True, blank=True)
    sec_3_detalle = models.TextField(max_length=700, null=True, blank=True)
    sec_3_sub_1_titulo_1 = models.CharField(max_length=100, null=True, blank=True)
    sec_3_sub_1_valor_1 = models.CharField(max_length=100, null=True, blank=True)
    sec_3_sub_2_titulo_1 = models.CharField(max_length=100, null=True, blank=True)
    sec_3_sub_2_valor_1 = models.CharField(max_length=100, null=True, blank=True)
    sec_3_sub_3_titulo_1 = models.CharField(max_length=100, null=True, blank=True)
    sec_3_sub_3_valor_1 = models.CharField(max_length=100, null=True, blank=True)
    sec_3_clientes = models.CharField(max_length=100, null=True, blank=True)
    sec_3_proyectos = models.CharField(max_length=100, null=True, blank=True)
    sec_3_anios_experiencia = models.CharField(max_length=100, null=True, blank=True)



    def vista_previa(self):
        return mark_safe('<image width="300" height="150"  src="/media/%s">' % self.sec_1_imagen)

    class Meta:
        verbose_name_plural = "GI- 02 Editable"

class Frase(models.Model):
    cita=models.TextField(null=True, blank=True)
    autor=models.CharField(max_length=90, null=True, blank=True)

    class Meta:
        verbose_name_plural = "GI- 03 Frases"


class Contacto_empresa(models.Model):
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    calle = models.CharField(max_length=100, null=True, blank=True)
    mapa = models.TextField(max_length=500, null=True, blank=True)
    representante = models.CharField(max_length=100, null=True, blank=True)
    correo_personal = models.CharField(max_length=100, null=True, blank=True)
    celular = models.CharField(max_length=11, null=True, blank=True)
    celular2 = models.CharField(max_length=100, null=True, blank=True)
    whatsapp = models.CharField(max_length=15, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "GI- 04 Contácto"


class Servicio(models.Model):
    orden=models.IntegerField()
    icono = models.CharField(max_length=20, null=True, blank=True)
    imagen=models.ImageField(upload_to='girekstudio/' ,null=True,blank=True)
    titulo=models.CharField(max_length=100, null=True,blank=True)
    sub_titulo = models.CharField(max_length=200, null=True, blank=True)
    descripcion=models.TextField(default="",null=True, blank=True)
    info_1_icono = models.CharField(max_length=50, null=True, blank=True)
    info_1_titulo = models.CharField(max_length=50, null=True, blank=True)
    info_1_descripcion = models.TextField(default="",null=True, blank=True)
    info_2_icono = models.CharField(max_length=50, null=True, blank=True)
    info_2_titulo = models.CharField(max_length=50, null=True, blank=True)
    info_2_descripcion = models.TextField(default="",null=True, blank=True)
    info_3_icono = models.CharField(max_length=50, null=True, blank=True)
    info_3_titulo = models.CharField(max_length=50, null=True, blank=True)
    info_3_descripcion = models.TextField(default="",null=True, blank=True)
    info_4_icono = models.CharField(max_length=50, null=True, blank=True)
    info_4_titulo = models.CharField(max_length=50, null=True, blank=True)
    info_4_descripcion = models.TextField(default="",null=True, blank=True)
    info_5_icono = models.CharField(max_length=50, null=True, blank=True)
    info_5_titulo = models.CharField(max_length=50, null=True, blank=True)
    info_5_descripcion = models.TextField(default="",null=True, blank=True)
    info_6_icono = models.CharField(max_length=50, null=True, blank=True)
    info_6_titulo = models.CharField(max_length=50, null=True, blank=True)
    info_6_descripcion = models.TextField(default="",null=True, blank=True)

    def __str__(self):

        return self.titulo

    def vista_previa(self):
        return mark_safe('<image width="150" height="150"  src="/media/%s">' % self.imagen)

    class Meta:
        verbose_name_plural = "SERV- 01 Servicios"





class Imag_Video_Servicio(models.Model):
    activo = models.BooleanField(default=False)
    servicio=models.ForeignKey(Servicio,on_delete=models.CASCADE)
    tipo_archivo = models.CharField(max_length=20, default='imagen', choices=(("imagen", "imagen"), ("video", "video")))
    archivo=models.FileField(upload_to='girekstudio/', null=True, blank=True,)


    def vista_previa(self):
        return mark_safe('<image width="150" height="150"  src="/media/%s">' % self.archivo)

    class Meta:
        verbose_name_plural = "SERV- 02 Imagenes / Video Servicios "



class Planes(models.Model):
    inicio_activo = models.BooleanField(default=False)
    activo = models.BooleanField(default=False)
    orden = models.IntegerField(default=0)
    categoria = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50, null=True, blank=True)
    precio = models.CharField(max_length=50, null=True, blank=True)
    detalle = models.TextField(null=True,blank=True)
    info_1 = models.CharField(max_length=100, null=True, blank=True)
    info_2 = models.CharField(max_length=100, null=True, blank=True)
    info_3 = models.CharField(max_length=100, null=True, blank=True)
    info_4 = models.CharField(max_length=100, null=True, blank=True)
    info_5 = models.CharField(max_length=100, null=True, blank=True)
    info_6 = models.CharField(max_length=100, null=True, blank=True)
    info_7 = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):

        return self.categoria.titulo



    class Meta:
        verbose_name_plural = "SERV- 03 Planes"





class Cliente(models.Model):
    nombre=models.CharField(max_length=90, null=True, blank=True)
    sitio=models.CharField(max_length=90, null=True, blank=True)
    logo=models.FileField(upload_to='girekstudio', null=True, blank=True)

    def __str__(self):
        return  self.nombre

    def vista_previa(self):
        return mark_safe('<image width="250" height="80"  src="/media/%s">' % self.logo)

    class Meta:
        verbose_name_plural = "PROY- 01 Clientes "




class Portafolio(models.Model):
    portafolio=models.CharField(max_length=90, null=True, blank=True)
    visualizaciones=models.IntegerField(default=1)

    def save(self, *args,**kwargs):
        self.visualizaciones+=1
        super(Portafolio,self).save(*args, **kwargs)

    def __str__(self):

        return  self.portafolio

    class Meta:
        verbose_name_plural = "PROY- 02 Tema Protafolio"

class Proyecto(models.Model):
    orden=models.IntegerField(default=0)
    portafolio=models.ForeignKey(Portafolio,on_delete=models.CASCADE)
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)
    fecha=models.DateField()
    nombreproyecto=models.CharField(max_length=120, null=True,blank=True, help_text="Texto de maximo 120 caracteres")
    detalle=models.TextField(null=True,blank=True)
    tipo_archivo=models.CharField(max_length=20,default='imagen',choices=(("imagen","imagen"),("video_vertical","video_vertical"),("video","video")))
    imagen=models.FileField(upload_to='girekstudio/',help_text='imagen producto 851x315',null=True,blank=True)
    link=models.CharField(max_length=250,null=True,blank=True)

    def __str__(self):

        return '%s %s'% (self.nombreproyecto,self.cliente)

    def vista_previa(self):
        return mark_safe('<image width="250" height="100"  src="/media/%s">' % self.imagen)

    class Meta:
        verbose_name_plural = "PROY- 03 Proyecto"


class Imagenesproyecto(models.Model):
    proyecto=models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    galeriaproyecto=models.FileField(upload_to='girekstudio/')


    def vista_previa(self):
        return mark_safe('<image width="100" height="100"  src="/media/%s">' % self.galeriaproyecto)

    class Meta:
        verbose_name_plural = "PROY- 04 Proyecto Imagenes"










class Suscripcion_Email(models.Model):
    email = models.EmailField(max_length=200)

    class Meta:
        verbose_name_plural = "9.2. Suscripción Email"
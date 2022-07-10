import uuid

from django.db import models

# Create your models here.
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.utils.safestring import mark_safe


class Slider(models.Model):
    orden=models.IntegerField()
    slider=models.FileField(upload_to='zatuar/', blank=True, null=True ,help_text='1884x529')

    def __str__(self):
        return ' %s ' % (self.slider)

    def vista_previa(self):
        return mark_safe('<image width="300" height="100"  src="/media/%s">' % self.slider)


    class Meta:
        verbose_name_plural="1. Slider"


class Zatuar_marca(models.Model):
    logo = models.FileField(upload_to='zatuar/', blank=True, null=True)
    logo_blanco = models.FileField(upload_to='zatuar/', blank=True, null=True)
    logo_negro = models.FileField(upload_to='zatuar/', blank=True, null=True)
    favicon = models.FileField(upload_to='zatuar/', blank=True, null=True)
    imagen = models.FileField(upload_to='zatuar/', blank=True, null=True, help_text='400x400')
    portada = models.FileField(upload_to='zatuar/', blank=True, null=True, help_text='1280x400')
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s" % self.portada

    def vista_previa(self):
        return mark_safe('<image width="200" height="200"  src="/media/%s">' % self.logo)

    class Meta:
        verbose_name_plural = "2. Zatuar Marca"


class Contacto_empresa(models.Model):
    direccion=models.CharField(max_length=100,null=True,blank=True)
    mapa=models.TextField(max_length=500,null=True,blank=True)
    celular=models.CharField(max_length=11,null=True,blank=True)
    celular2=models.CharField(max_length=100,null=True,blank=True)
    telefono=models.CharField(max_length=15,null=True,blank=True)
    correo=models.EmailField()
    horario=models.CharField(max_length=100, default=1, null=True, blank=True)
    horariosb=models.CharField(max_length=100, default=1, null=True, blank=True)

    class Meta:
        verbose_name_plural = "3. Contacto Empresa"


class Redes_sociales(models.Model):
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)
    class Meta:
        verbose_name_plural = "4. Redes Sociales"


class Beneficios(models.Model):
    beneficio=models.CharField( max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural="5. Zatuar Beneficios"


class Personalizaion_Poducto(models.Model):
    imagen=models.FileField(upload_to='zatuar/')
    titulo=models.CharField(max_length=30,blank=True, null=True)
    descripcion=models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return ' %s ' % (self.imagen)

    def vista_previa(self):
        return mark_safe('<image width="200" height="200"  src="/media/%s">' % self.imagen)


    class Meta:
        verbose_name_plural="6. Perzonalizacion de Productos"



class Identidad(models.Model):
    titulo=models.CharField(max_length=30,blank=True, null=True)

    def __str__(self):
        return ' %s ' % (self.titulo)

    class Meta:
        verbose_name_plural="7. Zatuar es"

class Proceso(models.Model):
    detalle=models.CharField(max_length=200,blank=True, null=True)
    img1=models.FileField(upload_to='zatuar/',blank=True, null=True)
    ti1=models.CharField(max_length=30,blank=True, null=True)
    img2=models.FileField(upload_to='zatuar/', blank=True, null=True)
    ti2=models.CharField(max_length=30, blank=True, null=True)
    img3=models.FileField(upload_to='zatuar/', blank=True, null=True)
    ti3=models.CharField(max_length=30, blank=True, null=True)
    ti4 = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return ' %s ' % (self.detalle)

    def vista_previa(self):
        return mark_safe('<image width="200" height="200"  src="/media/%s">' % self.img1)

    class Meta:
        verbose_name_plural="8. Proceso"


class Galeria_Proceso(models.Model):
    imagen=models.FileField(upload_to='zatuar/',blank=True, null=True)
    titulo=models.CharField(max_length=30,blank=True, null=True)

    def __str__(self):
        return ' %s ' % (self.titulo)

    def vista_previa(self):
        return mark_safe('<image width="200" height="200"  src="/media/%s">' % self.imagen)

    class Meta:
        verbose_name_plural="9. Galeria_Proceso"



class Detalles(models.Model):
    titulo=models.CharField(max_length=30,blank=True, null=True)
    image1 = models.FileField(upload_to='zatuar/',blank=True, null=True)
    image2 = models.FileField(upload_to='zatuar/',blank=True, null=True)
    image3 = models.FileField(upload_to='zatuar/',blank=True, null=True)

    def __str__(self):
        return ' %s ' % (self.titulo)

    def vista_previa(self):
        return mark_safe('<image width="200" height="200"  src="/media/%s">' % self.image1)

    class Meta:
        verbose_name_plural="9.1. Detalles"


class Descarga(models.Model):
    orden = models.IntegerField()
    principal= models.BooleanField(default=False)
    img=models.FileField(upload_to='zatuar/',blank=True, null=True)
    titulo=models.CharField(max_length=30,blank=True, null=True)
    archivo=models.FileField(upload_to='zatuar/',blank=True, null=True)

    def __str__(self):
        return ' %s ' % (self.titulo)

    def vista_previa(self):
        return mark_safe('<image width="200" height="200"  src="/media/%s">' % self.img)

    class Meta:
        verbose_name_plural="9.2. Descarga"



class Clasif_producto(models.Model):
    clasificacion_producto = models.CharField(max_length=90, null=True, blank=True)

    def __str__(self):
        return ' %s ' % (self.clasificacion_producto)

    class Meta:
        verbose_name_plural = "9.3. Clasificaciòn de Producto"


class Product(models.Model):
    orden = models.IntegerField(default=0)
    clasif = models.ForeignKey(Clasif_producto, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True, blank=True)
    image_a = models.FileField(upload_to='zatuar/', null=True, blank=True, help_text='100x100')
    image_b = models.FileField(upload_to='zatuar/', null=True, blank=True, help_text='100x100')
    foto_slider = models.FileField(upload_to='zatuar/', null=True, blank=True)
    descripcion = models.TextField(max_length=500, null=True, blank=True)
    caracteristicas = models.TextField(max_length=500, null=True, blank=True)
    tamanio = models.CharField(max_length=30, null=True, blank=True)
    tala_s = models.BooleanField(default=False)
    tala_m = models.BooleanField(default=False)
    tala_l = models.BooleanField(default=False)
    tala_xl = models.BooleanField(default=False)
    material = models.CharField(max_length=500, null=True, blank=True)
    textura = models.CharField(max_length=30, null=True, blank=True)
    gramaje = models.CharField(max_length=30, null=True, blank=True)
    nuevo = models.BooleanField(default=False)
    cantidad = models.IntegerField(null=True, blank=True)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    disponivilidad = models.BooleanField(default=True)
    azul = models.BooleanField(default=False)
    amarillo = models.BooleanField(default=False)
    verde = models.BooleanField(default=False)
    naranja = models.BooleanField(default=False)
    rojo = models.BooleanField(default=False)
    plomo = models.BooleanField(default=False)
    gris = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=False, blank=True, unique=True)

    def __str__(self):
        return ' %s ' % (self.title)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 200px'>" % self.image_a)

    class Meta:
        verbose_name_plural = "9.4. Producto"

def set_slug(sender, instance, *args, **kwargs):  # callback
    if instance.title and not instance.slug:
        slug = slugify(instance.title)

        while Product.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.title, str(uuid.uuid4())[:8])
            )
        instance.slug = slug
pre_save.connect(set_slug, sender=Product)






class Producto_Imagen(models.Model):
    orden = models.IntegerField(default=0)
    producto = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    galeria_articulo = models.FileField(upload_to='zatuar/', help_text='imagen producto 800x800', null=True, blank=True)

    def __str__(self):
        return ' %s ' % (self.producto)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 200px'>" % self.galeria_articulo)

    class Meta:
        verbose_name_plural = '9.5. Producto Imagenes'



class Producto_Personalizacion(models.Model):
    producto = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    imagen = models.FileField(upload_to='zatuar/')
    titulo = models.CharField(max_length=30, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    def vista_previa(self):
        if self.imagen:
            return """<a href="/media/%s"><img width="60" height="60" border="0" alt="Miniatura" src="/media/%s"/></a>""" % (
            self.imagen, self.imagen)
        else:
            return 'No hay imagen'

    vista_previa.short_description = "vista_previa"
    vista_previa.allow_tags = True

    class Meta:
        verbose_name_plural = "9.6. Producto Personalizacion"



class Producto_Slider(models.Model):
    orden = models.IntegerField()
    producto = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    slider = models.FileField(upload_to='zatuar/', blank=True, null=True, help_text='1884x529')

    def vista_previa(self):
        if self.slider:
            return """<a href="/media/%s"><img width="300" height="150" border="0" alt="Miniatura" src="/media/%s"/></a>""" % (
            self.slider, self.slider)
        else:
            return 'No hay imagen'

    vista_previa.short_description = "vista_previa"
    vista_previa.allow_tags = True

    class Meta:
        verbose_name_plural = "9.7. Slider"


class Cliente(models.Model):
    nombre_export = models.CharField(max_length=100, blank=True, null=True)
    client_logo = models.FileField(upload_to='zatuar/', blank=True, null=True, help_text='200x200')
    detalle = models.TextField(max_length=500, blank=True, null=True)
    foto = models.FileField(upload_to='zatuar/', blank=True, null=True, help_text='1280x500')
    pagweb = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return "%s" % self.nombre_export

    def vista_previa(self):
        return mark_safe('<image width="200" height="200"  src="/media/%s">' % self.client_logo)

    class Meta:
        verbose_name_plural = "01.0 Clientes"




class Galeria_Cliente(models.Model):
    cliente=models.ForeignKey(Cliente,  on_delete=models.CASCADE,null=True,blank=True)
    galeria=models.FileField(upload_to='zatuar/',blank=True, null=True, help_text='500x500')

    def vista_previa(self):
       if self.galeria:
            return """<a href="/media/%s"><img width="250" height="150" border="0" alt="Miniatura" src="/media/%s"/></a>""" % (self.galeria,self.galeria)
       else:
           return 'No hay imagen'

    vista_previa.short_description="vista_previa"
    vista_previa.allow_tags=True

    class Meta:
        verbose_name_plural="01.1 Clientes-Galeria"


class Producto_cliente(models.Model):
    client = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    imagen_producto = models.FileField(upload_to='zatuar/', blank=True, null=True, help_text='500x500')
    portada = models.FileField(upload_to='zatuar/', blank=True, null=True, help_text='600x400')

    def vista_previa(self):
        if self.imagen_producto:
            return """<a href="/media/%s"><img width="250" height="150" border="0" alt="Miniatura" src="/media/%s"/></a>""" % (
            self.imagen_producto, self.imagen_producto)
        else:
            return 'No hay imagen'

    vista_previa.short_description = "vista_previa"
    vista_previa.allow_tags = True

    class Meta:
        verbose_name_plural = "9.9.1 Mandil Cliente"
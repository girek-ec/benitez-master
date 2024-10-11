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
    imagen_2 = models.FileField(upload_to='zatuar/', blank=True, null=True, help_text='400x400')
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

class Linea_Product(models.Model):
    orden = models.IntegerField(default=0)
    linea = models.CharField(max_length=50, null=True, blank=True)
    imagen = models.FileField(upload_to='zatuar/', null=True, blank=True, help_text='100x100')

    def __str__(self):
        return ' %s ' % (self.linea)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 200px'>" % self.imagen)
    class Meta:
        verbose_name_plural = "9.3 Linea de Producto"

class Clasif_producto(models.Model):
    clasificacion_producto = models.CharField(max_length=90, null=True, blank=True)
    linea = models.ForeignKey(Linea_Product, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return ' %s %s' % (self.clasificacion_producto, self.linea)

    class Meta:
        verbose_name_plural = "9.4. Clasificaciòn de Producto"

class Ficha_Product(models.Model):
    producto = models.CharField(max_length=50, null=True, blank=True)
    ficha = models.FileField(upload_to='zatuar/', null=True, blank=True, help_text='pdf')


    def __str__(self):
        return ' %s ' % (self.producto)


    class Meta:
        verbose_name_plural = "9.5. Producto Ficha Tecnica"

class Colores(models.Model):
    nombre_color = models.CharField(max_length=30, null=True, blank=True)
    codigo_color = models.CharField(max_length=8, null=True, blank=True)


    def __str__(self):
        return ' %s ' % (self.nombre_color)

    class Meta:
        verbose_name_plural = "9.5. Color"


class Tallas(models.Model):
    talla = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return ' %s ' % (self.talla)

    class Meta:
        verbose_name_plural = "9.5. Tallas"


class Materiales(models.Model):
    material = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return ' %s ' % (self.material)

    class Meta:
        verbose_name_plural = "9.5. Materiales"

class Texturs(models.Model):
    textura = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return ' %s ' % (self.textura)

    class Meta:
        verbose_name_plural = "9.5. Texturas"


class Product(models.Model):
    clasif = models.ForeignKey(Clasif_producto, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True, blank=True)
    ficha_tecnica= models.ForeignKey(Ficha_Product,  on_delete=models.CASCADE, blank=True, null=True)
    image_a = models.FileField(upload_to='zatuar/', null=True, blank=True, help_text='100x100')
    image_b = models.FileField(upload_to='zatuar/', null=True, blank=True, help_text='100x100')
    foto_slider = models.FileField(upload_to='zatuar/', null=True, blank=True)
    descripcion = models.TextField(max_length=500, null=True, blank=True)
    tamanio = models.CharField(max_length=30, null=True, blank=True)
    material = models.ForeignKey(Materiales,  on_delete=models.CASCADE, blank=True, null=True)
    textura = models.ForeignKey(Texturs,  on_delete=models.CASCADE, blank=True, null=True)
    gramaje = models.CharField(max_length=30, null=True, blank=True)
    nuevo = models.BooleanField(default=False)
    precio = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    disponibilidad = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=False, blank=True, unique=True)

    def __str__(self):
        return ' %s ' % (self.title)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 200px'>" % self.image_a)

    class Meta:
        verbose_name_plural = "9.5. Producto"



class Tallas_Product(models.Model):
    producto= models.ForeignKey(Product,  on_delete=models.CASCADE, blank=True, null=True)
    talla = models.ForeignKey(Tallas, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return ' %s %s ' % (self.producto , self.talla)

    class Meta:
        verbose_name_plural = "9.5. Talla Producto"


class Color_Product(models.Model):
    producto= models.ForeignKey(Product,  on_delete=models.CASCADE, blank=True, null=True)
    color = models.ForeignKey(Colores, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return ' %s %s ' % (self.producto , self.color)

    class Meta:
        verbose_name_plural = "9.5. Color Producto"



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
    producto = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    galeria_articulo = models.FileField(upload_to='zatuar/', help_text='imagen producto 800x800', null=True, blank=True)

    def __str__(self):
        return ' %s ' % (self.producto)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 200px'>" % self.galeria_articulo)

    class Meta:
        verbose_name_plural = '9.6. Producto Imagenes'

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
        verbose_name_plural = "9.7. Producto Personalizacion"


class Cliente(models.Model):
    nombre_export = models.CharField(max_length=100, blank=True, null=True)
    client_logo = models.FileField(upload_to='zatuar/', blank=True, null=True, help_text='200x200')
    def __str__(self):
        return "%s" % self.nombre_export

    def vista_previa(self):
        return mark_safe('<image width="200" height="200"  src="/media/%s">' % self.client_logo)

    class Meta:
        verbose_name_plural = "01.0 Clientes"


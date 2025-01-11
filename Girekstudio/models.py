from ckeditor.fields import RichTextField
from django.contrib.admin import BooleanFieldListFilter
from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class Ciudad(models.Model):
    ciudad = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return "%s" % self.ciudad

    class Meta:
        verbose_name_plural = "PROD- 01. Ciudad"


class Proveedor(models.Model):
    proveedor = models.CharField(max_length=100, null=True, blank=True)
    logo = models.FileField(upload_to='girekstudio/', null=True, blank=True)
    detalle = models.CharField(max_length=300, null=True, blank=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=100, null=True, blank=True)
    correo = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return '%s' % (self.proveedor)

    class Meta:
        verbose_name_plural = "PROD- 02. Proveedor"


class Clasif_producto(models.Model):
    clasificacion_producto = models.CharField(max_length=90, null=True, blank=True)

    def __str__(self):
        return '%s' % (self.clasificacion_producto)

    class Meta:
        verbose_name_plural = "PROD- 03. Clasificación de Producto"


class Slider(models.Model):
    imagen = models.FileField(upload_to='girekstudio/', null=True, blank=True)
    titulo = models.CharField(max_length=90, null=True, blank=True)
    sub_titulo = models.TextField(max_length=500, null=True, blank=True)
    frase = models.CharField(max_length=90, null=True, blank=True)


def __str__(self):
    return '%s' % (self.titulo)

    def vista_previa(self):
        return mark_safe('<image width="100" height="100"  src="/media/%s">' % self.imagen)

    class Meta:
        verbose_name_plural = "INICIO- 01. Slider"


class Producto(models.Model):
    clasif = models.ForeignKey(Clasif_producto, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=100, null=True, blank=True)
    stock = models.CharField(max_length=20, default='stock', choices=(("stock", "stock"), ("no_stock", "no_stock")))
    imagen = models.ImageField(upload_to='girekstudio/', null=True, blank=True)
    descripcion = models.TextField(max_length=500, null=True, blank=True)
    caracteristicas = models.TextField(max_length=500, null=True, blank=True)
    tamanos = models.TextField(max_length=500, null=True, blank=True)
    material = models.TextField(max_length=500, null=True, blank=True)
    precio = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return '%s' % (self.nombre_producto)

    def vista_previa(self):
        return mark_safe('<image width="100" height="100"  src="/media/%s">' % self.imagen)

    class Meta:
        verbose_name_plural = "PROD- 04. Producto"


class Producto_Imagen(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=True, null=True)
    galeria_articulo = models.ImageField(upload_to='girekstudio', help_text='imagen producto 800x800', null=True,
                                         blank=True)

    def __str__(self):
        return '%s' % (self.producto)

    def vista_previa(self):
        return mark_safe('<image width="200" height="200"  src="/media/%s">' % self.galeria_articulo)

    class Meta:
        verbose_name_plural = 'PROD- 05. Producto Imagenes'


class Marca(models.Model):
    favicon = models.ImageField(upload_to='girekstudio/', null=True, blank=True)
    logo = models.ImageField(upload_to='girekstudio/', null=True, blank=True)
    logo_blanco = models.ImageField(upload_to='girekstudio/', null=True, blank=True)
    logo_gris = models.ImageField(upload_to='girekstudio/', null=True, blank=True)
    logo_negro = models.ImageField(upload_to='girekstudio/', null=True, blank=True)
    imagen = models.ImageField(upload_to='girekstudio/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "GI- 01 Marca"


class Editables(models.Model):
    sec_1_imagen_01 = models.FileField(upload_to='girekstudio/', null=True, blank=True,help_text="Encabezado slider  1149x800")
    sec_1_imagen_02 = models.FileField(upload_to='girekstudio/', null=True, blank=True,help_text="Encabezado slider 1149x800")
    sec_1_imagen_03 = models.FileField(upload_to='girekstudio/', null=True, blank=True,help_text="Encabezado slider 1149x800")
    sec_1_subsubti_01 = models.CharField(max_length=200, null=True, blank=True,help_text="Encabezado Texto Vertical")
    sec_1_titulo_01 = models.CharField(max_length=200, null=True, blank=True,help_text="Encabezado  Titulo")
    sec_1_subti_01 = models.CharField(max_length=200, null=True,  blank=True,help_text="Encabezado  subtitulo")
    sec_1_imagen_1 = models.FileField(upload_to='girekstudio/', null=True, blank=True,help_text="Bajo de encabezado  imagen 421x524")
    sec_1_imagen_2 = models.FileField(upload_to='girekstudio/', null=True, blank=True,help_text="Bajo de encabezado  imagen 500x614")
    sec_1_imagen_3 = models.FileField(upload_to='girekstudio/', null=True, blank=True,help_text="Bajo de encabezado  imagen 261x313")
    sec_1_subti_1 = models.CharField(max_length=200, null=True,  blank=True,  help_text="Bajo de encabezado")
    sec_1_titulo_1 = models.CharField(max_length=200, null=True, blank=True, help_text="Bajo de encabezado")
    sec_1_detalle_1 = models.TextField(max_length=500, null=True, blank=True, help_text="Bajo de encabezado")
    frase = models.CharField(max_length=800, null=True, blank=True, help_text="Frase movimiento")
    sec_1_titulo_2 = models.CharField(max_length=200, null=True, blank=True, help_text="Bajo de servicio")
    sec_1_subti_2 = models.CharField(max_length=200, null=True,  blank=True, help_text="Bajo de servicio")
    sec_1_titulo_3 = models.CharField(max_length=200, null=True, blank=True, help_text="Opcion Titulo 1")
    sec_1_subti_3 = models.CharField(max_length=200, null=True,  blank=True, help_text="Opcion detalle 1")
    sec_1_titulo_4 = models.CharField(max_length=200, null=True, blank=True, help_text="Opcion Titulo 2")
    sec_1_subti_4 = models.CharField(max_length=200, null=True,  blank=True, help_text="Opcion detalle 2")
    sec_1_titulo_5 = models.CharField(max_length=200, null=True,  blank=True,help_text="Opcion Titulo 3")
    sec_1_subti_5 = models.CharField(max_length=200, null=True,  blank=True, help_text="Opcion detalle 3")
    sec_1_titulo_6 = models.CharField(max_length=200, null=True, blank=True,help_text="Bajo parte izq. de equipo")
    sec_1_titulo_7 = models.CharField(max_length=200, null=True, blank=True,help_text="Pie de pag izq. frase")
    sec_1_imagen_4 = models.FileField(upload_to='girekstudio/', null=True, blank=True, help_text="imagen pie de pag 1126x630")
    sec_2_subti_1 = models.CharField(max_length=200, null=True, blank=True, help_text="Agencia encabezado text verti")
    sec_2_titulo_1 = models.CharField(max_length=200, null=True, blank=True, help_text="Agencia encabezado text horiz")
    sec_2_imagen_1 = models.FileField(upload_to='girekstudio/', null=True, blank=True,help_text="Agencia encabezado imagen 1149x800")
    sec_2_imagen_rota = models.FileField(upload_to='girekstudio/', null=True, blank=True, help_text="Agencia texto rotativo")
    sec_2_imag_rota_ico= models.FileField(upload_to='girekstudio/', null=True, blank=True, help_text="Agencia texto rotativo")
    sec_2_titulo_2 = models.CharField(max_length=200, null=True, blank=True, help_text="Agencia bajo de encabezado")
    sec_2_palabra = models.CharField(max_length=200, null=True, blank=True,  help_text="Agencia bajo de encabezado palabra ")
    sec_2_detalle_2 = models.TextField(max_length=500, null=True, blank=True, help_text="Agencia a lado de imagen rotando y frase ")
    sec_2_clientes = models.CharField(max_length=200, null=True, blank=True, help_text="Numero de Clientes")
    sec_2_clientes_detalle = models.CharField(max_length=200, null=True, blank=True, help_text="Detalle Clientes")
    sec_2_proyectos = models.CharField(max_length=200, null=True, blank=True, help_text="Numero proyectos")
    sec_2_proyectos_detalle = models.CharField(max_length=200, null=True, blank=True, help_text="Detalle proyectos")
    sec_2_anios_exper = models.CharField(max_length=200, null=True, blank=True, help_text="Anios de experiencia")
    sec_2_anios_exper_detalle = models.CharField(max_length=200, null=True, blank=True, help_text="Detalle Crecimiento")
    sec_2_crecimi = models.CharField(max_length=200, null=True, blank=True, help_text="Numero porcentaje crecimiento")
    sec_2_crecimi_detalle = models.CharField(max_length=200, null=True, blank=True, help_text="Detalle crecimiento")
    sec_2_imagen_3 = models.FileField(upload_to='girekstudio/', null=True, blank=True,help_text="Bajo de encabezado  imagen 421x524")
    sec_2_imagen_4 = models.FileField(upload_to='girekstudio/', null=True, blank=True,help_text="Bajo de encabezado  imagen 500x614")
    sec_2_imagen_5 = models.FileField(upload_to='girekstudio/', null=True, blank=True,help_text="Bajo de encabezado  imagen 261x313")
    sec_2_subti_4 = models.CharField(max_length=200, null=True, blank=True,help_text="Subtitulo pequeño lado derecho")
    sec_2_titulo_4 = models.CharField(max_length=200, null=True, blank=True,help_text="Titulo grande lado derecho")
    sec_2_detalle_4 = models.TextField(max_length=500, null=True, blank=True,help_text="Detalle lado derecho")
    sec_3_subti_1 = models.CharField(max_length=200, null=True, blank=True, help_text="Servicios encabezado text verti")
    sec_3_titulo_1 = models.CharField(max_length=200, null=True, blank=True, help_text="Servicios encabezado text horiz")
    sec_3_imagen_1 = models.FileField(upload_to='girekstudio/', null=True, blank=True, help_text="Servicios encabezado imagen 1149x800")
    sec_3_imagen_rota = models.FileField(upload_to='girekstudio/', null=True, blank=True, help_text="Agencia texto rotativo")
    sec_3_imag_rota_ico= models.FileField(upload_to='girekstudio/', null=True, blank=True, help_text="Agencia texto rotativo")
    sec_3_titulo_2 = models.CharField(max_length=200, null=True, blank=True, help_text="Servicios bajo de encabezado")
    sec_3_palabra = models.CharField(max_length=200, null=True, blank=True,  help_text="Agencia bajo de encabezado palabra ")
    sec_3_subti_2 = models.CharField(max_length=200, null=True, blank=True, help_text="Servicios bajo de encabezado")
    sec_3_subti_2 = models.FileField(upload_to='girekstudio/',null=True, blank=True, help_text="Agencia texto rotativo")
    sec_4_titulo_1 = models.CharField(max_length=200, null=True, blank=True, help_text="Portafolio encabezado")
    sec_4_detalle = models.TextField(max_length=500, null=True, blank=True, help_text="Portafolio Detalle encabezado")
    sec_4_imagen = models.FileField(upload_to='girekstudio/',null=True, blank=True, help_text="Portafolio imagen encabezado")
    sec_4_imagen_rota = models.FileField(upload_to='girekstudio/', null=True, blank=True, help_text="Agencia texto rotativo")
    sec_4_imag_rota_ico = models.FileField(upload_to='girekstudio/', null=True, blank=True, help_text="Agencia texto rotativo")
    sec_5_subti_1 = models.CharField(max_length=200, null=True, blank=True, help_text="Contacto encabezado text verti")
    sec_5_titulo_1 = models.CharField(max_length=200, null=True, blank=True, help_text="Contacto encabezado text horiz")
    sec_5_imagen_1 = models.FileField(upload_to='girekstudio/', null=True, blank=True, help_text="Contacto encabezado imagen 1149x800")
    sec_5_imagen_2 = models.FileField(upload_to='girekstudio/', null=True, blank=True, help_text="Contacto encabezado imagen 1149x800")
    estudio = models.TextField(max_length=800, null=True, blank=True)
    mision = models.TextField(max_length=400, null=True, blank=True)
    vision = models.TextField(max_length=400, null=True, blank=True)

    def vista_previa(self):
        return mark_safe('<image width="300" height="150"  src="/media/%s">' % self.sec_1_imagen)

    class Meta:
        verbose_name_plural = "GI- 02 Editable pag Webs"


class Frase(models.Model):
    cita = models.TextField(null=True, blank=True)
    autor = models.CharField(max_length=90, null=True, blank=True)

    class Meta:
        verbose_name_plural = "GI- 03 Frases"


class Contacto_empresa(models.Model):
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    tiktok = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)
    #behance = models.CharField(max_length=100, null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    whatsapp = models.CharField(max_length=15, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    celular = models.CharField(max_length=11, null=True, blank=True)
    celular2 = models.CharField(max_length=100, null=True, blank=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    calle = models.CharField(max_length=100, null=True, blank=True)
    mapa = models.TextField(max_length=500, null=True, blank=True)
    representante = models.CharField(max_length=100, null=True, blank=True)
    class Meta:
        verbose_name_plural = "GI- 04 Contácto"


class Servicio(models.Model):
    orden = models.IntegerField()
    icono = models.CharField(max_length=20, null=True, blank=True)
    inicio = models.BooleanField(default=False, help_text="Para Ver en Inicio")
    img_direc = models.BooleanField(default=False, help_text="Sec Agencia img activar si numero orden es  impar ")
    white = models.BooleanField(default=False, help_text="Activar en numeros impar - tono claro en fondo")
    line = models.BooleanField(default=False, help_text="Activar en numeros par - tono gris en fondo")
    imagen_rota = models.FileField(upload_to='girekstudio/', null=True, blank=True, help_text="servicios texto rotativo")
    imag_rota_ico= models.FileField(upload_to='girekstudio/', null=True, blank=True, help_text="Agencia texto rotativo")
    titulo = models.CharField(max_length=100, null=True, blank=True)
    palabra = models.CharField(max_length=20, null=True, blank=True)
    sub_titulo = models.CharField(max_length=200, null=True, blank=True)
    descripcion = models.TextField(default="", null=True, blank=True)
    imag_serv_1 = models.ImageField(upload_to='girekstudio/', null=True, blank=True, help_text="Imagen horizontal")
    imag_serv_2 = models.ImageField(upload_to='girekstudio/', null=True, blank=True, help_text="Imagen cuadrada")
    video_link = models.CharField(max_length=500, null=True, blank=True, help_text="Pegar link video de youtube")

    def __str__(self):
        return '%s' % (self.titulo)

    def vista_previa(self):
        return mark_safe('<image width="150" height="150"  src="/media/%s">' % self.imag_serv_1)

    class Meta:
        verbose_name_plural = "SERV- 01 Servicios"


class Lista_servicio(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, null=True, blank=True)
    primera_colu = models.BooleanField(default=False, help_text="Activar para enviar a primera columna")
    Segunda_colu = models.BooleanField(default=False, help_text="Activar para enviar a segunda columna")
    lista_serv = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.servicio, self.lista_serv)

    class Meta:
        verbose_name_plural = "SERV- 01.1 Servicios Lista"


class Imag_Video_Servicio(models.Model):
    activo = models.BooleanField(default=False)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    tipo_archivo = models.CharField(max_length=20, default='imagen', choices=(("imagen", "imagen"), ("video", "video")))
    archivo = models.FileField(upload_to='girekstudio/', null=True, blank=True, )

    def vista_previa(self):
        return mark_safe('<image width="150" height="150"  src="/media/%s">' % self.archivo)

    class Meta:
        verbose_name_plural = "SERV- 02 Imagenes / Video Servicios "

class Planes(models.Model):
    inicio_activo = models.BooleanField(default=False)
    activo = models.BooleanField(default=False)
    orden = models.IntegerField(default=0)
    categoria = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100, null=True, blank=True)
    sub_titulo = models.CharField(max_length=100, null=True, blank=True)
    precio = models.CharField(max_length=100, null=True, blank=True)
    detalle = models.TextField(null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.categoria, self.titulo)

    class Meta:
        verbose_name_plural = "SERV- 03 Planes"

class Plan_list(models.Model):
    plan_serv = models.ForeignKey(Planes, on_delete=models.CASCADE)
    orden = models.IntegerField(default=0)
    info_1 = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.plan_serv, self.info_1)

    class Meta:
        verbose_name_plural = "SERV- 03.5 Plan Lista "



class Cliente(models.Model):
    nombre = models.CharField(max_length=90, null=True, blank=True)
    sitio = models.CharField(max_length=90, null=True, blank=True)
    logo = models.FileField(upload_to='girekstudio', null=True, blank=True)

    def __str__(self):
        return '%s' % (self.nombre)

    def vista_previa(self):
        return mark_safe('<image width="250" height="80"  src="/media/%s">' % self.logo)

    class Meta:
        verbose_name_plural = "PROY- 01 Clientes "


class Portafolio(models.Model):
    portafolio = models.CharField(max_length=90, null=True, blank=True)
    visualizaciones = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        self.visualizaciones += 1
        super(Portafolio, self).save(*args, **kwargs)

    def __str__(self):
        return '%s' % (self.portafolio)

    class Meta:
        verbose_name_plural = "PROY- 02 Tema Protafolio"

class Proyecto(models.Model):
    orden = models.IntegerField(default=0)
    img_izq = models.BooleanField(default=False, help_text="imagen a la izquierda ")
    img_dere = models.BooleanField(default=False, help_text="imagen a la izquierda ")
    img_central = models.BooleanField(default=False, help_text="imagen a la izquierda ")
    portafolio = models.ForeignKey(Portafolio, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    nombreproyecto = models.CharField(max_length=120, null=True, blank=True, help_text="Texto de maximo 120 caracteres")
    detalle = models.TextField(null=True, blank=True)
    tipo_archivo = models.CharField(max_length=20, default='imagen', choices=(("imagen", "imagen"), ("video_vertical", "video_vertical"), ("video", "video")))
    tipo_imagen= models.BooleanField(default=False, help_text="Activar si es una imagen cuadrada ")
    imagen = models.FileField(upload_to='girekstudio/', help_text='imagen proyecto 851x315', null=True, blank=True)
    tipo_imagen_rectang = models.BooleanField(default=False, help_text="Activar si es una imagen rectangular ")
    imagen_rectang = models.FileField(upload_to='girekstudio/', help_text='imagen proyecto rectangular 851x315', null=True, blank=True)
    tipo_video = models.BooleanField(default=False, help_text="Activar si es un video de Youtube ")
    tipo_video_vertical = models.BooleanField(default=False, help_text="Activar si es un video Vertical de Youtube ")
    link = models.CharField(max_length=250, null=True, blank=True)
    detalle_2 = models.TextField(null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.nombreproyecto, self.cliente)

    def vista_previa(self):
        return mark_safe('<image width="250" height="100"  src="/media/%s">' % self.imagen)

    class Meta:
        verbose_name_plural = "PROY- 03 Proyecto"


class Imagenesproyecto(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    imagen_cuadra = models.BooleanField(default=False)
    imagen_rectangu = models.BooleanField(default=False)
    galeriaproyecto = models.FileField(upload_to='girekstudio/')

    def vista_previa(self):
        return mark_safe('<image width="100" height="100"  src="/media/%s">' % self.galeriaproyecto)

    class Meta:
        verbose_name_plural = "PROY- 04 Proyecto Imagenes"


class Equipo(models.Model):
    foto = models.FileField(upload_to='girekstudio', null=True, blank=True)
    foto_2 = models.FileField(upload_to='girekstudio', null=True, blank=True)
    nombre = models.CharField(max_length=90, null=True, blank=True)
    cargo = models.CharField(max_length=90, null=True, blank=True)

    def __str__(self):
        return '%s' % (self.nombre)

    def vista_previa(self):
        return mark_safe('<image width="250" height="80"  src="/media/%s">' % self.foto)

    class Meta:
        verbose_name_plural = "TEAM- 01 Equipo de trabajo "


class Sucursales(models.Model):
    ciudad = models.CharField(max_length=90, null=True, blank=True)
    direccion = models.CharField(max_length=90, null=True, blank=True)
    celular = models.CharField(max_length=90, null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.ciudad, self.direccion)

    class Meta:
        verbose_name_plural = "TEAM- 02 Sucursales "

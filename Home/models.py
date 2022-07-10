from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe



class Marca_benitez(models.Model):
    favicon = models.ImageField(upload_to='empresas', null=True, blank=True)
    logo=models.ImageField(upload_to='empresas', null=True, blank=True)
    logo_blanco=models.ImageField(upload_to='empresas/', null=True, blank=True)
    imagen = models.ImageField(upload_to='empresas', null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    tiktok = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)
    mision = models.TextField(max_length=400, null=True, blank=True)
    vision = models.TextField(max_length=400, null=True, blank=True)
    nosotros = models.TextField(max_length=800, null=True, blank=True)
    frase = models.TextField(max_length=200, null=True, blank=True)
    autor = models.CharField(max_length=15, null=True, blank=True)
    whatsapp = models.CharField(max_length=15, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    celular = models.CharField(max_length=11, null=True, blank=True)
    celular2 = models.CharField(max_length=100, null=True, blank=True)
    correo = models.EmailField()
    horario = models.CharField(max_length=100, default=1, null=True, blank=True)
    horariosb = models.CharField(max_length=100, default=1, null=True, blank=True)

    def vista_previa(self):
        return mark_safe('<image width="300" height="150"  src="/media/%s">' % self.logo)

    class Meta:
        verbose_name_plural = "1. Grupo Benitez "





class Empresas(models.Model):
    logo = models.ImageField(upload_to='empresas', null=True, blank=True)
    link = models.CharField(max_length=100, null=True, blank=True)
    nombre_marcas = models.CharField(max_length=100, null=True, blank=True)
    slider = models.ImageField(upload_to='slider_marcas', null=True, blank=True)
    def vista_previa(self):
        return mark_safe('<image width="300" height="150"  src="/media/%s">' % self.slider)

    class Meta:
        verbose_name_plural = "2. Empresas"

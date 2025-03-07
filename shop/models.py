from django.db import models
from django.utils.safestring import mark_safe


class Marca(models.Model):
    favicon = models.ImageField(upload_to='colexin/', help_text='imagenes 200*200', null=True, blank=True)
    logo_color = models.ImageField(upload_to='colexin/', help_text='imagenes 200*200', null=True, blank=True)
    logo_blanco = models.ImageField(upload_to='colexin/', help_text='imagenes 200*200', null=True, blank=True)
    whatsapp = models.CharField(max_length=11, null=True, blank=True)
    celular = models.CharField(max_length=11, null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    facebook= models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    tiktok = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>"%self.logo_color)


    class Meta:
        verbose_name_plural = "2. Colexin"

class Category(models.Model):
    icono = models.ImageField(upload_to='colexin', blank=True)
    name = models.CharField(max_length=200)


    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def miniatura(self):
        if self.icono:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.icono.url))
        return "Sin imagen"

class Product(models.Model):
    # Otros campos de tu modelo
    principal = models.BooleanField(default=False)
    slider = models.BooleanField(default=False)
    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image_1 = models.ImageField(upload_to='colexin', blank=True)
    image_2 = models.ImageField(upload_to='colexin', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name

    def miniatura(self):
        if self.image_1:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.image_1.url))
        return "Sin imagen"

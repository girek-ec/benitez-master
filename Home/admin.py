from django.contrib import admin

# Register your models here.
from Home.models import *
from benitez.snippers import Attr



@admin.register(Marca_benitez)
class EmpresasAdmin(admin.ModelAdmin):
    list_display = Attr(Marca_benitez) + ["vista_previa"]
    list_display_links = Attr(Marca_benitez)


@admin.register(Empresas)
class EmpresasAdmin(admin.ModelAdmin):
    list_display = Attr(Empresas) + ["vista_previa"]
    list_display_links = Attr(Empresas)

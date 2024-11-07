from django.contrib import admin
from .models import Archivos,Planetas

# Register your models here.
class AdministrarArchivos(admin.ModelAdmin):
    list_display=('id','titulo','created','archivo')
    search_fields=('titulo','descripcion')
    date_hierarchy ='created'
    list_filter =('created','updated')

admin.site.register(Archivos, AdministrarArchivos)

class AdministrarPlanetas(admin.ModelAdmin):
    list_display=('name','rotation_period','orbital_period','climate','terrain','archivo')
    search_fields=('name','rotation_period')
    date_hierarchy ='created'
    list_filter =('created','updated')

admin.site.register(Planetas, AdministrarPlanetas)
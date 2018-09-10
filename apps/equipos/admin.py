from django.contrib import admin
from apps.ambientes.models import *
from apps.equipos.models import *
# Register your models here.
@admin.register(Ambiente)
class ProductosAdmin(admin.ModelAdmin):
    model = Ambiente
    list_display = ('id','nombre','finalidad','capacidad',)
    list_editable = ('nombre','finalidad','capacidad',)

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    model = Equipo
    list_display = ('id','codigo_patrimonial','fecha_adquisicion','tipo_equipo',)
    list_editable = ('codigo_patrimonial','fecha_adquisicion','tipo_equipo',)

@admin.register(Infraestructura)
class InfraestructuraAdmin(admin.ModelAdmin):
    model = Infraestructura
    list_display = ('id','nombre','facultad','pisos','fecha_construccion',)
    list_editable = ('nombre','facultad','pisos','fecha_construccion',)

@admin.register(TipoEquipo)
class TipoEquipoAdmin(admin.ModelAdmin):
    model = TipoEquipo
    list_display = ('id','nombre_tecnico',)
    list_editable = ('nombre_tecnico',)
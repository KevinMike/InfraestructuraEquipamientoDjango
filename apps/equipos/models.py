from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TipoEquipo(models.Model):
    nombre_tecnico = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        db_table = 'tipo_equipo'

class Especificacion(models.Model):
    nombre_especificacion = models.CharField(max_length=45, blank=True, null=True)
    medida_especificacion = models.CharField(max_length=45, blank=True, null=True)
    class Meta:
        db_table = 'especificacion'

class EspecificacionEquipo(models.Model):
    especificacion = models.ForeignKey(Especificacion)
    tipo_equipo = models.ForeignKey(TipoEquipo)
    valor = models.CharField(max_length=45, blank=True, null=True)
    class Meta:
        db_table = 'especificacion_equipo'

class Equipo(models.Model):
    codigo_patrimonial = models.CharField(max_length=45, blank=True, null=True)
    fecha_adquisicion = models.DateField(blank=True, null=True)
    tipo_equipo = models.ForeignKey(TipoEquipo)
    class Meta:
        db_table = 'equipo'

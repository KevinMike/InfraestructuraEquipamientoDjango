from __future__ import unicode_literals

from django.db import models
from apps.ambientes.models import Ambiente
# Create your models here.
class Infraestructura(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    facultad = models.CharField(max_length=20, blank=True, null=True)
    pisos = models.IntegerField(blank=True,null=True)
    fecha_construccion = models.DateField(blank=True, null=True)
    class Meta:
        db_table = 'infraestructura'

class InfraestructuraAmbiente(models.Model):
    ambiente = models.ForeignKey(Ambiente)
    infraestructura = models.ForeignKey(Infraestructura)
    piso = models.CharField(max_length=45, blank=True, null=True)
    class Meta:
        db_table = 'infraestructura_ambiente'


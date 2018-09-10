from __future__ import unicode_literals

from django.db import models
from apps.equipos.models import Equipo

# Create your models here.

class Ambiente(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    finalidad = models.CharField(max_length=1, blank=True, null=True)
    capacidad = models.IntegerField(blank=True, null=True)
    class Meta:
        db_table = 'ambiente'

class AmbienteEquipo(models.Model):
    equipo = models.ForeignKey(Equipo)
    ambiente = models.ForeignKey(Ambiente)
    class Meta:
        db_table = 'ambiente_equipo'


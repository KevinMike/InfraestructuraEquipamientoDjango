# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Ambiente(models.Model):
    id_ambi = models.AutoField(primary_key=True)
    nombre_ambi = models.CharField(max_length=50, blank=True, null=True)
    finalidad_ambi = models.CharField(max_length=1, blank=True, null=True)
    capacidad_ambi = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ambiente'


class AmbienteEquipo(models.Model):
    equipo_id_equi = models.ForeignKey('Equipo', db_column='equipo_id_equi')
    ambiente_id_ambi = models.ForeignKey(Ambiente, db_column='ambiente_id_ambi')

    class Meta:
        managed = False
        db_table = 'ambiente_equipo'
        unique_together = (('equipo_id_equi', 'ambiente_id_ambi'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Equipo(models.Model):
    id_equi = models.IntegerField(primary_key=True)
    codigo_equi = models.CharField(max_length=45, blank=True, null=True)
    adquisicion_equi = models.DateField(blank=True, null=True)
    tipo_equipo_id_tequ = models.ForeignKey('TipoEquipo', db_column='tipo_equipo_id_tequ')

    class Meta:
        managed = False
        db_table = 'equipo'


class Especificacion(models.Model):
    id_tesp = models.ForeignKey('TipoEspecificacion', db_column='id_tesp')
    id_tequ = models.ForeignKey('TipoEquipo', db_column='id_tequ')
    valor_espe = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especificacion'
        unique_together = (('id_tesp', 'id_tequ'),)


class Infraestructura(models.Model):
    id_infr = models.AutoField(primary_key=True)
    nombre_infr = models.CharField(max_length=50, blank=True, null=True)
    facultad_infr = models.CharField(max_length=20, blank=True, null=True)
    construccion_infr = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infraestructura'


class InfraestructuraAmbiente(models.Model):
    id_ambi = models.ForeignKey(Ambiente, db_column='id_ambi')
    id_infr = models.ForeignKey(Infraestructura, db_column='id_infr')
    piso_inframbi = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infraestructura_ambiente'
        unique_together = (('id_ambi', 'id_infr'),)


class TipoEquipo(models.Model):
    id_tequ = models.AutoField(primary_key=True)
    nombre_tequ = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_equipo'


class TipoEspecificacion(models.Model):
    id_tesp = models.IntegerField(primary_key=True)
    nombre_tesp = models.CharField(max_length=45, blank=True, null=True)
    medida_tesp = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_especificacion'

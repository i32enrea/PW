from django.db import models

# Create your models here.

class Circunscripcion(models.Model):
    nombre = models.CharField(max_length = 100)
    escanyos = models.IntegerField()
    def __unicode__(self):
        return self.nombre

class Mesa(models.Model):
    nombre = models.CharField(max_length = 100)
    circunscripcion = models.ForeignKey(Circunscripcion)
    def __unicode__(self):
        return self.nombre

class Partido(models.Model):
    nombre = models.CharField(max_length = 100, unique = True)
    escanyos = models.IntegerField(default = 0)
    votos = models.IntegerField(default = 0)
    votosCircunscripcion = models.IntegerField(default = 0)
    def __unicode__(self):
        return self.nombre

class Resultado(models.Model):
    partido = models.ForeignKey(Partido)
    mesa = models.ForeignKey(Mesa)
    votos = models.IntegerField(default = 0)
    def __unicode__(self):
        return self.partido.nombre +" - "+ self.mesa.nombre
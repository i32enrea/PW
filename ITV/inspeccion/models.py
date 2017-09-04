from django.db import models
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Coche(models.Model):
    industrial='in'
    profesional='pro'
    particular='par'
    modelo = models.CharField(max_length = 100)
    matricula = models.CharField(max_length = 100)
    bastidor = models.IntegerField()
    tipos=((industrial, 'industrial'),(profesional, 'profesional'),(particular, 'particular'))
    tipo = models.CharField(max_length=100, choices=tipos,default=particular)
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,default = User)

    def __unicode__(self):
        return self.matricula

class Centros(models.Model):
    nombre = models.CharField(max_length = 100)
    direccion = models.CharField(max_length = 100)
    telefono = models.IntegerField()

    def __unicode__(self):
        return self.nombre

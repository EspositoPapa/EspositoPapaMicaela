from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime

# Create your models here.

class Clases(models.Model):
    nombre=models.CharField(max_length=20)
    dia=models.CharField(max_length=20)
    horario=models.FloatField()

    def __str__(self):
        return f"Nombre: {self.nombre} Dia: {self.dia} Horario: {self.horario}"

class Profesores(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    estilo=models.CharField(max_length=20)
    email=models.EmailField(max_length=40)

    def __str__(self):
        return f"Nombre:{self.nombre} Apellido:{self.apellido} Estilo:{self.estilo} Email:{self.email}"
class Eventos(models.Model):
    fcomienzo=models.DateField()
    ffinal=models.DateField()
    detalle=models.CharField(max_length=70)

    def __str__(self):
        return f"Fecha Inicio: {self.fcomienzo} Fecha Conclusión: {self.ffinal} Detalle:{self.detalle}"

class Bailarines(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    curso=models.CharField(max_length=20)
    activodesde=models.DateField()
    email=models.EmailField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombre} Apellido:{self.apellido} Curso: {self.curso} Ingreso:{self.activodesde} Email:{self.email}"

class Rutas(models.Model):
    rutaclase=models.CharField(max_length=80)
    rutaprofesores=models.CharField(max_length=80)

    def __str__ (self):
        return f"Rutaclase:{self.rutaclase} RutaProfesor{self.rutaprofesores}"

class Comentarios(models.Model):
    nombre=models.CharField(max_length=40)
    fechacoment=models.DateField()
    comentario=models.CharField(max_length=600)

    def __str__(self):
        return f"Nombre:{self.nombre} Fecha:{self.fechacoment} Comentario:{self.comentario}"
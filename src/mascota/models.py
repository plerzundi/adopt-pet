# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# tabla tipo_animal
class Tipo_Animal(models.Model):
    nombre_tipo = models.CharField(max_length=30)
    detalle     = models.TextField()

    class Meta:
        ordering = ('id',)
        verbose_name ='Tipo Animal'
        verbose_name_plural = 'Tipos de animales'

    def __str__(self):
        return self.nombre_tipo

# tabla mascota
class Mascota(models.Model):
    
    PEQUENIO = 0
    MEDIANO  = 1
    GRANDE   = 2
    TAMANIO_TYPE = (
        (PEQUENIO, 'Pequeño'),
        (MEDIANO, 'Mediano'),
        (GRANDE,'Grande'),
    )

    MACHO  = 0
    HEMBRA = 1

    SEXO = (
        (MACHO,'Macho'),
        (HEMBRA,'Hembra'),
    )

    nombre_mascota = models.CharField(blank=False, max_length=30)
    imagen_mascota = models.ImageField(upload_to="img_mascota")
    fk_tipo        = models.ForeignKey(Tipo_Animal, on_delete=models.CASCADE)
    tamanio        = models.PositiveIntegerField(choices=TAMANIO_TYPE)
    edad           = models.IntegerField()
    sexo           = models.PositiveIntegerField(choices=SEXO)

    class Meta:
        ordering = ('id',)


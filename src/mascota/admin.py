# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Tipo_Animal, Mascota

@admin.register(Tipo_Animal)
class AdminTipoAnimal(admin.ModelAdmin):
    list_display = ('id','nombre_tipo','detalle',)
    list_filter  = ('nombre_tipo',)

@admin.register(Mascota)
class AdminMascota(admin.ModelAdmin):
    list_display = ('id','nombre_mascota','imagen_mascota','fk_tipo','tamanio','edad','sexo')
    list_filter = ('tamanio','sexo')
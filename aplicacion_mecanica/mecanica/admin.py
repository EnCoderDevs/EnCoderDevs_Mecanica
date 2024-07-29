from django.contrib import admin
from .models import Empleado, Cliente, Genero

# Register your models here.

admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Genero)
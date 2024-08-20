from django.contrib import admin
from .models import Empleado, Cliente, Usuario_Empleado

# Register your models here.

admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Usuario_Empleado)
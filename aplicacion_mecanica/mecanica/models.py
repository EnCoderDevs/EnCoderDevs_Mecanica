from django.db import models

# Create your models here.

class Empleado (models.Model):
    rut                 = models.CharField(primary_key=True, max_length=10)
    primer_nombre       = models.CharField(max_length=20)
    segundo_nombre      = models.CharField(max_length=20)
    apellido_paterno    = models.CharField(max_length=20)
    apellido_materno    = models.CharField(max_length=20)
    fecha_nacimiento    = models.DateField(blank=False, null=False)
    id_genero           = models.ForeignKey('Genero', on_delete=models.CASCADE, db_column='idGenero')
    telefono            = models.CharField(max_length=45)
    email               = models.EmailField(max_length=45)
    region              = models.CharField(max_length=50, blank=True, null=True)
    ciudad              = models.CharField(max_length=50, blank=True, null=True)
    direccion           = models.CharField(max_length=50, blank=True, null=True)    
    activo              = models.IntegerField()

class Cliente (models.Model):
    rut                 = models.CharField(primary_key=True, max_length=10)
    primer_nombre       = models.CharField(max_length=20)
    segundo_nombre      = models.CharField(max_length=20)
    apellido_paterno    = models.CharField(max_length=20)
    apellido_materno    = models.CharField(max_length=20)
    fecha_nacimiento    = models.DateField(blank=False, null=False)
    id_genero           = models.ForeignKey('Genero', on_delete=models.CASCADE, db_column='idGenero')
    telefono            = models.CharField(max_length=45)
    email               = models.EmailField(max_length=45)
    region              = models.CharField(max_length=50, blank=True, null=True)
    ciudad              = models.CharField(max_length=50, blank=True, null=True)
    direccion           = models.CharField(max_length=50, blank=True, null=True)    
    activo              = models.IntegerField()

class Genero (models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero    = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str (self.genero)   
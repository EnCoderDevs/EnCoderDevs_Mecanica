from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class Empleado (models.Model):
    rut                 = models.CharField(primary_key=True, max_length=10)
    primer_nombre       = models.CharField(max_length=20)
    segundo_nombre      = models.CharField(max_length=20)
    apellido_paterno    = models.CharField(max_length=20)
    apellido_materno    = models.CharField(max_length=20)
    fecha_nacimiento    = models.DateField(blank=False, null=False)
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
    telefono            = models.CharField(max_length=45)
    email               = models.EmailField(max_length=45)
    region              = models.CharField(max_length=50, blank=True, null=True)
    ciudad              = models.CharField(max_length=50, blank=True, null=True)
    direccion           = models.CharField(max_length=50, blank=True, null=True)    
    activo              = models.IntegerField()




class UsuarioManager(BaseUserManager):
    def crear_usuario_empleado(self, rut_empleado, username_empleado,primer_nombre_empleado, segundo_nombre_empleado, apellido_paterno_empleado, apellido_materno_empleado, fecha_nacimiento_empleado, telefono_empleado, email_empleado, region_empleado, ciudad_empleado, direccion_empleado, password=None):
        if not email_empleado:
            raise ValueError('El empleado debe tener correo electronico')

        usuario_empleado = self.model(
            rut_empleado=rut_empleado,
            username_empleado=username_empleado,
            primer_nombre_empleado=primer_nombre_empleado,
            segundo_nombre_empleado=segundo_nombre_empleado,
            apellido_paterno_empleado=apellido_paterno_empleado,
            apellido_materno_empleado=apellido_materno_empleado,
            fecha_nacimiento_empleado=fecha_nacimiento_empleado,
            telefono_empleado=telefono_empleado,
            email_empleado=self.normalize_email(email_empleado),
            region_empleado=region_empleado,
            ciudad_empleado=ciudad_empleado,
            direccion_empleado=direccion_empleado,
        )
        usuario_empleado.set_password(password)
        usuario_empleado.save()
        return usuario_empleado

    def create_superuser(self, rut_empleado, username_empleado, primer_nombre_empleado, segundo_nombre_empleado, apellido_paterno_empleado, apellido_materno_empleado, fecha_nacimiento_empleado, telefono_empleado, email_empleado, region_empleado, ciudad_empleado, direccion_empleado, password):
        usuario_empleado = self.crear_usuario_empleado(
            rut_empleado=rut_empleado,
            username_empleado=username_empleado,
            primer_nombre_empleado=primer_nombre_empleado,
            segundo_nombre_empleado=segundo_nombre_empleado,
            apellido_paterno_empleado=apellido_paterno_empleado,
            apellido_materno_empleado=apellido_materno_empleado,
            fecha_nacimiento_empleado=fecha_nacimiento_empleado,
            telefono_empleado=telefono_empleado,
            email_empleado=self.normalize_email(email_empleado),
            region_empleado=region_empleado,
            ciudad_empleado=ciudad_empleado,
            direccion_empleado=direccion_empleado,
            password=password
        )
        usuario_empleado.usuario_administrador = True
        usuario_empleado.save()
        return usuario_empleado
 
    


class Usuario_Empleado (AbstractBaseUser):
    rut_empleado        = models.CharField('rut_empleado',unique=True, max_length=10)
    username_empleado            = models.CharField('Nombre de Usuario Empleado', unique=True, max_length=100)
    primer_nombre_empleado       = models.CharField('Primer Nombre Empleado',max_length=20, blank=True, null=True)
    segundo_nombre_empleado      = models.CharField('Segundo Nombre Empleado',max_length=20, blank=True, null=True)
    apellido_paterno_empleado    = models.CharField('Apellido Paterno Empleado',max_length=20, blank=True, null=True)
    apellido_materno_empleado    = models.CharField('Apellido Materno Empleado',max_length=20, blank=True, null=True)
    fecha_nacimiento_empleado    = models.DateField( 'Fecha de Nacimiento Empleado',blank=False, null=False)
    telefono_empleado            = models.CharField('Telefono de Empleado',max_length=45, blank=True, null=True)
    email_empleado               = models.EmailField('Correo de Empleado',max_length=45, blank=True, null=True)
    region_empleado              = models.CharField('Region de Empleado',max_length=50, blank=True, null=True)
    ciudad_empleado              = models.CharField('Ciudad de Empleado',max_length=50, blank=True, null=True)
    direccion_empleado           = models.CharField('Direccion de Empleado',max_length=50, blank=True, null=True)  
    usuario_activo               = models.BooleanField(default=True)
    usuario_administrador        = models.BooleanField(default=False)
    objects                      = UsuarioManager()

    USERNAME_FIELD = 'username_empleado'
    REQUIRED_FIELDS = ['rut_empleado','primer_nombre_empleado', 'segundo_nombre_empleado', 'apellido_paterno_empleado', 'apellido_materno_empleado', 'fecha_nacimiento_empleado','telefono_empleado', 'email_empleado', 'region_empleado', 'ciudad_empleado', 'direccion_empleado']

    def __str__(self):
        return f'Usuario_Empleado{self.primer_nombre_empleado}.{self.apellido_paterno_empleado}'
    
    def has_perm (self,perm,obj = None):
        return True
    
    def has_module_perms (self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.usuario_administrador


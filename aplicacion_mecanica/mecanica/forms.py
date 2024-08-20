from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from apps.mecanica.models import Usuario_Empleado

class FormularioUsuario_Empleado(forms.ModelForm):
    """" Formulario de registro de un usuario en la base de datos

    Variables:
        - password1:    Contraseña
        - password2:    verificacion de la contraseña
    
    """
    password1 = forms.CharField(label = 'Contraseña', widget= forms.PasswordInput{
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña...',
            'id': 'password1',
            'required':'required',
        }
    })

    password2 = forms.CharField(label = 'Contraseña de confirmacion', widget= forms.PasswordInput{
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese nuevamente su contraseña...',
            'id': 'password2',
            'required':'required',
        }
    })

    class Meta:
        model = Usuario_Empleado
        fields = ('rut_empleado','primer_nombre_empleado', 'segundo_nombre_empleado', 'apellido_paterno_empleado', 'apellido_materno_empleado', 'fecha_nacimiento_empleado','telefono_empleado', 'email_empleado', 'region_empleado', 'ciudad_empleado', 'direccion_empleado')    
        widgets = {
            'rut_empleado': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Rut',
                }
            ),
        'primer_nombre_empleado': forms.TextInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Ingrese su primer nombre'
            }
        ),
        'segundo_nombre_emleado': forms.TextInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Ingrese su segundo nombre'
            }            
        ),
        'apellido_paterno_empleado': forms.TextInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Ingrese su apellido paterno'
            }            
        ),
        'apellido_materno_empleado': forms.TextInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Ingrese su apellido materno'
            }            
        ),
        'fecha_nacimiento_empleado': forms.DateInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Ingrese su fecha de nacimiento'
            }            
        ),
        'telefono_empleado': forms.TextInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Ingrese su numero de telefono'
            }            
        ),
        'email_empleado': forms.EmailInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Ingrese su correo electronico'
            }            
        ),
        'region_empleado': forms.TextInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Ingrese su region'
            }            
        ),
        'ciudad_empleado': forms.TextInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Ingrese su ciudad'
            }            
        ),
        'direccion_empleado': forms.TextInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Ingrese su direccion'
            }            
        )
        },


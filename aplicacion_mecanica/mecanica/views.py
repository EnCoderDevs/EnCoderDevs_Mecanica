from django.shortcuts import render
from .models import Empleado, Cliente, Genero

# Create your views here.

def index (request):
    empleados=Empleado.objects.all()
    context={"empleados":empleados}
    return render(request, 'mecanica/index.html', context)
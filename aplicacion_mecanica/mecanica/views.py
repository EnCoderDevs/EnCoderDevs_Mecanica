from django.shortcuts import render
from .models import Empleado, Cliente
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.



def index (request):
    empleados=Empleado.objects.all()
    context={"empleados":empleados}
    return render(request, 'mecanica/index.html', context)

def home(request):
    return render(request, 'mecanica/home.html')

def signup (request):

    if request.method == 'GET':
        return render (request, 'mecanica/signup.html', {
        'form': UserCreationForm
        })        

    else:
        if request.POST['password1'] == request.POST['password2']:

            # register user
            
            try:

                user =  User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                return HttpResponse('user created succesfully')
            
            except:
                return HttpResponse('Username already exists')
        return HttpResponse('password do not match')     




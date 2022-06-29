from django.shortcuts import render
from blogdanzaalas.models import *
from django.template import loader
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from psutil import users
from login.models import Avatar
import datetime
from blogdanzaalas.forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def registrar(request):
    if request.method == "POST":

        formreg= UserCreationForm(request.POST)
        
        if formreg.is_valid():

            formreg.save()
            return render (request, 'usercreated.html')
        else:
            return HttpResponse('usuario o contraseña no correcta. Probar nuevamente')
    else:

        form = UserCreationForm()
        return render(request, "registro.html",{'formreg':formreg})

##############################################################
####VISTA USUARIO CREADO

def usercreated(request):
    return render (request,'usercreated.html')

        
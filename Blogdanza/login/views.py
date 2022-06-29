from django.http import HttpResponse
from django.shortcuts import render
#Para el login

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from psutil import users
from login.models import Avatar

#Decorador por defecto
from django.contrib.auth.decorators import login_required



# Create your views here.
#def inicio(request):
#    return (render(request,'index.html'))
#####Imagen de ingreso
#####Aprobar ingreso si está en nuestra base de datos
def login_request (request):
    if request.method == 'POST':

        form = AuthenticationForm(request , data= request.POST)

        if form.is_valid():
            
            usuario= form.cleaned_data.get("username")
            contrasena= form.cleaned_data.get("password")

            user= authenticate(username=usuario,password=contrasena)

            if user is not None:
                login(request,user)
                avatares= Avatar.objects.filter(user= request.user.id)
                if avatares is not None:
                    return render(request, 'index.html', {'url': avatares[0].imagen.url})
                else:
                    url='/media/avatar/indef.JPG'
                    return render(request, 'index.html',{'url'})
            else:
                return HttpResponse('Usted no está en nuestra base de datos')
        else:
            return render(request,'registro.html')
    form = AuthenticationForm()

    return render(request, "login.html",{'form':form})
##### 
def avatar(user):
    avatares = Avatar.objects.filter(user=user)
    if avatares.exists():
        # Se usa first() para obtener el primer objeto
        if avatares.first().imagen:
            return avatares.first().imagen.url
        else:
            # Existe el avatar pero no tiene imagen
            return None

    # Si no existe el avatar regresar un None
    return None







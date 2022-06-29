from django.http import HttpResponse
from django.shortcuts import render

from perfiles.forms import modifuser
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def modif_perfil (request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = modifuser(request.POST)

        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            usuario.email=informacion['email']
            password = informacion['password1']
            usuario.set_password(password)
            usuario.save()

            return render (request,"inicio.html")
    
    else:
        miFormulario = modifuser(initial={'email':usuario.email})

    return render (request, "modif_perfil.html",{"miFormulario": miFormulario, "usuario":usuario})



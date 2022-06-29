from django.shortcuts import render
from blogdanzaalas.models import *
from django.template import loader
from django.http import HttpRequest, HttpResponse
import datetime
from blogdanzaalas.forms import *
from django.contrib.auth.decorators import login_required
from login.models import Avatar
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
import sqlite3
# Create your views here.
#####################################################################
####TABLA DE BASE DE DATOS (CRUD - VISTA)
##TABLA DE COMENTARIOS
def coment (request):
    coment=Comentarios.objects.all()
    bdcomentario= {"bdcomentario": coment}
    return render (request, 'menssage.html',bdcomentario)

##TABLA DE CLASES
def clases(request):
    clase = Clases.objects.all()
    bdclase={"bdclase": clase}
    return render(request,'clases.html',bdclase)

#TABLA DE PROFESORES
def profesores(request):
    profe= Profesores.objects.all()
    bdprofe={"bdprofe": profe}
    return render(request,'profesores.html',bdprofe)

#TABLA DE ESTUDIANTES/BAILARINES
def bailarines(request):
    bailarin= Bailarines.objects.all()
    bdbailarin={"bdbailarin": bailarin}
    return render(request,'estudiantes.html',bdbailarin)

#TABLA DE EVENTO
def eventos(request):
    evento= Eventos.objects.all()
    bdevento={"bdevento":evento}
    return render (request,'eventos.html',bdevento)

#########################################################
##VISTAS TIPO BLOG DE EVENTOS
def eventocolor(request):
    avatares= Avatar.objects.filter(user= request.user.id)

    if avatares.exists():
        return render (request, 'eventocolor.html',{'url': avatares[0].imagen.url})
    else:
        url='/media/avatares/indef.JPG'
        return render (request, 'eventocolor.html',{'url': url})

def eventomuestra(request):
    avatares= Avatar.objects.filter(user= request.user.id)

    if avatares.exists():
        return render (request, 'eventomuestra.html',{'url': avatares[0].imagen.url})
    else:
        url='/media/avatares/indef.JPG'
        return render (request, 'eventomuestra.html',{'url': url})

def eventosolidario(request):
    avatares= Avatar.objects.filter(user= request.user.id)

    if avatares.exists():
        return render (request, 'eventosolidario.html',{'url': avatares[0].imagen.url})
    else:
        url='/media/avatares/indef.JPG'
        return render (request, 'eventosolidario.html',{'url': url})

def altas(request):
    avatares= Avatar.objects.filter(user= request.user.id)

    if avatares.exists():
        return render (request, 'altas.html',{'url': avatares[0].imagen.url})
    else:
        url='/media/avatares/indef.JPG'
        return render (request, 'altas.html',{'url': url})

def paginas(request):
    avatares= Avatar.objects.filter(user= request.user.id)

    if avatares.exists():
        return render (request, 'pageventos.html',{'url': avatares[0].imagen.url})
    else:
        url='/media/avatares/indef.JPG'
        return render (request, 'pageventos.html',{'url': url})

def modif_perfil (request):
    avatares= Avatar.objects.filter(user= request.user.id)

    if avatares.exists():
        return render (request, 'modif_perfil.html',{'url': avatares[0].imagen.url})
    else:
        url='/media/avatares/indef.JPG'
        return render (request, 'modif_perfil.html',{'url': url})
 
## VISTA TIPO BLOG DE PROFESIONALES (UNICA VISTA)
def profesionales(request):
    avatares= Avatar.objects.filter(user= request.user.id)

    if avatares.exists():
        return render (request, 'profesionales.html',{'url': avatares[0].imagen.url})
    else:
        url='/media/avatares/indef.JPG'
        return render (request, 'profesionales.html',{'url': url})

def aboutme (request):
    return render (request, 'aboutme.html')
## VISTA DE INICIO
def inicio (request):
    avatares= Avatar.objects.filter(user= request.user.id)

    if avatares.exists():
        return render (request, 'index.html',{'url': avatares[0].imagen.url})
    else:
        url='/media/avatares/indef.JPG'
        return render (request, 'index.html',{'url': url})

#########################################################################
## FUNCIONES CONECTADAS CON FORMULARIO PARA REALIZAR EL INGRESO DE LA INFORMACION SEGUN LA CLASE
#(CRUD - CREATED)
def ingresocoment(request):
    if request.method=='POST':
        mi_formulario=formcomentario(request.POST)
        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data

            coment=Comentarios(nombre=datos['nombre'], fechacoment=datos['fechacoment'], comentario=datos['comentario'])
            coment.save() 
            texto=f"Gracias por el comentario"
            return HttpResponse(texto)
    else:
        return HttpResponse('No ha ingresado la informacion correctamente')

def ingresoevento(request):
    if request.method=='POST':

        mi_formulario = formevento(request.POST)
        if mi_formulario.is_valid():
            datos2=mi_formulario.cleaned_data

            evento=Eventos(detalle=datos2['detalle'], fcomienzo=datos2['fcomienzo'], ffinal=datos2['ffinal'])
            evento.save()
            texto=f"Un nuevo evento en Alas"
            return HttpResponse(texto)

def ingresoclases(request):
    if request.method=='POST':

        mi_formulario = formclases(request.POST)
        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data

            clase=Clases(nombre=datos['nombre'], dia=datos['dia'], horario=datos['horario'])
            clase.save()
            texto=f"Felicidades por tu nueva clase: {clase.nombre}"
            return HttpResponse(texto)

def ingresoprofesores(request):
    if request.method=='POST':

        mi_formulario = formprofesores(request.POST)
        if mi_formulario.is_valid():
            datos1=mi_formulario.cleaned_data

            profe=Profesores(nombre=datos1['nombre'], apellido=datos1['apellido'], email=datos1['email'], estilo=datos1['estilo'])    
            profe.save()
            texto=f"Certificado profe de Alas para: {profe.nombre} {profe.apellido} desempeñano la clase de: {profe.estilo}"
            return HttpResponse(texto)
    
def ingresoestudiantes(request):
    if request.method=='POST':

        mi_formulario = formestudiantes(request.POST)
        if mi_formulario.is_valid():
            datos3=mi_formulario.cleaned_data

            bailarin=Bailarines(nombre=datos3['nombre'], apellido=datos3['apellido'], email=datos3['email'], curso=datos3['curso'], activodesde=datos3['activodesde'])   
            bailarin.save()
            return HttpResponse(f"Bienvenido {bailarin.nombre} {bailarin.apellido}. Mereces lo que sueñas! Disfrutá {bailarin.curso}")

#############################################################
##FORMULARIOS CREADOS PARA SER COMPLETADOS, COMPLEMENTO DE LAS FUNCIONES DE ARRIBA
def formbailarines(request):
    return render(request,'formbailarines.html')

def formprofesore(request):
    return render (request,'formprofesores.html')

def formcursos(request):
    return render (request,'formcursos.html')

def buscar(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        bailarin = Bailarines.objects.filter(nombre__icontains= nombre)
        return render (request,"resulbusqueda.html", {"bailarin": bailarin})
    else:
        return HttpResponse("Campo vacío o inexistente")

def formingresos(request):
    return render (request,"formingreso.html")

def formeventos(request):
    return render (request,'formeventos.html')

################################################################
##MODULO DE ELIMINACION DE INFORMACION (CRUD - DELETE)
def eliminarprof(request, id):
    profesor=Profesores.objects.get(id=id)
    profesor.delete()

    profe= Profesores.objects.all()
    return render(request,'profesores.html',{"bdprofe": profe})

def eliminarcurso(request, id):
    clase=Clases.objects.get(id=id)
    clase.delete()

    clase = Clases.objects.all()
    return render(request,'clases.html',{"bdclase": clase})
def eliminarbailarin(request, id):
    bailarin=Bailarines.objects.get(id=id)
    bailarin.delete()

    bailarin = Bailarines.objects.all()
    return render(request,'estudiantes.html',{'bdbailarin': bailarin})
    
def eliminoevento(request,id):
    evento=Eventos.objects.get(id=id)
    evento.delete()

    evento= Eventos.objects.all()
    return render (request,'eventos.html',{"bdevento":evento})

############################################
##PAGINA QUE APARECERÁ EN LAS URLS NO CREADAS
def noencontrado(request):
    return render(request,'paginanoencontrada.html')

############################################
##ACTUALIZACIONES/ MODIF (CRUD - UPDATE)
def editclase(request,id):
    clase= Clases.objects.get (id=id)

    if request.method == 'POST':

        mi_formulario = formclases (request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            clase.nombre = datos['nombre']
            clase.dia = datos['dia']
            clase.horario = datos['horario']
            
            clase.save()

            return render (request, 'clases.html')
    else:
        mi_formulario = formclases(initial={'nombre': clase.nombre,'dia': clase.dia, 'horario': clase.horario})

    return render (request, 'editarcurso.html', {'mi_formulario': mi_formulario, 'clase': clase})

def editprofe(request,id):
    profe= Profesores.objects.get (id=id)

    if request.method == 'POST':

        mi_formulario = formprofesores (request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            profe.nombre = datos['nombre']
            profe.apellido= datos['apellido']
            profe.estilo= datos['estilo']
            profe.email= datos['email']
            
            profe.save()

            return render (request, 'profesores.html')
    else:
        mi_formulario = formprofesores(initial={'nombre': profe.nombre,'apellido': profe.apellido, 'estilo': profe.estilo, 'email': profe.email})

    return render (request, 'editaprofesor.html', {'mi_formulario': mi_formulario, 'profe': profe})

def editevento(request,id):
    evento= Eventos.objects.get (id=id)

    if request.method == 'POST':

        mi_formulario = formevento (request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            evento.fcomienzo = datos['fcomienzo']
            evento.ffinal= datos['ffinal']
            evento.detalle= datos['detalle']
            
            evento.save()

            return render (request, 'eventos.html')
    else:
        mi_formulario = formevento(initial={'Inicio': evento.fcomienzo, 'Fin': evento.ffinal, 'detalle': evento.detalle})

    return render (request, 'editaevento.html', {'mi_formulario': mi_formulario, 'evento':evento})

def editalumno(request, id):
    alumno= Bailarines.objects.get (id=id)

    if request.method == 'POST':

        mi_formulario = formestudiantes (request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            alumno.nombre = datos['nombre']
            alumno.apellido= datos['apellido']
            alumno.curso= datos['curso']
            alumno.email= datos['email']
            alumno.activodesde= datos['activodesde']
            
            alumno.save()

            return render (request, 'estudiantes.html')
    else:
        mi_formulario = formestudiantes (initial={'Nombre': alumno.nombre, 'Apellido': alumno.apellido,'Curso': alumno.curso, 'Email': alumno.email, 'Activo desde': alumno.activodesde})
    
    return render(request,"editaalumno.html",{'mi_formulario': mi_formulario, 'alumno': alumno})
#######################################################
def avatar(request):
    avatares = Avatar.objects.filter(user=request)
    if avatares.exists():
        # Se usa first() para obtener el primer objeto
        if avatares.first().imagen:
            return avatares.first().imagen.url
        else:
            # Existe el avatar pero no tiene imagen
            return None

    # Si no existe el avatar regresar un None
    return None
    
#########################################################
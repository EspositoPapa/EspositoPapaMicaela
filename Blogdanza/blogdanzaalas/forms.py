import datetime
from traceback import format_stack
from django import forms
from django.contrib.auth.forms import UserCreationForm

class formevento(forms.Form):
    fcomienzo=forms.DateField()
    ffinal=forms.DateField()
    detalle=forms.CharField(max_length=70)

class formclases(forms.Form):
    nombre=forms.CharField(max_length=20)
    dia=forms.CharField(max_length=20)
    horario=forms.FloatField()

class formprofesores(forms.Form):
    nombre=forms.CharField(max_length=20)
    apellido=forms.CharField(max_length=20)
    estilo=forms.CharField(max_length=20)
    email=forms.EmailField(max_length=40)

class formestudiantes(forms.Form):
    nombre=forms.CharField(max_length=20)
    apellido=forms.CharField(max_length=20)
    curso=forms.CharField(max_length=20)
    activodesde=forms.DateField()
    email=forms.EmailField(max_length=40)

class formcomentario(forms.Form):
    nombre=forms.CharField(max_length=40)
    fechacoment=forms.DateField()
    comentario=forms.CharField(max_length=600)
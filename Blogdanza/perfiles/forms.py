from traceback import format_stack
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse


class modifuser (UserCreationForm):

    email = forms.EmailField(label='Modificar')
    password1: forms.CharField(label='Contraseña', widget= forms.PasswordInput)
    password2: forms.CharField(label='Repetir contraseña', widget= forms.PasswordInput)

    class Meta:
        model = User
        fields =['email','password','password2']
        help_text = {k:"" for k in fields} 
    
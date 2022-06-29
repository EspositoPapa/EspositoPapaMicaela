from django.shortcuts import render
from blogdanzaalas.templates import *
from login.models import Avatar

def login(request):
    return render(request, 'login.html')

def inicio (request):
    return render(request,'index.html')
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('modif_perfil', views.modif_perfil, name='modif_perfil')
    # path('',,name=''),
]
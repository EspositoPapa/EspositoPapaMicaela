from django.contrib import admin
from django.urls import path, include
from.import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.login_request,name='login'),
    # path('home',views.inicio, name='inicio'),
    # path('registrar',views.registrar,name='registrar'),
    path('logout',LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('blogdanzaalas/', include('blogdanzaalas.urls')),

    # path('',,name=''),
]
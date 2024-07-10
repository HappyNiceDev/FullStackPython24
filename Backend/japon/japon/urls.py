"""
URL configuration for japon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('arquitectura/', views.arquitectura, name='arquitectura'),
    path('gastronomia/', views.gastronomia, name='gastronomia'),
    path('mitosyleyendas/', views.mitosyleyendas, name='mitosyleyendas'),
    path('paisajesyjardines/', views.paisajesyjardines, name='paisajesyjardines'),
    path('puntosturisticos/', views.puntosturisticos, name='puntosturisticos'),
    path('religion/', views.religion, name='religion'),
    path('contacto/', views.contacto, name='contacto'),


    path('cuentaconfig/', views.cuentaconfig, name='cuentaconfig'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='general/login-temp.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

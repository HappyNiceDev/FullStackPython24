from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('cuentaconfig/', views.cuentaconfig, name='cuentaconfig'),
    path('register/', views.register, name='register'),

]
from django.urls import path
from . import views

urlpatterns = [
    path('arquitectura/', views.arquitectura, name='arquitectura'),
    path('gastronomia/', views.gastronomia, name='gastronomia'),
    path('mitosyleyendas/', views.mitosyleyendas, name='mitosyleyendas'),
    path('paisajesyjardines/', views.paisajesyjardines, name='paisajesyjardines'),
    path('puntosturisticos/', views.puntosturisticos, name='puntosturisticos'),
    path('religion/', views.religion, name='religion'),
]
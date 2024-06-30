from django.shortcuts import render

# Create your views here.
def arquitectura(request):
    return render(request, 'arquitectura.html')

def gastronomia(request):
    return render(request, 'gastronomia.html')

def mitosyleyendas(request):
    return render(request, 'mitosyleyendas.html')

def paisajesyjardines(request):
    return render(request, 'paisajesyjardines.html')

def puntosturisticos(request):
    return render(request, 'puntosturisticos.html')

def religion(request):
    return render(request, 'religion.html')
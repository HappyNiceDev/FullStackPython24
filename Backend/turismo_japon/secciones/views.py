from django.shortcuts import render

# Create your views here.
def arquitectura(request):
    return render(request, 'secciones/arquitectura.html')

def gastronomia(request):
    return render(request, 'secciones/gastronomia.html')

def mitosyleyendas(request):
    return render(request, 'secciones/mitosyleyendas.html')

def paisajesyjardines(request):
    return render(request, 'secciones/paisajesyjardines.html')

def puntosturisticos(request):
    return render(request, 'secciones/puntosturisticos.html')

def religion(request):
    return render(request, 'secciones/religion.html')
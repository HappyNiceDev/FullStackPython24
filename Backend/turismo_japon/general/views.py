from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

def cuentaconfig(request):
    return render(request, 'cuenta-config.html')



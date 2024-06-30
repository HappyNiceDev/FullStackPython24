from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Contacto
# Create your views here.
def index(request):
    return render(request, 'index.html')

def contacto(request):
    #Contactos form
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        mail = request.POST.get('mail')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')
        adjunto = request.FILES.get('adjunto')  # Para manejar archivos adjuntos
        # Convertir el contenido del archivo a datos binarios
        if adjunto:
            adjunto_binario = adjunto.read()
        else:
            adjunto_binario = None
        terminos_condiciones = request.POST.get('terminos') == 'on'

        # Guardar en la base de datos
        nuevo_contacto = Contacto(nombre=nombre, apellido=apellido, telefono=telefono, mail=mail,
                                asunto=asunto, mensaje=mensaje, adjunto=adjunto_binario, terminos_condiciones=terminos_condiciones)
        nuevo_contacto.save()
    # Renderizar el formulario en caso de GET o errores
    #return render(request, 'tu_template.html')
    return render(request, 'contacto.html')

def cuentaconfig(request):
    return render(request, 'cuenta-config.html')

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Contacto
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.db import IntegrityError

# Create your views here.
def index(request):
    return render(request, 'general/index.html')

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
    return render(request, 'general/contacto.html')

def cuentaconfig(request):
    return render(request, 'general/cuenta-config.html')

def custom_login(request):
    return render(request, 'general/login.html')
#---login---
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                new_user = form.save(commit=False)
                new_user.set_password(form.cleaned_data['password'])
                new_user.save()
                login(request, new_user)
                return redirect('index')  # Redirige a la página principal o a donde desees
            except IntegrityError:
                form.add_error(None, "El nombre de usuario ya existe.")
            except Exception as e:
                form.add_error(None, "Ocurrió un error al crear el usuario. Por favor, inténtalo de nuevo.")
    else:
        form = RegisterForm()
    return render(request, 'general/login-temp.html', {'form': form})
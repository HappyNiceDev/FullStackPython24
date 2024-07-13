from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.db import IntegrityError, DatabaseError
from django.contrib.auth import login, logout, authenticate
import logging
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    return render(request, 'general/index.html')

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


def contacto(request):
    #Contactos form
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        mail = request.POST.get('email')
        asunto = request.POST.get('categoria')
        mensaje = request.POST.get('mensaje')
        adjunto = request.FILES.get('foto')  # Para manejar archivos adjuntos
        # Convertir el contenido del archivo a datos binarios
        if adjunto:
            adjunto_binario = adjunto.read()
        else:
            adjunto_binario = None
        terminos_condiciones = request.POST.get('terminos') == 'on'

        # Guardar en la base de datos
        nuevo_contacto = Contact(nombre=nombre, apellido=apellido, telefono=telefono, mail=mail,
                                asunto=asunto, mensaje=mensaje, adjunto=adjunto_binario, terminos_condiciones=terminos_condiciones)
        nuevo_contacto.save()
    # Renderizar el formulario en caso de GET o errores
    #return render(request, 'tu_template.html')
    return render(request, 'general/contacto.html')

#--------------------------------------------------------------------------------------------#
#                                 Rigitra y logea al usuario                                 #
#--------------------------------------------------------------------------------------------#
def register(request):
    if request.method == 'POST':
        form = FormRegister(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirigir a una página de inicio o cualquier otra página
    else:
        form = FormRegister()
    return render(request, 'general/register.html', {'form': form})

#--------------------------------------------------------------------------------------------#
#                                 LOGIN                                                      #
#--------------------------------------------------------------------------------------------#
#---login---
#def login(request):
#    return render(request, 'general/login.html')

def login_view(request):
    if request.method == 'POST':
        form = FormLogin(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')  # Redirigir a una página de inicio o cualquier otra página
    else:
        form = FormLogin()
    return render(request, 'general/login.html', {'form': form})

#--------------------------------------------------------------------------------------------#
#                                 LOGOUT                                                     #
#--------------------------------------------------------------------------------------------#
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirigir a la página de login u otra página

#--------------------------------------------------------------------------------------------#
#               Carga cuenta-config para cambiar datos del perfil del usuario                #
#--------------------------------------------------------------------------------------------#
@login_required
def cuentaconfig(request):
    '''
    if request.method == 'POST':
        form = InfoCuenta(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cuentaconfig')  # Redirigir a la página de perfil u otra página
    else:
        form = InfoCuenta(user = request.user.username)
    '''
    return render(request, 'general/cuenta-config.html') #, {'form': form}




'''

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                # Crear el usuario
                new_user = User.objects.create_user(username=username, password=password, email='nico@naty')

                # Autenticar al usuario y mantenerlo logueado
                login(request, new_user)

                # Redirigir a la página de configuración
                return redirect('cuentaconfig')

            except IntegrityError:
                form.add_error(None, "El nombre de usuario ya existe.")
            except DatabaseError:
                form.add_error(None, "Ocurrió un error con la base de datos. Por favor, inténtalo de nuevo.")
            except ValidationError:
                form.add_error(None, "Los datos proporcionados no son válidos. Por favor, verifica la información.")
            except Exception as e:
                form.add_error(None, "Ocurrió un error al crear el usuario. Por favor, inténtalo de nuevo.")
    else:
        form = RegisterForm()

    return render(request, 'general/register.html', {'form': form})

'''

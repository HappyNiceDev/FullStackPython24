from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Contact
from .forms import RegisterForm
from django.db import IntegrityError
from django.contrib.auth import login
import logging
from django.db import IntegrityError, DatabaseError
from django.core.exceptions import ValidationError

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    context = {}
    if request.user.is_authenticated:
        context['user'] = request.user
    return render(request, 'general/index.html', context)


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


def cuentaconfig(request):
    return render(request, 'general/cuenta-config.html')

#---login---
def login(request):
    return render(request, 'general/login-temp.html')

def logout(request):
    return render(request, 'general/logout.html')



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
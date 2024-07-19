import logging
from .models import *
from .forms import *
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.db import IntegrityError, DatabaseError
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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
        form = FormRegister(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = form.save()
            login(request, user)
            return JsonResponse({'success': True, 'mensaje': 'Gracias por registrarte ' + username})
            #return redirect('cuentaconfig')  # Redirigir a una página de inicio o cualquier otra página
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
            
    else:
        form = FormRegister()
    return render(request, 'general/register.html', {'form': form})

#--------------------------------------------------------------------------------------------#
#                                 LOGIN                                                      #
#--------------------------------------------------------------------------------------------#

def login_view(request):
    if request.method == 'POST':
        form = FormLogin(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'success': True, 'mensaje': 'Bienvenido ' + username})
                #return redirect('/')  # Redirigir a una página de inicio o cualquier otra página
    else:
        form = FormLogin()
    return render(request, 'general/login.html', {'form': form})

#--------------------------------------------------------------------------------------------#
#                                 LOGOUT                                                     #
#--------------------------------------------------------------------------------------------#
def logout_view(request):
    logout(request)
    return redirect('/')  # Redirigir a la página de login u otra página

#--------------------------------------------------------------------------------------------#
#                             Carga avatar del usuario                                       #
#--------------------------------------------------------------------------------------------#

@login_required
def upload_avatar(request):
    if request.method == 'POST':
        if 'avatar' in request.FILES:
            user_profile = UserProfile.objects.get(username=request.user)
            avatar = request.FILES.get('avatar')  
            user_profile.avatar = avatar.read() # Leer la imagen como binario
            user_profile.save()
            return JsonResponse({'success': True})

    return render(request, 'upload_avatar.html')


@login_required
def avatar_view(request):
    user_profile = UserProfile.objects.get(username=request.user)
    if user_profile.avatar:
        return HttpResponse(user_profile.avatar, content_type='image/jpeg')
    return HttpResponse(status=404)  # Imagen no encontrada


#--------------------------------------------------------------------------------------------#
#               Carga cuenta-config para cambiar datos del perfil del usuario                #
#--------------------------------------------------------------------------------------------#

@login_required
def cuentaconfig(request):
    profile, created = UserProfile.objects.get_or_create(username=request.user)

    if request.method == 'POST':
        form = FormCuentaConfig(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return FormCuentaConfig({'success': False, 'errors': form.errors})

    else:
        form = FormCuentaConfig(instance=profile)

    return render(request, 'general/cuenta-config.html', {'form': form})


#--------------------------------------------------------------------------------------------#
#                                 ELIMINAR CUENTA                                            #
#--------------------------------------------------------------------------------------------#

@login_required
def eliminar_cuenta(request):
    if request.method == 'POST':
        # Elimina la cuenta del usuario
        request.user.delete()
        return JsonResponse({'success': True})
    
    return render(request, 'app/eliminar_cuenta.html')  # Muestra un template de confirmación si queremos

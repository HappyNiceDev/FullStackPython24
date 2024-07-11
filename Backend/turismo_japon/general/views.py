from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Contact
from django.contrib.auth import login as auth_login
#>>>>from django.contrib.auth.models import User
from forms import RegisterForm
from django.db import IntegrityError
from django.contrib.auth import login


# Create your views here.

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
def custom_login(request):
    return render(request, 'general/login-temp.html')

def logout(request):
    return render(request, 'general/logout.html')

#>>>> def index(request):
#     context = {}
#     if request.user.is_authenticated:
#         context['user'] = request.user
#     return render(request, 'general/index.html', context)
#---------------------------------------------------------------------------#
#def register(request):
#    if request.method == 'POST':
#        form = RegisterForm(request.POST)
#        if form.is_valid():
#            try:
#                new_user = form.save(commit=False)
#                new_user.set_password(form.cleaned_data['password'])
#                new_user.save()
#                auth_login(request, new_user)
#                return redirect('index')
#            except IntegrityError:
#                form.add_error(None, "El nombre de usuario ya existe.")
#            except Exception as e:
#                form.add_error(None, "Ocurrió un error al crear el usuario. Por favor, inténtalo de nuevo.")
#    else:
#        form = RegisterForm()
#    return render(request, 'general/register.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                new_user = form.save(commit=False)
                new_user.set_password(form.cleaned_data['password'])
                new_user.save()
                login(request, new_user)
                return redirect('cuentaconfig')  # Redirige a la página de configuración
            except IntegrityError:
                form.add_error(None, "El nombre de usuario ya existe.")
            except Exception as e:
                form.add_error(None, "Ocurrió un error al crear el usuario. Por favor, inténtalo de nuevo.")
    else:
        form = RegisterForm()
    return render(request, 'general/register.html', {'form': form})
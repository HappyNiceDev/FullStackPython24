from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact, UserProfile
from django.contrib.auth import login
from .forms import RegisterForm, UserProfileForm, AvatarForm
from django.contrib.auth.decorators import login_required
from django.templatetags.static import static
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'general/index.html')

def cuentaconfig(request):
    return render(request, 'general/cuenta-config.html')
#---login---
def custom_login(request):
    return render(request, 'general/login-temp.html')

def logout(request):
    return render(request, 'general/logout.html')


#Vista que maneja el registro de usuarios

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()

            # Crear el perfil de usuario
            UserProfile.objects.create(user=new_user)

            login(request, new_user)
            return redirect('cuentaconfig')
    else:
        form = RegisterForm()
    
    return render(request, 'general/register.html', {'form': form})


#Vista que maneja el formulario de Contacto

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
        nuevo_contacto = Contact(nombre=nombre, apellido=apellido, telefono=telefono, mail=mail,)
        nuevo_contacto = Contact(nombre=nombre, apellido=apellido, telefono=telefono, mail=mail,
                                asunto=asunto, mensaje=mensaje, adjunto=adjunto_binario, terminos_condiciones=terminos_condiciones)
        nuevo_contacto.save()
    # Renderizar el formulario en caso de GET o errores
    #return render(request, 'tu_template.html')
    return render(request, 'general/contacto.html')


#Vista que maneja la carga de datos en Mi cuenta y la carga del Avatar

@login_required
def cuentaconfig(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # Inicializamos ambos formularios
        user_profile_form = UserProfileForm(request.POST, instance=user_profile)
        avatar_form = AvatarForm(request.POST, request.FILES, instance=user_profile)

        # Verificamos qué formulario se envió
        if 'save_profile' in request.POST and user_profile_form.is_valid():
            user_profile_form.save()
            # Redirige después de guardar
            return redirect('cuentaconfig')

        elif 'save_avatar' in request.POST and avatar_form.is_valid():
            avatar_form.save()
            # Redirige después de guardar
            return redirect('cuentaconfig')

    else:
        user_profile_form = UserProfileForm(instance=user_profile)
        avatar_form = AvatarForm(instance=user_profile)

    # Define la URL de la imagen de perfil
    profile_image_url = user_profile.avatar.url if user_profile.avatar else static('img/login.webp')

    return render(request, 'general/cuenta-config.html', {
        'user_profile_form': user_profile_form,
        'avatar_form': avatar_form,
        'profile_image_url': profile_image_url,
        'user_profile': user_profile  # Incluye el perfil del usuario
    })
    
    
#Vista que Elimina la cuenta

@login_required
def eliminar_cuenta(request):
    if request.method == 'POST':
        # Elimina la cuenta del usuario
        request.user.delete()
        messages.success(request, "Tu cuenta ha sido eliminada permanentemente.")
        return redirect('index')  # Redirige a la página de inicio o a donde desees

    return render(request, 'general/eliminar_cuenta.html')  # Muestra un template de confirmación si es necesario



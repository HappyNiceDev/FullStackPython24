'''
from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    
     # Agrega campos adicionales de Persona si es necesario

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cd['password2']
'''

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		help_texts = {k:"" for k in fields }
		

class UserForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ['email']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['telefono']


class InfoCuenta(forms.Form):
    email = forms.EmailField()
    telefono = forms.CharField(max_length=15)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        if user:
            # Si hay un usuario válido pasado como argumento,
            # establecemos el valor inicial del campo email con el email del usuario.
            user_profile = AuthUser.objects.get(username=user)
            self.fields['email'].initial = user_profile.email
            
            try:
                # Intentamos obtener el perfil de usuario relacionado con 'user'.
                user_profile = UserProfile.objects.get(telefono=user)
                self.fields['telefono'].initial = user_profile.telefono
            except UserProfile.DoesNotExist:
                # Si no hay perfil de usuario, dejamos el campo 'telefono' inicializado como vacío.
                self.fields['telefono'].initial = ''

    def save(self, user):
        # Guardamos el email actualizado del usuario.
        user.email = self.cleaned_data['email']
        user.save()

        try:
            # Intentamos obtener y actualizar el perfil de usuario.
            user_profile = UserProfile.objects.get(user=user)
            user_profile.telefono = self.cleaned_data['telefono']
            user_profile.save()
        except UserProfile.DoesNotExist:
            # Si no hay perfil de usuario, creamos uno nuevo con el telefono actualizado.
            UserProfile.objects.create(user=user, telefono=self.cleaned_data['telefono'])
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *

#--------------------------------------------------------------------------------------------#
#                                 Registra usuario nuevo                                     #
#--------------------------------------------------------------------------------------------#
class FormRegister(UserCreationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'name': 'username', 'class': 'campo', 'placeholder': 'Username'}))
	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			UserProfile.objects.get(username=username)
			raise forms.ValidationError('Este usuario ya existe. Por favor, elige otro nombre de usuario.')
		except UserProfile.DoesNotExist:
			return username
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'name': 'password1', 'class': 'campo', 'placeholder': 'Password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'name': 'password2', 'class': 'campo', 'placeholder': 'Confirm Password'}))

	class Meta:
		model = UserProfile
		fields = ['username', 'password1', 'password2']
		#help_texts = {k:"" for k in fields }

#--------------------------------------------------------------------------------------------#
#                                 Loguea un usuario ya registrado                            #    
#--------------------------------------------------------------------------------------------#
class FormLogin(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'name': 'usuario', 'class': 'campo', 'placeholder': 'Usuario'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'name': 'pw1', 'class': 'campo', 'placeholder': 'Contraseña'}))

	class Meta:
		model = UserProfile
		fields = ['username', 'password1']
		#help_texts = {k:"" for k in fields }

#--------------------------------------------------------------------------------------------#
#                                 Imprime y guarda cuenta-config                             #
#--------------------------------------------------------------------------------------------#
class FormCuentaConfig(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['username', 'fech_nac', 'pais', 'genero', 'email', 'telefono']
		widgets = {
            'username': forms.TextInput(attrs={'name': 'username', 'class': 'campo', 'placeholder': 'Username'}),
            'fech_nac': forms.DateInput(format='%Y-%m-%d', attrs={'name': 'fech_nac', 'class': 'campo', 'placeholder': 'Fecha de Nacimiento', 'type': 'date'}),
			'pais': forms.TextInput(attrs={'name': 'pais', 'class': 'campo', 'placeholder': 'País'}),
			'genero': forms.TextInput(attrs={'name': 'genero', 'class': 'campo', 'placeholder': 'Género'}),
			'email': forms.EmailInput(attrs={'name': 'email', 'class': 'campo', 'placeholder': 'Email'}),
			'telefono': forms.TextInput(attrs={'name': 'telefono', 'class': 'campo', 'placeholder': 'Teléfono'})
        }


#--------------------------------------------------------------------------------------------#
#                     Imprime y guarda avatar del perfil del usuario                         #
#--------------------------------------------------------------------------------------------#

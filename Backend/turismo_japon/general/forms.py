from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


# Form que maneja el registro de usuarios

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cd['password2']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password2 and password != password2:
            self.add_error('password2', 'Las contraseñas no coinciden.')

        return cleaned_data
    
    
# Form que maneja la carga de datos en Mi cuenta

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['usuario', 'fech_nac', 'mail', 'telefono', 'genero', 'pais']
        
        
        
# Form que maneja la carga del Avatar

class AvatarForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar']  # Solo el campo de avatar
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'accept': 'image/*', 'class': 'hidden'})
        }

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if avatar:
            return avatar 
        return None


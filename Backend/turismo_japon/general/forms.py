from django import forms
from django.contrib.auth.models import User
from .models import Persona

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

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            persona = Persona.objects.create(
                user=user,
                usuario='',  # Agrega el valor adecuado si es necesario
                mail=user.email,
                telefono=None,  # Agrega el valor adecuado si es necesario
                genero='',  # Agrega el valor adecuado si es necesario
                fech_nac=None,  # Agrega el valor adecuado si es necesario
                pais='',  # Agrega el valor adecuado si es necesario
                avatar=None  # Agrega el valor adecuado si es necesario
            )
        return user
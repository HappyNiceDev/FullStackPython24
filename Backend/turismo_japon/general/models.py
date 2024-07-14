from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    usuario = models.CharField(max_length=150, unique=True)
    mail = models.EmailField()
    telefono = models.CharField(max_length=15, blank=True, null=True)
    genero = models.CharField(max_length=10, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')])
    fech_nac = models.DateField(blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    class Meta:
        db_table = '_user_profile'
        
        
class Contact(models.Model):
    contacto_id = models.AutoField(primary_key=True)
    nombre = models.TextField(blank=True, null=True)
    apellido = models.TextField(blank=True, null=True)
    telefono = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mail = models.TextField(blank=True, null=True)
    asunto = models.TextField(blank=True, null=True)
    mensaje = models.TextField(blank=True, null=True)
    adjunto = models.BinaryField(blank=True, null=True)
    terminos_condiciones = models.BooleanField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_contact'

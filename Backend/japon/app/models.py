from django.db import models
from django.contrib.auth.models import AbstractUser

#--------------------------------------------------------------------------------------------#
#                                 Tablas propias                                             #
#--------------------------------------------------------------------------------------------#
class Contact(models.Model):
    contacto_id = models.AutoField(primary_key=True)
    nombre = models.TextField(blank=True, null=True)
    apellido = models.TextField(blank=True, null=True)
    telefono = models.BigIntegerField(blank=True, null=True)
    mail = models.TextField(blank=True, null=True)
    asunto = models.TextField(blank=True, null=True)
    mensaje = models.TextField(blank=True, null=True)
    adjunto = models.BinaryField(blank=True, null=True)
    terminos_condiciones = models.BooleanField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

#--------------------------------------------------------------------------------------------#
#                                 Models propias de Django                                   #
#--------------------------------------------------------------------------------------------#
class UserProfile(AbstractUser):
    telefono = models.BigIntegerField(blank=True, null=True)
    genero = models.TextField(blank=True, null=True)
    fech_nac = models.DateField(blank=True, null=True)
    pais = models.TextField(blank=True, null=True)
    avatar = models.BinaryField(blank=True, null=True)

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
'''
class ImgSaved(models.Model):
    user_id = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    tematic = models.TextField()
    num_img = models.IntegerField()
    imgurl = models.ForeignKey('ImgUrl', on_delete=models.CASCADE, to_field=['tematic', 'num_img'], db_constraint=False)


class ImgUrl(models.Model):
    tematic = models.TextField()
    num_img = models.IntegerField()
    url = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['tematic', 'num_img'], name='UnicaCombinacionImgUrl')
        ]
'''
#--------------------------------------------------------------------------------------------#
#                                 Models propias de Django                                   #
#--------------------------------------------------------------------------------------------#
class UserProfile(AbstractUser):
    telefono = models.BigIntegerField(blank=True, null=True)
    genero = models.TextField(blank=True, null=True)
    fech_nac = models.DateField(blank=True, null=True)
    pais = models.TextField(blank=True, null=True)
    avatar = models.BinaryField(blank=True, null=True)

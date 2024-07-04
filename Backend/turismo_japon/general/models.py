# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class BlogSaved(models.Model):
    comentario_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Persona', models.DO_NOTHING)
    destinos = models.ForeignKey('Destinos', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_saved'
        db_table_comment = 'Tabla que contendra los blog guardados por el usuario'


class Comentarios(models.Model):
    comentario = models.ForeignKey(BlogSaved, models.DO_NOTHING)
    user = models.ForeignKey('Persona', models.DO_NOTHING)
    tema = models.TextField(blank=True, null=True)
    img_tema = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comentarios'
        db_table_comment = 'Tabla de comentarios sobre las tematicas del usuario'


class Contacto(models.Model):
    contacto_id = models.AutoField(primary_key=True)
    nombre = models.TextField(blank=True, null=True)
    apellido = models.TextField(blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    mail = models.TextField(blank=True, null=True)
    asunto = models.TextField(blank=True, null=True)
    mensaje = models.TextField(blank=True, null=True)
    adjunto = models.BinaryField(blank=True, null=True)
    terminos_condiciones = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacto'


class Destinos(models.Model):
    destino_id = models.AutoField(primary_key=True)
    nombre_destino = models.TextField(blank=True, null=True)
    direccion_completa = models.TextField(blank=True, null=True)
    longitud = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    latitud = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tematica = models.TextField(blank=True, null=True)
    img_tematica = models.BinaryField(blank=True, null=True)
    peso = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'destinos'
        db_table_comment = 'Tabla que me muestra los destinos elegidos'


class Persona(models.Model):
    user_id = models.AutoField(primary_key=True)
    usuario = models.TextField(blank=True, null=True)
    mail = models.TextField(blank=True, null=True)
    telefono = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    genero = models.TextField(blank=True, null=True)
    fech_nac = models.DateField(blank=True, null=True)
    pais = models.TextField(blank=True, null=True)
    avatar = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persona'
        db_table_comment = 'Tabla que describe los datos de la persona'


class RoutesSaved(models.Model):
    ruta_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Persona, models.DO_NOTHING)
    nom_ruta = models.TextField(blank=True, null=True)
    date_creac = models.TextField(blank=True, null=True)  # This field type is a guess.
    position_dom = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'routes_saved'
        db_table_comment = 'Tabla que me indica las rutas guardadas por el usuario'

#Se comenta porque esta generando errores y no permitía migrar, no se permiten 2 autofield
# class RutasDestino(models.Model):
#    ruta_id = models.AutoField()
#    destino_id = models.AutoField()
#
#    class Meta:
#        managed = False
#        db_table = 'rutas_destino'
#        db_table_comment = 'Tabla que me muestra las rutas destino identificadas'


class Seguridad(models.Model):
    user = models.ForeignKey(Persona, models.DO_NOTHING)
    psw = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seguridad'
        db_table_comment = 'Tabla que me indica id de usuario y contrase±a'


class Sesion(models.Model):
    user = models.ForeignKey(Persona, models.DO_NOTHING)
    token = models.IntegerField(blank=True, null=True)
    pc_mac = models.TextField(blank=True, null=True)  # This field type is a guess.
    ip_public = models.GenericIPAddressField(blank=True, null=True)
    time_sesion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sesion'
        db_table_comment = 'Datos de la sesion'


class Tematic(models.Model):
    user = models.ForeignKey(Persona, models.DO_NOTHING)
    tema = models.TextField(blank=True, null=True)
    img_tema = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tematic'
        db_table_comment = 'Tematica del usuario'

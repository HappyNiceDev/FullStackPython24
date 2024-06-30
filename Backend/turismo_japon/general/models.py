# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BlogSaved(models.Model):
    coment_id = models.TextField(primary_key=True)  # This field type is a guess.
    user_id = models.IntegerField(blank=True, null=True)
    destin_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blog_saved'


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


class DataUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    usuario = models.TextField(blank=True, null=True)  # This field type is a guess.
    e_mail = models.TextField(db_column='e-mail', blank=True, null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    telefono = models.IntegerField(blank=True, null=True)
    genero = models.TextField(blank=True, null=True)  # This field type is a guess.
    fech_nac = models.IntegerField(blank=True, null=True)
    nacion_user = models.TextField(blank=True, null=True)  # This field type is a guess.
    img_user = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_user'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ImgTematic(models.Model):
    user_id = models.IntegerField()
    tematica = models.TextField(blank=True, null=True)  # This field type is a guess.
    img_tematica = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'img_tematic'


class RoutesSaved(models.Model):
    route_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    nomb_route = models.TextField(blank=True, null=True)  # This field type is a guess.
    date_create = models.IntegerField(blank=True, null=True)
    position_dom = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'routes_saved'


class SecureUser(models.Model):
    user_id = models.IntegerField()
    user_pass = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'secure_user'


class UserSesion(models.Model):
    user_id = models.IntegerField()
    token_user = models.TextField(blank=True, null=True)  # This field type is a guess.
    pc_mac = models.TextField(blank=True, null=True)  # This field type is a guess.
    ip_public = models.IntegerField(blank=True, null=True)
    hour_sesion = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_sesion'

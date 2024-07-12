# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Comments(models.Model):
    comentario_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    coment = models.TextField()
    timestamp = models.DateTimeField()
    tematic = models.TextField()
    num_img = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_comments'
        db_table_comment = 'Tabla de comentarios sobre las imagenes del totem dentro del las tematicas'


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


class Destination(models.Model):
    destination_id = models.AutoField(primary_key=True)
    name_destination = models.TextField()
    full_address = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    tematic = models.TextField()
    num_img = models.IntegerField()
    weighting = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_destination'


class RoutesDestination(models.Model):
    route = models.ForeignKey('RoutesSaved', models.DO_NOTHING)
    destination = models.ForeignKey(Destination, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = '_routes_destination'


class RoutesSaved(models.Model):
    route_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    name_route = models.TextField()
    timestamp = models.DateTimeField()
    position_dom = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_routes_saved'


class Sesion(models.Model):
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    token = models.TextField()
    pc_mac = models.TextField()  # This field type is a guess.
    ip_public = models.GenericIPAddressField()
    time_sesion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = '_sesion'
        db_table_comment = 'Datos de la sesion'


class TematicSaved(models.Model):
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    tematic = models.TextField()
    num_img = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_tematic_saved'
        db_table_comment = 'Tematica del usuario'


class UserProfile(models.Model):
    user = models.ForeignKey('AuthUser', models.CASCADE)
    telefono = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    genero = models.TextField(blank=True, null=True)
    fech_nac = models.DateField(blank=True, null=True)
    pais = models.TextField(blank=True, null=True)
    avatar = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_user_profile'
        db_table_comment = 'Tabla que describe los datos de la persona'

    def __str__(self):
        return self.user.email


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

    def __str__(self):
        return self.email


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

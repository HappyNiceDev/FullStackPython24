# Generated by Django 5.0.6 on 2024-07-09 01:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comentario_id', models.AutoField(primary_key=True, serialize=False)),
                ('coment', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('tematic', models.TextField()),
                ('num_img', models.IntegerField()),
            ],
            options={
                'db_table': '_comments',
                'db_table_comment': 'Tabla de comentarios sobre las imagenes del totem dentro del las tematicas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contacto_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField(blank=True, null=True)),
                ('apellido', models.TextField(blank=True, null=True)),
                ('telefono', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('mail', models.TextField(blank=True, null=True)),
                ('asunto', models.TextField(blank=True, null=True)),
                ('mensaje', models.TextField(blank=True, null=True)),
                ('adjunto', models.BinaryField(blank=True, null=True)),
                ('terminos_condiciones', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': '_contact',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('destination_id', models.AutoField(primary_key=True, serialize=False)),
                ('name_destination', models.TextField()),
                ('full_address', models.TextField()),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('tematic', models.TextField()),
                ('num_img', models.IntegerField()),
                ('weighting', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': '_destination',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RoutesDestination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': '_routes_destination',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TematicSaved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tematic', models.TextField()),
                ('num_img', models.IntegerField()),
            ],
            options={
                'db_table': '_tematic_saved',
                'db_table_comment': 'Tematica del usuario',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='BlogSaved',
        ),
        migrations.DeleteModel(
            name='Comentarios',
        ),
        migrations.DeleteModel(
            name='Contacto',
        ),
        migrations.DeleteModel(
            name='Destinos',
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
        migrations.DeleteModel(
            name='Seguridad',
        ),
        migrations.DeleteModel(
            name='Tematic',
        ),
        migrations.AlterModelTableComment(
            name='routessaved',
            table_comment=None,
        ),
        migrations.AlterModelTable(
            name='routessaved',
            table='_routes_saved',
        ),
        migrations.AlterModelTable(
            name='sesion',
            table='_sesion',
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='general.authuser')),
                ('usuario', models.TextField(blank=True, null=True)),
                ('mail', models.TextField(blank=True, null=True)),
                ('telefono', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('genero', models.TextField(blank=True, null=True)),
                ('fech_nac', models.DateField(blank=True, null=True)),
                ('pais', models.TextField(blank=True, null=True)),
                ('avatar', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': '_user_profile',
                'db_table_comment': 'Tabla que describe los datos de la persona',
                'managed': False,
            },
        ),
    ]

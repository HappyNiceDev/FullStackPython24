# Generated by Django 5.0.6 on 2024-07-04 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogSaved',
            fields=[
                ('comentario_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'blog_saved',
                'db_table_comment': 'Tabla que contendra los blog guardados por el usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema', models.TextField(blank=True, null=True)),
                ('img_tema', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'comentarios',
                'db_table_comment': 'Tabla de comentarios sobre las tematicas del usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('contacto_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField(blank=True, null=True)),
                ('apellido', models.TextField(blank=True, null=True)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('mail', models.TextField(blank=True, null=True)),
                ('asunto', models.TextField(blank=True, null=True)),
                ('mensaje', models.TextField(blank=True, null=True)),
                ('adjunto', models.BinaryField(blank=True, null=True)),
                ('terminos_condiciones', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'contacto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Destinos',
            fields=[
                ('destino_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_destino', models.TextField(blank=True, null=True)),
                ('direccion_completa', models.TextField(blank=True, null=True)),
                ('longitud', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('latitud', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('tematica', models.TextField(blank=True, null=True)),
                ('img_tematica', models.BinaryField(blank=True, null=True)),
                ('peso', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'destinos',
                'db_table_comment': 'Tabla que me muestra los destinos elegidos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.TextField(blank=True, null=True)),
                ('mail', models.TextField(blank=True, null=True)),
                ('telefono', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('genero', models.TextField(blank=True, null=True)),
                ('fech_nac', models.DateField(blank=True, null=True)),
                ('pais', models.TextField(blank=True, null=True)),
                ('avatar', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'persona',
                'db_table_comment': 'Tabla que describe los datos de la persona',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RoutesSaved',
            fields=[
                ('ruta_id', models.AutoField(primary_key=True, serialize=False)),
                ('nom_ruta', models.TextField(blank=True, null=True)),
                ('date_creac', models.TextField(blank=True, null=True)),
                ('position_dom', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'routes_saved',
                'db_table_comment': 'Tabla que me indica las rutas guardadas por el usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seguridad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('psw', models.CharField(blank=True, null=True)),
            ],
            options={
                'db_table': 'seguridad',
                'db_table_comment': 'Tabla que me indica id de usuario y contrase±a',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sesion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.IntegerField(blank=True, null=True)),
                ('pc_mac', models.TextField(blank=True, null=True)),
                ('ip_public', models.GenericIPAddressField(blank=True, null=True)),
                ('time_sesion', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sesion',
                'db_table_comment': 'Datos de la sesion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tematic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema', models.TextField(blank=True, null=True)),
                ('img_tema', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tematic',
                'db_table_comment': 'Tematica del usuario',
                'managed': False,
            },
        ),
    ]

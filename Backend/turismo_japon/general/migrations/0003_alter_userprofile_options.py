# Generated by Django 5.0.6 on 2024-07-09 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_authgroup_authgrouppermissions_authpermission_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'User Profile', 'verbose_name_plural': 'User Profiles'},
        ),
    ]
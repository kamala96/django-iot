# Generated by Django 4.2.3 on 2023-07-19 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0003_alter_devicetype_options_controller_access_key'),
    ]

    operations = [
        migrations.RenameField(
            model_name='controller',
            old_name='ip_address',
            new_name='network_address',
        ),
    ]

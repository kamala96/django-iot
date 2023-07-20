# Generated by Django 4.2.3 on 2023-07-20 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0007_rename_unique_id_controller_chip_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proximity',
            name='sensor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sensor_proximity', to='devices.sensor'),
        ),
    ]

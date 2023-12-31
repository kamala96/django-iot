# Generated by Django 4.2.3 on 2023-07-19 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0005_alter_controller_type_alter_proximity_sensor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controller',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type_controllers', to='devices.devicetype'),
        ),
        migrations.AlterField(
            model_name='proximity',
            name='sensor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sensor_proximity', to='devices.sensor'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='controller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='controller_sensors', to='devices.controller'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type_sensors', to='devices.devicetype'),
        ),
    ]

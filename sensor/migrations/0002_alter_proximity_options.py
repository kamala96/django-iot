# Generated by Django 4.2.3 on 2023-07-17 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proximity',
            options={'ordering': ('timestamp',), 'verbose_name': 'Proximity', 'verbose_name_plural': 'Proximity'},
        ),
    ]
# Generated by Django 4.2.6 on 2023-11-11 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tendencias', '0004_medicos_db'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicos',
            name='diagnostico',
        ),
    ]

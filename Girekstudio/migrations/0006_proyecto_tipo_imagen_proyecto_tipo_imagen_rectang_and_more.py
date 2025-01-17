# Generated by Django 4.0.6 on 2025-01-11 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Girekstudio', '0005_remove_servicio_imag_serv_princi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='tipo_imagen',
            field=models.BooleanField(default=False, help_text='Activar si es una imagen cuadrada '),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='tipo_imagen_rectang',
            field=models.BooleanField(default=False, help_text='Activar si es una imagen rectangular '),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='tipo_video',
            field=models.BooleanField(default=False, help_text='Activar si es un video de Youtube '),
        ),
    ]

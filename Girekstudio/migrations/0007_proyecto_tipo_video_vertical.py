# Generated by Django 4.0.6 on 2025-01-11 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Girekstudio', '0006_proyecto_tipo_imagen_proyecto_tipo_imagen_rectang_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='tipo_video_vertical',
            field=models.BooleanField(default=False, help_text='Activar si es un video Vertical de Youtube '),
        ),
    ]
# Generated by Django 4.0.6 on 2024-09-27 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vortice', '0006_rename_about_02_imagen_vortice_about_04_imagen_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vortice',
            name='about_03_imagen_01',
            field=models.ImageField(blank=True, help_text='imagenes 2000 × 1262 px', null=True, upload_to='vortice'),
        ),
    ]
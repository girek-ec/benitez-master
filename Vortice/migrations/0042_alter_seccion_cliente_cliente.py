# Generated by Django 4.2.20 on 2025-07-05 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vortice', '0041_prod_prenda_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seccion_cliente',
            name='cliente',
            field=models.CharField(choices=[('hombre', 'Hombre'), ('mujer', 'Mujer'), ('unisex', 'Unisex')], default='unisex', max_length=10),
        ),
    ]

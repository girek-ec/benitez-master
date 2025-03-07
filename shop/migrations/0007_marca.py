# Generated by Django 4.1.13 on 2025-03-04 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_category_icono'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favicon', models.ImageField(blank=True, help_text='imagenes 200*200', null=True, upload_to='colexin/')),
                ('logo_color', models.ImageField(blank=True, help_text='imagenes 200*200', null=True, upload_to='colexin/')),
                ('logo_blanco', models.ImageField(blank=True, help_text='imagenes 200*200', null=True, upload_to='colexin/')),
                ('whatsapp', models.CharField(blank=True, max_length=11, null=True)),
                ('celular', models.CharField(blank=True, max_length=11, null=True)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('instagram', models.CharField(blank=True, max_length=100, null=True)),
                ('tiktok', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('youtube', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': '2. Colexin',
            },
        ),
    ]

# Generated by Django 4.1.13 on 2025-02-18 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vortice', '0020_prod_prenda_size_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prod_prenda',
            name='has_sizes',
        ),
        migrations.RemoveField(
            model_name='prod_prenda',
            name='size_type',
        ),
    ]

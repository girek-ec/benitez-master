# Generated by Django 4.0.6 on 2024-09-22 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Girekstudio', '0032_remove_editables_sec_2_subti_2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='editables',
            name='sec_2_detalle_5',
        ),
        migrations.RemoveField(
            model_name='editables',
            name='sec_2_encabezado',
        ),
        migrations.RemoveField(
            model_name='editables',
            name='sec_2_imagen_6',
        ),
        migrations.RemoveField(
            model_name='editables',
            name='sec_2_subti_5',
        ),
        migrations.RemoveField(
            model_name='editables',
            name='sec_2_titulo_5',
        ),
    ]
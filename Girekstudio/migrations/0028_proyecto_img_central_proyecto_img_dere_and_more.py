# Generated by Django 4.0.6 on 2024-09-20 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Girekstudio', '0027_remove_editables_sec_4_subti_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='img_central',
            field=models.BooleanField(default=False, help_text='imagen a la izquierda '),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='img_dere',
            field=models.BooleanField(default=False, help_text='imagen a la izquierda '),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='img_izq',
            field=models.BooleanField(default=False, help_text='imagen a la izquierda '),
        ),
    ]

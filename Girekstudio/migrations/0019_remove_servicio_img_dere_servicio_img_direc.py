# Generated by Django 4.0.6 on 2024-09-18 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Girekstudio', '0018_servicio_img_dere'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio',
            name='img_dere',
        ),
        migrations.AddField(
            model_name='servicio',
            name='img_direc',
            field=models.BooleanField(default=False, help_text='Sec Agencia img activar si numero orden es  impar '),
        ),
    ]
# Generated by Django 4.0.6 on 2025-01-14 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Girekstudio', '0009_cliente_principal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imag_video_servicio',
            name='activo',
        ),
        migrations.AddField(
            model_name='imag_video_servicio',
            name='link_video',
            field=models.CharField(blank=True, help_text='Link video de youtube', max_length=200, null=True),
        ),
    ]

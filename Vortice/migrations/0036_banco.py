# Generated by Django 4.2.20 on 2025-03-18 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vortice', '0035_alter_prod_prenda_tipo_material'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=False)),
                ('ahorro', models.BooleanField(default=True)),
                ('corriente', models.BooleanField(default=False)),
                ('numero', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'verbose_name_plural': '12. Banco',
            },
        ),
    ]

# Generated by Django 4.0.6 on 2024-09-27 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zatuar', '0010_product_blanco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ficha_tec',
            field=models.FileField(blank=True, help_text='pdf', null=True, upload_to='zatuar/'),
        ),
    ]

# Generated by Django 4.0.6 on 2024-10-15 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca_benitez',
            name='horarioc',
            field=models.CharField(blank=True, default=1, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='marca_benitez',
            name='horariod',
            field=models.CharField(blank=True, default=1, max_length=100, null=True),
        ),
    ]

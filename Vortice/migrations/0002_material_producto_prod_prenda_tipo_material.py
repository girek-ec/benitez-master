# Generated by Django 4.0.6 on 2024-12-05 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vortice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material_producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'verbose_name_plural': '4. Material de producto',
            },
        ),
        migrations.AddField(
            model_name='prod_prenda',
            name='tipo_material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Vortice.material_producto'),
        ),
    ]

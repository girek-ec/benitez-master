# Generated by Django 4.0.6 on 2024-10-11 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clasif_producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clasificacion_producto', models.CharField(blank=True, max_length=90, null=True)),
            ],
            options={
                'verbose_name_plural': 'PROD- 01. Clasificación de Producto',
            },
        ),
        migrations.CreateModel(
            name='Editable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_fondo', models.ImageField(blank=True, help_text='slider', null=True, upload_to='niska/')),
                ('slider_imagen', models.ImageField(blank=True, help_text='slider', null=True, upload_to='niska/')),
                ('slider_titulo', models.CharField(blank=True, max_length=80, null=True)),
                ('slider_subtitulo', models.CharField(blank=True, max_length=80, null=True)),
                ('slider_detalle', models.TextField(blank=True, max_length=500, null=True)),
                ('sec1_imagen', models.ImageField(blank=True, help_text='cuadrada', null=True, upload_to='niska/')),
                ('sec1_titulo', models.CharField(blank=True, max_length=80, null=True)),
                ('sec1_subtitulo', models.CharField(blank=True, max_length=80, null=True)),
                ('sec1_detalle', models.TextField(blank=True, max_length=500, null=True)),
                ('sec2_titulo', models.CharField(blank=True, max_length=80, null=True)),
                ('sec2_subtitulo', models.CharField(blank=True, max_length=80, null=True)),
                ('sec3_titulo', models.CharField(blank=True, max_length=80, null=True)),
                ('sec3_subtitulo', models.CharField(blank=True, max_length=80, null=True)),
                ('empr_imagen', models.ImageField(blank=True, help_text='cuadrada', null=True, upload_to='niska/')),
                ('empr_titulo', models.CharField(blank=True, max_length=80, null=True)),
                ('empr_detalle', models.TextField(blank=True, max_length=500, null=True)),
                ('empr_imagen2', models.ImageField(blank=True, help_text='cuadrada', null=True, upload_to='niska/')),
                ('empr_titulo2', models.CharField(blank=True, max_length=80, null=True)),
                ('empr_detalle2', models.TextField(blank=True, max_length=500, null=True)),
                ('empr_imagen3', models.ImageField(blank=True, help_text='cuadrada', null=True, upload_to='niska/')),
                ('empr_titulo3', models.CharField(blank=True, max_length=80, null=True)),
                ('empr_detalle3', models.TextField(blank=True, max_length=500, null=True)),
                ('fondo_produ', models.ImageField(blank=True, help_text='horizontal', null=True, upload_to='niska/')),
                ('publicidad', models.ImageField(blank=True, help_text='vertical', null=True, upload_to='niska/')),
                ('contac_imagen', models.ImageField(blank=True, help_text='cuadrada', null=True, upload_to='niska/')),
                ('contac_titulo', models.CharField(blank=True, max_length=80, null=True)),
                ('contac_subtitulo', models.CharField(blank=True, max_length=80, null=True)),
                ('contac_detalle', models.TextField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name_plural': '1. Editable',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favicon', models.ImageField(blank=True, help_text='imagenes 20*20', null=True, upload_to='niska/')),
                ('logo_horizontal', models.ImageField(blank=True, help_text='imagenes 20*20', null=True, upload_to='niska/')),
                ('logo_blanco', models.ImageField(blank=True, help_text='imagenes 20*20', null=True, upload_to='niska/')),
                ('whatsapp', models.CharField(blank=True, max_length=11, null=True)),
                ('celular', models.CharField(blank=True, max_length=11, null=True)),
                ('celular2', models.CharField(blank=True, max_length=100, null=True)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('instagram', models.CharField(blank=True, max_length=100, null=True)),
                ('tiktok', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=100, null=True)),
                ('youtube', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': '2. Niska',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(blank=True, max_length=100, null=True)),
                ('stock', models.CharField(choices=[('stock', 'stock'), ('no_stock', 'no_stock')], default='stock', max_length=20)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='niska/')),
                ('descripcion', models.TextField(blank=True, max_length=500, null=True)),
                ('embalaje', models.CharField(blank=True, max_length=100, null=True)),
                ('empaque', models.CharField(blank=True, max_length=100, null=True)),
                ('sabores', models.CharField(blank=True, max_length=100, null=True)),
                ('duracion', models.CharField(blank=True, max_length=100, null=True)),
                ('presentaciones', models.CharField(blank=True, max_length=100, null=True)),
                ('ingredientes', models.CharField(blank=True, max_length=100, null=True)),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('clasif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Niska.clasif_producto')),
            ],
            options={
                'verbose_name_plural': 'PROD- 02. Producto',
            },
        ),
        migrations.CreateModel(
            name='Producto_Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('galeria_articulo', models.ImageField(blank=True, help_text='imagen producto 800x800', null=True, upload_to='niska/')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Niska.producto')),
            ],
            options={
                'verbose_name_plural': 'PROD- 03. Producto Imagenes',
            },
        ),
    ]
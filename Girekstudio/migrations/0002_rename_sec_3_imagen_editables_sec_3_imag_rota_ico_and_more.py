# Generated by Django 4.0.6 on 2024-10-13 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Girekstudio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='editables',
            old_name='sec_3_imagen',
            new_name='sec_3_imag_rota_ico',
        ),
        migrations.AddField(
            model_name='editables',
            name='sec_3_palabra',
            field=models.CharField(blank=True, help_text='Agencia bajo de encabezado palabra ', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='editables',
            name='sec_3_subti_2',
            field=models.FileField(blank=True, help_text='Agencia texto rotativo', null=True, upload_to='girekstudio/'),
        ),
    ]

# Generated by Django 2.2 on 2020-04-14 21:07

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letras', '0021_columns_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='columns',
            options={'verbose_name': 'Columna', 'verbose_name_plural': 'Columnas'},
        ),
        migrations.AlterField(
            model_name='columns',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido Columna'),
        ),
    ]

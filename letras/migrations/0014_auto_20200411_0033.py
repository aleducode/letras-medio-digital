# Generated by Django 3.0.5 on 2020-04-11 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letras', '0013_notice_podcast'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name': 'Generador de link para Imagenes', 'verbose_name_plural': 'Generador de link para Imagenes'},
        ),
        migrations.AlterModelOptions(
            name='notice',
            options={'get_latest_by': 'created', 'ordering': ['-created', '-modified'], 'verbose_name': 'Noticia', 'verbose_name_plural': 'Noticias'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name': 'Sección', 'verbose_name_plural': 'Secciones'},
        ),
        migrations.AlterModelOptions(
            name='suscriptor',
            options={'verbose_name': 'Suscritor', 'verbose_name_plural': 'Suscritores'},
        ),
    ]

# Generated by Django 2.2 on 2019-04-20 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letras', '0004_auto_20190420_2050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Linkedin',
            new_name='linkedin',
        ),
    ]

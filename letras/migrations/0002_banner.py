# Generated by Django 3.1 on 2020-08-24 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positions', models.CharField(choices=[('Principal', 'Principal'), ('Side', 'Side')], default='Side', max_length=55)),
                ('images', models.ImageField(upload_to='banners/')),
            ],
        ),
    ]

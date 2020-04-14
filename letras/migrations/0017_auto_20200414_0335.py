# Generated by Django 2.2 on 2020-04-14 03:35

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('letras', '0016_podcast'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='priority',
            field=models.PositiveIntegerField(choices=[(1, 'Top 1'), (2, 'Top 2'), (3, 'Normal')]),
        ),
        migrations.CreateModel(
            name='columns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Titulo Columna')),
                ('text', ckeditor.fields.RichTextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

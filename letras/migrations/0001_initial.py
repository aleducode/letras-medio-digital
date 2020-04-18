# Generated by Django 2.2 on 2020-04-16 21:30

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import letras.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo de la imagen')),
                ('route', models.FileField(upload_to='img/')),
            ],
            options={
                'verbose_name': 'Generador de link para Imagen',
                'verbose_name_plural': 'Generador de link para Imagen',
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Titulo Noticia')),
                ('lead', models.TextField(blank=True, null=True, verbose_name='Lead Noticia')),
                ('text', ckeditor.fields.RichTextField()),
                ('video', models.URLField(blank=True)),
                ('video_file', models.FileField(blank=True, null=True, upload_to='video_files/')),
                ('podcast', models.FileField(blank=True, null=True, upload_to='audios/')),
                ('priority', models.PositiveIntegerField(choices=[(1, 'Top 1'), (2, 'Top 2'), (3, 'Normal')], verbose_name='Prioridad')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre Seccion')),
                ('is_active', models.BooleanField(default=1, verbose_name='Activa')),
                ('color_background', models.CharField(blank=True, help_text='Hexagecimal color.', max_length=10, null=True, verbose_name='Color Fondo')),
                ('color_text', models.CharField(blank=True, help_text='Hexagecimal color.', max_length=10, null=True, verbose_name='Color Letra')),
                ('order', models.PositiveIntegerField(verbose_name='Posición en pantalla')),
            ],
            options={
                'verbose_name': 'Sección',
                'verbose_name_plural': 'Secciones',
            },
        ),
        migrations.CreateModel(
            name='Suscriptor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre Sucriptior')),
                ('email', models.CharField(max_length=255, verbose_name='Correo')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Suscritor',
                'verbose_name_plural': 'Suscritores',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(blank=True, max_length=30, verbose_name='Cargo')),
                ('role', models.PositiveIntegerField(blank=True, choices=[(1, 'Administrador'), (2, 'Columnista'), (3, 'Podcaster'), (4, 'Columnista - Podcaster')], null=True)),
                ('biography', models.TextField(blank=True, null=True, verbose_name='Biografia')),
                ('picture', models.ImageField(blank=True, null=True, upload_to=letras.models.user_directory_path)),
                ('facebook', models.URLField(blank=True, verbose_name='Perfil Facebook')),
                ('instagram', models.URLField(blank=True, verbose_name='Perfil instagram')),
                ('twitter', models.URLField(blank=True, verbose_name='Perfil Twitter')),
                ('linkedin', models.URLField(blank=True, verbose_name='Perfil Linkedin')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo del podcast')),
                ('picture', models.FileField(default='img', upload_to='img_podcasts', verbose_name='Imagen')),
                ('podcast', models.FileField(upload_to='podcasts/', verbose_name='Audio Podcast')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Descripcion')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route', models.FileField(upload_to=letras.models.notices_directory_path)),
                ('is_principal', models.BooleanField(default=True, verbose_name='Es Principal')),
                ('footer', models.CharField(blank=True, default='Imaegen por: Letras Medio', max_length=500, null=True, verbose_name='Pie de foto')),
                ('notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='letras.Notice')),
            ],
            options={
                'ordering': ['-notice__created', '-notice__modified'],
                'get_latest_by': 'notice__created',
            },
        ),
        migrations.AddField(
            model_name='notice',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='letras.Section', verbose_name='Seccion'),
        ),
        migrations.AddField(
            model_name='notice',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Columns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Titulo Columna')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Contenido Columna')),
                ('image', models.ImageField(default='img', upload_to='img_columns', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Columna',
                'verbose_name_plural': 'Columnas',
            },
        ),
    ]

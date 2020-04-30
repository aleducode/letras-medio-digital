"""Letras Models."""

# Django
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver

# Utils
from ckeditor.fields import RichTextField
import PIL
from PIL import Image
ROL_CHOICES = (
    (1, 'Administrador'),
    (2, 'Columnista'),
    (3, 'Podcaster'),
    (4, 'Columnista - Podcaster')
)

PRIORIDAD_CHOICES = (
    (1, 'Top 1'),
    (2, 'Top 2'),
    (3, 'Normal'),
)


def user_directory_path(instance, filename):
    """Route to storage user picture."""
    return 'user{0}/{1}'.format(instance.user.id, filename)


def notices_directory_path(instance, filename):
    """Route to storage notice(s) picture."""
    return 'notice{0}/{1}'.format(instance.notice.id, filename)


class Profile(models.Model):
    """Profile model that extens the db with other informations."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField('Cargo', max_length=30, blank=True)
    role = models.PositiveIntegerField(
        choices=ROL_CHOICES,
        null=True,
        blank=True
    )
    biography = models.TextField('Biografia', null=True, blank=True)
    picture = models.ImageField(
        upload_to=user_directory_path,
        blank=True,
        null=True
    )
    facebook = models.URLField('Perfil Facebook', max_length=200, blank=True)
    instagram = models.URLField('Perfil instagram', max_length=200, blank=True)
    twitter = models.URLField('Perfil Twitter', max_length=200, blank=True)
    linkedin = models.URLField('Perfil Linkedin', max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username."""
        return self.user.username

    def save(self):
        super(Profile, self).save()
        picture = Image.open(self.picture)
        picture = picture.resize((190,190), Image.ANTIALIAS)
        picture.save(self.picture.path)


class Section(models.Model):
    """Notice section."""

    name = models.CharField('Nombre Seccion', max_length=255)
    is_active = models.BooleanField(
        'Activa',
        default=1,
    )
    color_background = models.CharField(
        'Color Fondo',
        max_length=10,
        null=True,
        blank=True,
        help_text='Hexagecimal color.')
    color_text = models.CharField(
        'Color Letra',
        max_length=10,
        null=True,
        blank=True,
        help_text='Hexagecimal color.')
    order = models.PositiveIntegerField('Posición en pantalla')

    def __str__(self):
        """Return username."""
        return self.name

    class Meta:
        verbose_name = 'Sección'
        verbose_name_plural = 'Secciones'



class Notice(models.Model):
    """Notice model."""

    title = models.TextField('Titulo Noticia')
    lead = models.TextField('Lead Noticia', null=True, blank=True)
    text = RichTextField()
    video = models.URLField(max_length=200, blank=True)
    video_file = models.FileField(upload_to = 'video_files/', null = True, blank= True)
    podcast = models.FileField(upload_to='audios/', null=True, blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name = 'Seccion')
    priority = models.PositiveIntegerField(choices=PRIORIDAD_CHOICES, verbose_name='Prioridad')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta option."""

        get_latest_by = 'created'
        ordering = ['-created', '-modified']
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    def __str__(self):
        """Return notice's title."""
        return '{} | {}'.format(self.title, self.section)

    @property
    def principal_picture(self):
        """Return principal image url."""
        return self.pictures.filter(is_principal=True).last().route.url


class Picture(models.Model):
    """Picture model."""

    notice = models.ForeignKey(
        Notice,
        on_delete=models.CASCADE,
        related_name='pictures'
    )
    route = models.FileField(upload_to=notices_directory_path)
    is_principal = models.BooleanField(
        'Es Principal',
        default=True,
    )
    footer = models.CharField(
        'Pie de foto',
        max_length=500,
        null=True,
        blank=True,
        default='Imagen por: Letras Medio')

    def __str__(self):
        """Return notice name."""
        return 'Notice:{}'.format(self.notice)

    class Meta:
        get_latest_by = 'notice__created'
        ordering = ['-notice__created', '-notice__modified']


class Images(models.Model):
    """Model por temporal images."""

    title = models.CharField('Titulo de la imagen', max_length=200)
    route = models.FileField(upload_to='img/')

    def __str__(self):
        """Return complente url."""
        return '{}{}'.format(
            settings.SITE_URL,
            self.route.url
        )

    class Meta:
        verbose_name = 'Generador de link para Imagen'
        verbose_name_plural = 'Generador de link para Imagen'


class Suscriptor(models.Model):
    """Class for suscriptors storage."""

    name = models.CharField('Nombre Sucriptior', max_length=255)
    email = models.CharField('Correo', max_length=255)
    is_active = models.BooleanField(
        'Activo',
        default=True,
    )

    def __str__(self):
        """Return suscriptor."""
        return 'Suscriptior:{}'.format(self.name)

    class Meta:
        verbose_name = 'Suscritor'
        verbose_name_plural = 'Suscritores'


class Podcast(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Titulo del podcast')
    picture = models.FileField(upload_to = 'img_podcasts', default = 'img', verbose_name ='Imagen')
    user = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name = 'Usuario')
    podcast = models.FileField(upload_to ='podcasts/', verbose_name = 'Audio Podcast')
    description = RichTextField(verbose_name= 'Descripcion')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Columns(models.Model):
    """Notice model."""
    title = models.TextField('Titulo Columna')
    text = RichTextField(verbose_name='Contenido Columna')
    image = models.ImageField(upload_to = "img_columns", default = "img", verbose_name= 'Imagen')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name = 'Usuario'
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Columna"
        verbose_name_plural = "Columnas"

@receiver(post_save, sender =Notice)
def change_notice(sender,instance, **kwargs):
    priority = instance.priority
    ult_priority = Notice.objects.filter(priority=1)
    ult_prioritytwo = Notice.objects.filter(priority=2)


    if  priority == 1:
        if ult_priority.count() > 1 and ult_priority:
            N= ult_priority.last()
            N.priority = 2
            N.save()

    if ult_prioritytwo.count() >= 5:
        ult_notice = ult_prioritytwo.last()
        ult_notice.priority = 3
        ult_notice.save()

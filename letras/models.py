"""Letras Models."""

# Django
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


# Utils
from ckeditor.fields import RichTextField


ROL_CHOICES = (
    (1, 'Administrador'),
    (2, 'Columnista')
)

PRIORIDAD_CHOICES = (
    (1, 'Top 1'),
    (2, 'Top 2'),
    (3, 'Normal'),
    (4, 'Columna')
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
    podcast = models.FileField(upload_to='audios/', null=True, blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    priority = models.PositiveIntegerField(choices=PRIORIDAD_CHOICES)

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
        default='por: Letras Medio')

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

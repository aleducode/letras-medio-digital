"""Letras Models"""

#Django
from django.contrib.auth.models import User
from django.db import models


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
    """Route to storage user picture"""
    return 'user{0}/{1}'.format(instance.user.id, filename)


def notices_directory_path(instance, filename):
    """Route to storage notice(s) picture"""
    return 'notice{0}/{1}'.format(instance.notice.id, filename)


class Profile(models.Model):
    """Profile model that extens the db with other informations"""
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
        """return username"""
        return self.user.username


class Section(models.Model):
    """Notice sections"""
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
        """return username"""
        return self.name


class Notice(models.Model):
    """Notice model."""

    title = models.TextField('Titulo Noticia')
    lead = models.TextField('Lead Noticia', null=True, blank=True)
    text = models.TextField('Texto Noticia')
    video = models.URLField(max_length=200, blank=True)
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

    def __str__(self):
        """return notice's title."""
        return '{} | {}'.format(self.title, self.section)

    @property
    def principal_picture(self):
        """Return principal image url."""
        return self.pictures.get(is_principal=True).route.url


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
        default=False,
    )
    footer = models.CharField(
        'Pie de foto',
        max_length=500,
        null=True,
        blank=True,
        default='por: Letras Medio')

    def __str__(self):
        """returrn picture name"""
        return 'Notice:{}'.format(self.notice)

    class Meta:
        """Meta option."""
        get_latest_by = 'notice__created'
        ordering = ['-notice__created', '-notice__modified']


class Suscriptor(models.Model):
    """Class for suscriptors storage"""
    name = models.CharField('Nombre Sucriptior', max_length=255)
    email = models.CharField('Correo', max_length=255)
    is_active = models.BooleanField(
        'Activo',
        default=True,
    )

    def __str__(self):
        """return suscriptor."""
        return 'Suscriptior:{}'.format(self.name)

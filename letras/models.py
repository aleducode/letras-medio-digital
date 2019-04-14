"""Letras Models"""

#Django
from django.contrib.auth.models import User
from django.db import models



ROL_CHOICES=(
    (1,'Administrador'),
	(2,'Columnista')
    )

PRIORIDAD_CHOICES=(
    (1,'Top 1'),
    (2,'Top 2'),
    (3,'Normal')
		)

def user_directory_path(instance,filename):
    """Route to storage user picture"""
    return 'user{0}/{1}'.format(instance.usuario.id,filename)

def user_directory_path(instance,filename):
    """Route to storage notice(s) picture"""
    return 'notice{0}/{1}'.format(instance.noticia.id,filename)

class Profile(models.Model):
    """Profile model that extens the db with other informations"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField('Cargo',max_length=30,blank=True)
    role = models.PositiveIntegerField(
        choices=ROL_CHOICES,
        null=True,
        blank=True
        )
    biography=models.TextField('Biografia',null=True,blank=True)
    picture=models.ImageField(
        upload_to=user_directory_path,
        blank=True,
        null=True
        )
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        """return username"""
        return self.user.username
class Section(models.Model):
    """Notice sections"""
    name=models.CharField('Nombre Seccion',max_length=255)
    is_active=models.BooleanField(
        'Activa',
        default=1,
    )

class Notice(models.Model):
    """Notice model"""
    title = models.TextField('Titulo Noticia')
    lead = models.TextField('Lead Noticia',null=True,blank=True)
    text = models.TextField('Texto Noticia')
    video = models.URLField(max_length=200,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    section = models.ForeignKey(Section,on_delete=models.CASCADE)
    priority = models.PositiveIntegerField(choices=PRIORIDAD_CHOICES)

    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        """return notice's title"""
        return '{} by @{}'.format(self.title, self.user.first_name)
	
class Picture(models.Model):
    """Picture model"""
    notice = models.ForeignKey(Notice,models.CASCADE)
    route = models.FileField(upload_to=user_directory_path)
    name_picture = models.CharField('Texto Noticia',max_length=500,null=True,blank=True)
    is_principal=models.BooleanField(
        'Principal',
        default=1,
    )
    footer = models.CharField('Pie de foto',max_length=500,null=True,blank=True)
    def __str__(self):
        """returrn picture name"""
        return 'Notice:{}'.format(self.notice)
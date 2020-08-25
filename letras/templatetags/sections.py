"""Template Tags."""

# Django
from django import template

# Models
from letras.models import Section, Notice, Banner, Company

register = template.Library()
@register.inclusion_tag('base/sections.html')
def show_sections():
    sections = Section.objects.filter(is_active=True).order_by('order')
    return {'sections': sections}


@register.inclusion_tag('base/breaking_news.html')
def show_breakings():
    breakings = Notice.objects.all()[0:3]
    return {'breakings': breakings}


@register.simple_tag
def get_youtube(url):
    url = url.split('v=')
    return url[1]


@register.simple_tag
def get_getprincipal():
    principals = Banner.objects.filter(position=Banner.PRINCIPAL)
    if principals:
        return principals.last().images.url
    else:
        return None


@register.simple_tag
def get_getcompany():
    seccion = Company.objects.all().first()
    return seccion

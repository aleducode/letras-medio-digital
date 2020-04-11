"""Template Tags."""

# Django
from django import template

# Models
from letras.models import Section, Notice

register = template.Library()
@register.inclusion_tag('base/sections.html')
def show_sections():
    sections = Section.objects.filter(is_active=True)
    return {'sections': sections}


@register.inclusion_tag('base/breaking_news.html')
def show_breakings():
    breakings = Notice.objects.all()[0:3]
    return {'breakings': breakings}


@register.simple_tag
def get_youtube(url):
    url = url.split('v=')
    return url[1]

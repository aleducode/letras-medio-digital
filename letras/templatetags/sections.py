"""Template Tags"""

#Django
from django import template
from django.conf import settings
from django.contrib.staticfiles.finders import find as find_static_file

#Models
from letras.models import Section 

register = template.Library()
@register.inclusion_tag('base/sections.html')
def show_sections():
    sections = Section.objects.filter(is_active=True)
    return {'sections': sections}

@register.simple_tag
def get_youtube(url):
    url = url.split('v=')
    return url[1]


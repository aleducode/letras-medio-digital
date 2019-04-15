"""Template Tags"""

#Django
from django import template
from django.conf import settings
from django.contrib.staticfiles.finders import find as find_static_file

#Models
from letras.models import Section 

register = template.Library()

@register.simple_tag
def sections_active():
    """return active sessions"""
    sections = Section.objects.filter(is_active=True)
    return {'sections': sections}
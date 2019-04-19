""" users forms"""

#Django
from django import forms

#Models 
from letras.models import *

class SuscriptorsForm(forms.ModelForm):
    """ post model form"""
    class Meta:
        model=Suscriptors
        fields=('name','email')
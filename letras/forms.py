"""Users forms."""

# Django
from django import forms

# Models
from letras.models import Suscriptor


class SuscriptorsForm(forms.ModelForm):
    """Subscriptor model form."""

    class Meta:
        model = Suscriptor
        fields = ('name', 'email')

"""Letras view"""

#Django

from django.shortcuts import render, redirect
from django.views.generic import DetailView, FormView, UpdateView,TemplateView
from django.urls import reverse_lazy
#Models
from letras.models import *

class IndexView(TemplateView):
    """Index view letras"""
    template_name = 'index.html'



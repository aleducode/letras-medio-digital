"""Letras view."""

# Django
from django.shortcuts import render, redirect
from django.views.generic import (
    DetailView, FormView,
    TemplateView, ListView
)
import requests
import json
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponse
from covid.utils import *
# Models
from letras.models import (
    Notice, Picture,
    Profile, Suscriptor,
    Podcast, Columns
)
from letras.forms import SuscriptorsForm
# Utils
from sweetify.views import SweetifySuccessMixin


class IndexView(SweetifySuccessMixin, FormView):
    """Index view letras."""

    template_name = 'index.html'
    form_class = SuscriptorsForm
    success_message = 'Suscripción exitosa'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        """Add notices to context."""
        context = super().get_context_data(**kwargs)
        # Top notices
        top_one = Notice.objects.filter(priority=1)
        context['top1_notice'] = top_one.first() if top_one.exists() else None
        context['top2_notices'] = Notice.objects.filter(
            priority=2).order_by('-created')
        context['notices'] = Notice.objects.filter(
            priority=3).order_by('-created')
        #Contagiados en tiempo real Coronavirus
        context['total_casos'] = total_cases()
        context['casos_activos'] = active_cases()
        context['recuperados'] = total_recovered()
        context['muertes'] = total_deaths()

        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PublicationView(DetailView):
    """Publication viewer."""
    template_name = 'publication.html'
    pk_url_kwarg = 'pk'
    queryset = Notice.objects.all()
    context_object_name = 'notice'

    def get_context_data(self, **kwargs):
        """Detail contex."""
        context = super().get_context_data(**kwargs)
        notice = self.get_object()
        context['top2_notices'] = Notice.objects.filter(
            priority=2).exclude(pk=notice.pk).order_by('-created')
        # Related section
        context['section_notices'] = Notice.objects.filter(
            section=notice.section).exclude(pk=notice.pk).order_by('-created')
        return context


class SectionView(TemplateView):
    """Section Generic viewer."""

    template_name = 'section.html'

    def get_context_data(self, **kwargs):
        """Notices context."""
        context = super().get_context_data(**kwargs)
        context['notices'] = Notice.objects.filter(
            section=self.kwargs['section']).order_by('-created')
        context['top_notices'] = Notice.objects.filter(
            Q(priority=2) | Q(priority=1)).order_by('-created')
        return context


class OpinionView(TemplateView):
    """Section opinion  View."""

    template_name = 'opinion.html'

    def get_context_data(self, **kwargs):
        """add picture and other notices to context"""
        #normal context without override it
        context = super().get_context_data(**kwargs)
        #section information
        context['columns'] = Columns.objects.all()

        return context

class ColumnDetailView(DetailView):
    """Column detail."""

    template_name = 'column_detail.html'
    pk_url_kwarg = 'pk'
    queryset = Columns.objects.all()
    context_object_name = 'column'

class ColumnView(DetailView):
    """Section opinion View."""
    template_name = 'perfil.html'
    slug_url_kwarg = 'user'
    slug_field = 'user'
    queryset = Profile.objects.all()
    context_object_name = 'columnist'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['columns'] = Columns.objects.all()[0:3]
        context['podcasts'] = Podcast.objects.filter(user=self.kwargs['user']).order_by('-created')[0:3]
        context['other_columnist'] = Profile.objects.filter(
            role=2).exclude(user = self.kwargs['user'] ).order_by('-created')
        return context


class PodcastView(DetailView):
    template_name= 'podcast_detail.html'
    queryset = Podcast.objects.all()
    contex_object_name = 'podcast'

    def get_context_data(self, **kwargs):
        contex = super(PodcastView, self).get_context_data(**kwargs)
        contex['more_podcasts'] = Podcast.objects.exclude( pk = self.kwargs['pk'])
        return contex

class PodcastList(ListView):
    paginate_by = 4
    model = Podcast
    template_name = 'podcast_list.html'


def trigger_error(request):
    division_by_zero = 1 / 0




def create_suscriptor(request):
    """Ajax receptor to create sucriptor."""
    if request.method == 'POST':
        email = request.POST.get('email')
        user_subscribed = Suscriptor.objects.filter(email=email)
        if not user_subscribed:
            data = {
                'name': request.POST.get('name'),
                'email': email,
            }
            Suscriptor.objects.create(**data)
            return HttpResponse(1)
        else:
            return HttpResponse(0)

"""Letras view"""

#Django

from django.shortcuts import render, redirect
from django.views.generic import (  DetailView,FormView,
                                    UpdateView,TemplateView,
                                    ListView, CreateView
                                )
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponse
#Models
from letras.models import *
from letras.forms import *
from django.template.loader import get_template
#utils
from sweetify.views import SweetifySuccessMixin
import sweetify



class IndexView(SweetifySuccessMixin,FormView):
    """Index view letras"""
    template_name = 'index.html'
    form_class = SuscriptorsForm
    success_message = 'TestModel successfully updated!'
    success_url = reverse_lazy('index')
    
    def get_context_data(self,**kwargs):
        """add notices post to context"""
        #normal context without override it
        context=super().get_context_data(**kwargs)
        #result of query
        #top1
        context['top1_notice'] = Notice.objects.get(priority=1)
        context['top1_image'] = Picture.objects.get(
            notice=context['top1_notice'], is_principal=True)
        #top2
        context['top2_notices'] = Notice.objects.filter(
            priority=2).order_by('-created')
        context['top2_images'] = Picture.objects.filter(
            notice__in=context['top2_notices'], is_principal=True)
        #latest
        context['notices'] = Notice.objects.filter(
            priority=3).order_by('-created')
        context['images'] = Picture.objects.filter(
            notice__in=context['notices'], is_principal=True)
        return context

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)


class PublicationView(DetailView):
    """Publication viewer"""
    template_name = 'publication.html'
    pk_url_kwarg = 'pk'
    queryset=Notice.objects.all()
    context_object_name='notice'

    def get_context_data(self,**kwargs):
        """add picture and other notices to context"""
        #normal context without override it
        context=super().get_context_data(**kwargs)
        #result of query 
        notice=self.get_object()
        context['picture']= Picture.objects.get(notice=notice) or None
        #top 2
        #top2
        context['top2_notices'] = Notice.objects.filter(
            priority=2).exclude(pk=notice.pk).order_by('-created')
        context['top2_images'] = Picture.objects.filter(
            notice__in=context['top2_notices'], is_principal=True)
        #section
        context['section_notices'] = Notice.objects.filter(
            section=notice.section).exclude(pk=notice.pk).order_by('-created')
        context['section_images'] = Picture.objects.filter(
            notice__in=context['section_notices'], is_principal=True)
        return context

class SectionView(TemplateView):
    """Section Generic viewer"""
    template_name = 'section.html'
    #TODO: paginator
    def get_context_data(self,**kwargs):
        """add picture and other notices to context"""
        #normal context without override it
        context=super().get_context_data(**kwargs)
        #section information 
        context['notices']= Notice.objects.filter(
            section=self.kwargs['section']).order_by('-created')
        context['images'] = Picture.objects.filter(
            notice__in=context['notices'], is_principal=True)
        #recent publications
        context['top_notices'] = Notice.objects.filter(
            Q(priority=2)|Q(priority=1)).order_by('-created')
        context['top_images'] = Picture.objects.filter(
            notice__in=context['top_notices'], is_principal=True)
        return context

def create_suscriptor(request):
    """ajax receptor to create sucriptor"""
    if request.method == 'POST':
        email = request.POST.get('email')
        user_subscribed = Suscriptors.objects.filter(email=email)
        if not user_subscribed:
            data={
                'name':request.POST.get('name'),
                'email':email,
            }
            Suscriptors.objects.create(**data)
            return HttpResponse(1)
        else:
            return HttpResponse(0)
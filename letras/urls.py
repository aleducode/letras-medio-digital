"""Letras URLs."""

# Django
from django.urls import path
from django.views.generic import TemplateView

# View
from letras import views


urlpatterns = [
    path(
        route='',
        view=views.IndexView.as_view(),
        name='index'),
    path(
        route='publicacion/<int:pk>/',
        view=views.PublicationView.as_view(),
        name='publication'),
    path(
        route='seccion/<int:section>/',
        view=views.SectionView.as_view(),
        name='section'),
    path(
        route='ajax_suscriptor/',
        view=views.create_suscriptor,
        name='ajax_suscriptor'),
    
]
"""Letras URLs."""

# Django
from django.urls import path

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
        route='opinion/',
        view=views.OpinionView.as_view(),
        name='opinion'),
    path(
        route='ajax_suscriptor/',
        view=views.create_suscriptor,
        name='ajax_suscriptor'),
    path(
        route='perfil/<int:user>',
        view=views.ColumnView.as_view(),
        name='perfil'),

    path(
        route='columna/<int:pk>',
        view=views.ColumnDetailView.as_view(),
        name='column'),
    path(
        route='podcast/<int:pk>',
        view =views.PodcastView.as_view(),
        name='podcast'
    ),
    path(
        route='podcasts/',
        view=views.PodcastList.as_view(),
        name='podcasts'
    ),
    path('debug_error/', views.trigger_error),




]

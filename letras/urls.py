"""Letras URLs."""

# Django
from django.urls import path
from django.views.generic import TemplateView

# View
from letras import views


urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('publicacion/<int:pk>/',views.PublicationView.as_view(), name='publication'),


]
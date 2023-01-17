from django.urls import path

from . import views

app_name = 'example_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('forms', views.forms, name='forms'),
    path('template_tags', views.template_tags, name='template_tags'),
]
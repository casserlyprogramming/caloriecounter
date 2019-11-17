from django.urls import path, re_path

from . import views

urlpatterns = [
    path('save', views.save, name='save'),
    re_path(r'$', views.index, name='index'),
]

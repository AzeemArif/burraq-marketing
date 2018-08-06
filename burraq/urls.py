from django.conf.urls import url
from django.urls import path

from . import views
from burraq.views import indexView

urlpatterns = [
    path('', views.index, name='index'),
    url('home', indexView.as_view(), name='indexView'),
]
from django.conf.urls import url
from django.urls import path

from . import views
from burraq.views import indexView

urlpatterns = [
    path('', views.index, name='index'),
    # url('home', indexView.as_view(), name='indexView'),
    url('home', views.indexView, name='indexView'),
    # url(r'^email/$',views.email,name='email'),
    path('success/', views.successView, name='success'),
]
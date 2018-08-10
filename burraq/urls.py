from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static

from burraqMarketing import settings
from . import views
from burraq.views import indexView

urlpatterns = [
    # path('', views.index, name='index'),
    url('', indexView.as_view(), name='indexView'),
    # url(r'^email/$',views.email,name='email'),
    path('success/', views.successView, name='success'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
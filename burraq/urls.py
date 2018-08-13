from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static

from burraqMarketing import settings
from . import views

urlpatterns = [
    url(r'success/$', views.successView, name='success'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
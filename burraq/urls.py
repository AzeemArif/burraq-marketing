from django.conf.urls import url
from django.conf.urls.static import static
from burraq.views import successView
from burraqMarketing import settings

urlpatterns = [
    url(r'success/$', successView.as_view(), name='success'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
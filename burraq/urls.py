from django.conf.urls import url
from django.conf.urls.static import static
from burraq.views import successView, ZohoView
from burraqMarketing import settings

urlpatterns = [
    url(r'success/$', successView.as_view(), name='success'),
    url(r'verifyforzoho.html/$', ZohoView.as_view(), name='zoho'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from menu.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('about/', contact, name='contact'),
    path('api/', include('api.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)

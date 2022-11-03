from django.contrib import admin
from django.urls import path, include

from menu.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='hone'),
    path('about/', contact, name='contact'),
    path('api/', include('api.urls')),
]

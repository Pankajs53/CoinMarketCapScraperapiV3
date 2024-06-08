# myceleryproject/urls.py

from django.contrib import admin
from django.urls import path, include   # Import include to include URLs from other apps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls')),
]

# myceleryproject/urls.py
from django.urls import path   # Import include to include URLs from other apps
from myapp import views
from .views import ScrapingView


urlpatterns = [
    path('',views.index, name='home'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('api/taskmanager/start_scraping/', ScrapingView.as_view(), name='start_scraping'),
    path('api/taskmanager/scraping_status/<str:task_id>/', ScrapingView.as_view(), name='task_status'),
    
]

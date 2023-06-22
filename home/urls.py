from django.urls import path
from .views import HomeView, AboutView, PrivacyView, ContactView

urlpatterns = [
    path('', HomeView, name='home'),
    path('about/', AboutView, name='about'),
    path('privacy/', PrivacyView, name='privacy'),
    path('contact/', ContactView, name='contact')
]

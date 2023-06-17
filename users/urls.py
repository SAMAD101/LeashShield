from django.urls import path
from .views import LoginView, LoginPage

urlpatterns = [
    path('login/', LoginView, name='login'),
    path('register/', LoginPage, name='register'),
]
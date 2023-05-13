from django.urls import path
from .views import LoginPage, RegisterPage

urlpatterns = [
    path('login/', LoginPage.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
]
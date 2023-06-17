from django.urls import path
from .views import LoginView, RegisterView

urlpatterns = [
    path('login/', LoginView, name='login'),
    path('register/', RegisterView, name='register'),
]
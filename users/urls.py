from django.urls import path
from .views import LoginView, RegisterView, DashboardView

urlpatterns = [
    path('login/', LoginView, name='login'),
    path('register/', RegisterView, name='register'),
    path('dashboard/<str:username>/', DashboardView, name='dashboard'),
    
]
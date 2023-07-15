from django.urls import path
from .views import LoginView, RegisterView, DashboardView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', LoginView, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterView, name='register'),
    path('dashboard/<str:username>/', DashboardView, name='dashboard'),
    
]
from django.urls import path
from .views import react_app

urlpatterns = [
    # Your other URL patterns
    path('', react_app, name='react_app'),
]

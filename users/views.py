from django.shortcuts import render
from django.views.generic import TemplateView


class LoginPage(TemplateView):
    template_name = 'users/login.html'

class RegisterPage(TemplateView):
    template_name = 'users/register.html'

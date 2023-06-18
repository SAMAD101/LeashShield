from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Passwords
from .forms import RegisterationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = RegisterationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'is_staff',]
    

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Passwords)

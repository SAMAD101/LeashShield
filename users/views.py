from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.dispatch import receiver
from .models import CustomUser, PasswordEntry
from django.contrib.auth import authenticate, login
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.decorators import login_required
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

def LoginView(request):
    if request.method == 'POST':
        identity = request.POST.get('identity')
        password = request.POST.get('password') # masterpassword
        try: 
            if '@' in identity:
                email = identity
                username = CustomUser.objects.get(email=email).username
            else:
                username = identity
                email = CustomUser.objects.get(username=username).email
            user = authenticate(request, username=username, email=email, password=password)
        except:
            return HttpResponse('User does not exist')
        
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('dashboard', username=username)
    return render(request, 'users/login.html')

@receiver(user_logged_in)
def derive_encryption_key(sender, user, request, **kwargs):
    # Use the user's master password as the input to PBKDF2
    salt = os.urandom(16)

    # key derivation function (KDF) using HMAC-SHA256
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    encryption_key = kdf.derive(user.password.encode('utf-8'))

    user.salt = salt
    user.encryption_key = encryption_key
    user.save()

def RegisterView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        mpassword = request.POST.get('mpassword')
        cmpassword = request.POST.get('cmpassword')
        
        if mpassword != cmpassword:
            return HttpResponse('Passwords do not match')
        elif CustomUser.objects.filter(email=email).exists():
            return HttpResponse('User with this email already exist')
        elif CustomUser.objects.filter(username=username).exists():
            return HttpResponse('User with this username already exist')
        else:
            user = CustomUser.objects.create_user(username=username, email=email, password=mpassword)
            user.save()
            return redirect('login')
    return render(request, 'users/register.html')

@login_required
def DashboardView(request, username):
    user = request.user
    passwords = PasswordEntry.objects.filter(user=user);
    
    contexts = {
        'passwords': passwords,
        'user': user.username,
    }
    
    if request.method == 'POST':
        purpose = request.POST.get('purpose')
        
        if purpose == "add_password":
            PasswordEntry.objects.create(
                user=user,
                url=request.POST.get('url'),
                saved_password=request.POST.get('spassword'),
            )
            return redirect('dashboard', username=username)
        
        if purpose == "edit_password":
            pk = request.POST.get('id')
            url = request.POST.get('url')
            npassword = request.POST.get('npassword')
            PasswordEntry.objects.filter(pk=pk).update(url=url, saved_password=npassword)
            return redirect('dashboard', username=username)
        
        if purpose == "delete_password":
            pk = request.POST.get('id')
            PasswordEntry.objects.filter(pk=pk).delete()
            return redirect('dashboard', username=username)
        
    return render(request, 'users/dashboard.html', contexts)

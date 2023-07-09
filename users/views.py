from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import CustomUser, PasswordEntry
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def LoginView(request):
    if request.method == 'POST':
        identity = request.POST.get('identity')
        password = request.POST.get('password') # masterpassword
        
        if '@' in identity:
            email = identity
            username = CustomUser.objects.get(email=email).username
        else:
            username = identity
            email = CustomUser.objects.get(username=username).email
        user = authenticate(request, username=username, email=email, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('dashboard', username=username)
    return render(request, 'users/login.html')

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
    return render(request, 'users/dashboard.html', contexts)
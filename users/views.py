from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser, Passwords
from django.contrib.auth import authenticate, login


def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        emial = request.POST.get('email')
        masterpassword = request.POST.get('masterpassword')
                
        user = authenticate(username=username, password=masterpassword)
        login(request, user)
        return redirect('dashboard/?user='+username)
    return redirect('redirect')

def RegisterView(response):
    if response.method == 'POST':
        username = response.POST.get('username')
        email = response.POST.get('email')
        masterpassword = response.POST.get('masterpassword')
    
        if CustomUser.objects.filter(email=email).exists():
            return HttpResponse('User with this email already exist')
        if CustomUser.objects.filter(username=username).exists():
            return HttpResponse('User with this username already exist')
        user = CustomUser.objects.create_user(username, email, masterpassword)
        user.save()
        return redirect('login')
    return render(response, 'users/register.html')

def DashboardView(request):
    passwords = Passwords.objects.filter(user=request.user)
    contexts = {
        'passwords': passwords,
        'user': request.user,
    }
    return render(request, 'users/dashboard.html', contexts)
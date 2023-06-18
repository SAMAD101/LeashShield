from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser, Passwords
from django.contrib.auth import authenticate, login


def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get['username']
        emial = request.POST.get['email']
        masterpassword = request.POST.get['masterpassword']
                
        user = authenticate(username=username, password=masterpassword)
        if user is not None:
            login(request, user)
            return redirect('dashboard/?user='+username)
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})   
    return render(request, 'users/login.html')

def RegisterView(request):
    if request.method == 'POST':
        username = request.POST.get['username']
        email = request.POST.get['email']
        masterpassword = request.POST.get['masterpassword']
    
        if CustomUser.objects.filter(email=email).exists():
            return HttpResponse('User with this email already exist')
    
        user = CustomUser.objects.create_user(username, email, masterpassword)
        user.save()
        return redirect('login')
    return render(request, 'users/register.html')

def DashboardView(request):
    passwords = Passwords.objects.filter(user=request.user)
    contexts = {
        'passwords': passwords,
        'user': request.user,
    }
    return render(request, 'users/dashboard.html', contexts)
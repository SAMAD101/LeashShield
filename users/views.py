from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser, Passwords
from django.contrib.auth import authenticate, login


def LoginView(response):
    if response.method == 'POST':
        username = response.POST.get('username')
        email = response.POST.get('email')
        password = response.POST.get('password') # masterpassword
        user = authenticate(response, username=username, email=email, password=password)
        
        if user is not None:
            if user.is_active:
                login(response, user)
                return redirect('/user/dashboard/?username='+username)
    return render(response, 'users/login.html')

def RegisterView(response):
    if response.method == 'POST':
        username = response.POST.get('username')
        email = response.POST.get('email')
        mpassword = response.POST.get('mpassword')
        cmpassword = response.POST.get('cmpassword')
        
        if mpassword != cmpassword:
            return HttpResponse('Passwords do not match')
        if CustomUser.objects.filter(email=email).exists():
            return HttpResponse('User with this email already exist')
        if CustomUser.objects.filter(username=username).exists():
            return HttpResponse('User with this username already exist')
        user = CustomUser.objects.create_user(username=username, email=email, password=mpassword)
        user.save()
        return redirect('login')
    return render(response, 'users/register.html')

def DashboardView(request):
    user = CustomUser.objects.filter(username=request.GET.get('username'))
    passwords = [];
    for password in Passwords.objects.filter(user=user[0]):
        passwords.append(password)
    
    contexts = {
        'passwords': passwords,
        'user': request.user,
    }
    return render(request, 'users/dashboard.html', contexts)
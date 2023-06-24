from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser, Passwords
from django.contrib.auth import authenticate, login


def LoginView(response):
    if response.method == 'POST':
        identity = response.POST.get('identity')
        password = response.POST.get('password') # masterpassword
        
        if '@' in identity:
            email = identity
            username = CustomUser.objects.get(email=email).username
        else:
            username = identity
            email = CustomUser.objects.get(username=username).email
        user = authenticate(response, username=username, email=email, password=password)
        
        if user is not None:
            if user.is_active:
                login(response, user)
                return HttpResponse(user)
    return render(response, 'users/login.html')

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
            return HttpResponse('User created')
    return render(request, 'users/register.html')

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
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .modals import CustomUser
from django.contrib.auth import authenticate, login


def LoginView(request):
    if request.method == 'POST':
        username = request.GET.get['username']
        emial = request.GET.get['email']
        masterpassword = request.GET.get['masterpassword']
                
        user = authenticate(username=username, password=masterpassword)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})   
    return render(request, '#')

def RegisterView(request):
    if request.method == 'POST':
        username = request.GET.get['username']
        email = request.GET.get['email']
        masterpassword = request.GET.get['masterpassword']
        cmasterpassword = request.GET.get['cmasterpassword']
    
    if CustomUser.objects.filter(username=username).exists():
        return HttpResponse('User with this username already exist')
    elif CustomUser.objects.filter(email=email).exists():
        return HttpResponse('User with this email already exist')
    
    if(masterpassword == cmasterpassword):
        user = CustomUser.objects.create_user(username, email, masterpassword)
        user.save()
        return redirect('login')
    else:
        return HttpResponse('Password does not match')
    return render(request, '#')
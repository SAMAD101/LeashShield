from django.shortcuts import render

def HomeView(request):
    return render(request, 'home/home.html', {})

def AboutView(request):
    return render(request, 'home/about.html', {})

def PrivacyView(request):
    return render(request, 'home/privacy.html', {})
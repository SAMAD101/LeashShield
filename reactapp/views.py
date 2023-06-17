from django.shortcuts import render


def react_app(request):
    # Acts as the entry point to our web app
    return render(request, 'index.html')
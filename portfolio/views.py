from django.shortcuts import render

def index(request):
    """Vista principal de la hoja de vida"""
    return render(request, 'index.html')

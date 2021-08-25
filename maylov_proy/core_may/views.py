from django.shortcuts import render

# Create your views here.

def home (request):
    return render(request, "core_may/home.html")

def inicio (request):
    return render(request, "core_may/inicio.html")

def presente (request):
    return render(request, "core_may/presente.html")

def futuro (request):
    return render(request, "core_may/futuro.html")
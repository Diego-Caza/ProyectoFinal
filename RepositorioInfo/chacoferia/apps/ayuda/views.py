from django.shortcuts import render

# Create your views here.

def ayuda(request):
    return render(request,"ayuda/ayuda.html")

def ayudaUser(request):
    return render(request,"ayuda/usuario/ayuda.html")

def about(request):
    return render(request,"ayuda/about.html")

def aboutUser(request):
    return render(request,"ayuda/usuario/about.html")
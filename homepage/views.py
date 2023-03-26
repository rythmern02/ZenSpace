from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "homepage/index.html")

def loggedin(request):
    return render(request, "homepage/loggedin.html")
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
# Create your views here.
import ctypes  # An included library with Python install
@login_required(login_url='/')
def home(request):
    return render(request,"/")

def signin(request):
    if request.method =='POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('/loggedin')
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('/authentication')
    username = request.POST.get('username')  
    return render(request,"authentication/signin.html",{"username" : username})

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('/authentication/signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('/authentication/signup')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('/authentication/signup')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('/authentication/signup')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('/authentication/signup')
        
        my_user = User.objects.create_user(username,email,pass1)
        my_user.save()
        return redirect('/authentication')
    
    return render(request, "authentication/signup.html")


def signout(request):
    logout(request)
    return redirect('/authentication')
    
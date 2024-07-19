from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from .import models

def base(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'auth/login.html')



def log_in(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('base')
            else:
                return render(request,'auth/login.html')
        except:
            return redirect('login')
    return render(request, 'auth/login.html')

def register(request):
    if request.method == 'POST':
        try:
            f_name = request.POST.get('f_name')
            l_name = request.POST.get('l_name')
            username = request.POST.get('username')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            if password == confirm_password:
                models.User.objects.create_user(
                    username=username, 
                    password=password, 
                    first_name=f_name, 
                    last_name=l_name
                    )
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('base')
        except:
            return redirect('register')
    return render(request, 'auth/register.html')

def log_out(request):
    logout(request)
    return redirect('base')
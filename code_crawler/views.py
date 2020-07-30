from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from . import forms

@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is Incorrect')
        context = {}
        return render(request,'login.html',context)

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            form = forms.UserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('loginpage')
        context={}
        return render(request,'register.html',context)

@login_required(login_url='login')
def analytics(request):
    return render(request,'home.html')

def resetpass(request):
    return render(request,'home.html')

@login_required(login_url='login')
def contactus(request):
    return render(request,'home.html')

def developers(request):
    return render(request,'developers.html')

@login_required(login_url='login')
def logout(request):
    logout(request)
    return redirect(home)


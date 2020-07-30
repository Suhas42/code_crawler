from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from . import forms
import urllib3, json

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
        form = forms.UserForm()
        if request.method == "POST":
            form = forms.UserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        context={'form':form}
        return render(request,'register.html',context)

@login_required(login_url='login')
def analytics(request):
    context = {}
    if request.method == 'POST':
        handle = request.POST.get('handleinput')
        url = "https://codeforces.com/api/user.info?handles=" + handle
        http = urllib3.PoolManager()
        json_obj = http.request('GET',url)
        userinfo = json.loads(json_obj.data.decode('utf-8'))
        status = userinfo['status']
        if status != 'OK':
            status = False
        else:
            status = True
            userinfo = userinfo["result"]
            userinfo = userinfo[0]
            context={'userinfo':userinfo, 'status':status}

    return render(request,'analytics.html',context)

def resetpass(request):
    return render(request,'resetpass.html')

@login_required(login_url='login')
def contactus(request):
    return render(request,'contactus.html')

def developers(request):
    return render(request,'developers.html')

@login_required(login_url='login')
def logout(request):
    logout(request)
    return redirect('home')


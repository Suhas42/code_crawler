from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from . import forms
import urllib3, json

@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

def loginto(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        message = ''
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'Username or Password is Incorrect'
        context = {'message':message}
        return render(request,'login.html',context)

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        message = ''
        form = forms.UserForm()
        if request.method == "POST":
            form = forms.UserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                message = 'Account was created for ' + user
                return redirect('login')
            message = 'Account not created'
        context={'form':form,'message':message}
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

            url = "https://codeforces.com/api/user.rating?handle=" + handle
            json_obj = http.request('GET', url)
            contestgiven = json.loads(json_obj.data.decode('utf-8'))
            contests = contestgiven['result']

            url = "https://codeforces.com/api/user.status?handle=" + handle
            json_obj = http.request('GET', url)
            problems = json.loads(json_obj.data.decode('utf-8'))
            problems = problems['result']


            context = {'userinfo': userinfo, 'status': status, 'contests':contests, 'problems':problems}

    return render(request,'analytics.html',context)

def resetpass(request):
    return render(request,'resetpass.html')

@login_required(login_url='login')
def contactus(request):
    return render(request,'contactus.html')

def developers(request):
    return render(request,'developers.html')

@login_required(login_url='login')
def logoutfrom(request):
    logout(request)
    return redirect('home')


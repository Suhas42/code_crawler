"""code_crawler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calender',include('calender.urls'),name='calender'),
    path('',views.home,name='home'),
    path('login/',views.loginto, name='login'),
    path('register/',views.register, name='register'),
    path('analytics/',views.analytics, name='analytics'),
    path('logout/',views.logoutfrom, name='logout'),
    path('resetpass/',views.resetpass, name='resetpass'),
    path('contactus/',views.contactus, name='contact'),
    path('developers/',views.developers, name='developers'),
]

"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth import views
from django.views.generic import RedirectView
from django.views.static import serve
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth import views
from . import views as root_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clients.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='clients/login.html'), name='login'),
    path('logout/', auth_views.LoginView.as_view(template_name='clients/logout.html'), name='logout'),
    path('login/',views.login),
    path('built/', root_views.built),
]

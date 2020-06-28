"""hreval URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from .views import home_page
from django.conf.urls import include
from employees.views import create_page
from accounts.views import register_page, login_page, logout_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page, name='home'),
     path('register/', register_page, name="register"),
    path('login/', login_page, name="login"),
    path('logout/', logout_page, name="logout"),
    path('create/',create_page, name='create'),
    path('employees/',  include('employees.urls')),
    path('roles/',  include('roles.urls')),
    path('departments/',  include('departments.urls'))
    
]

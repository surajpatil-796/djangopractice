"""modulepractice URL Configuration

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
from django.conf.urls import include
from .views import home_page, contact_page, about_page
from blog.views import article_detail_dynamic, create_page, list_view, article_detail_update, delete_page
#============================================
from rest_framework import routers
from restapi import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', home_page),
    # path('blog/', article_detail_page),
    path('list/', list_view, name='home'),
 
     path('blog/<int:id>/', article_detail_dynamic),
     path('blog/<int:id>/update/', article_detail_update),
      path('blog/<int:id>/delete/', delete_page),
     
    path('about/', about_page),
    path('serialblog/',  include('serialblog.urls')),
    path('serialpractice/',include('serialblog.urls')),

    path('create/', create_page, name='create'),
    path('contact/', contact_page),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
]

"""
URL configuration for courseplatform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('community/', include('MyApps.community.urls')),
    #path('courses/', include('MyApps.courses.urls')),
    #path('evaluations/', include('MyApps.evaluations.urls')),
    #path('users/', include('MyApps.users.urls')),
    #path('tags/', include('MyApps.tags.urls')),
    path('api/', include('MyApps.community.urls_viewset')),
    path('api/', include('MyApps.courses.urls_viewset')),
    path('api/', include('MyApps.evaluations.urls_viewset')),
    path('api/', include('MyApps.tags.urls_viewset')),
    path('api/', include('MyApps.users.urls_viewset')),
]

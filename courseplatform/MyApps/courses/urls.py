from django.urls import path
from MyApps.courses.views import home

urlpatterns = [
    path('inicio/', home , name='home')
]
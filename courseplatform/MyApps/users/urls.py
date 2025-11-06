from django.urls import path
from MyApps.users.views import home

urlpatterns = [
    path('inicio/', home , name='home')
]
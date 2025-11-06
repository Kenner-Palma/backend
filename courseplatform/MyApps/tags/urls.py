from django.urls import path
from MyApps.tags.views import home

urlpatterns = [
    path('inicio/', home , name='home')
]
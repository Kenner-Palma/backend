from django.urls import path
from MyApps.evaluations.views import home

urlpatterns = [
    path('inicio/', home , name='home')
]
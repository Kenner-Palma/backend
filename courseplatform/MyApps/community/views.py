from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework import generics

from rest_framework import status

from MyApps.community.models import Forums
from MyApps.community.serializers import ForumsSerializer 



# Create your views here.
class ForumsList(generics.ListCreateAPIView):
    """
    Lista de Foros
    """

    queryset = Forums.objects.all()
    serializer_class = ForumsSerializer
    
class ForumsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete de los Foros por pk
    """
    queryset = Forums.objects.all()
    serializer_class = ForumsSerializer

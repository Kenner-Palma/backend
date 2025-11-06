from rest_framework import viewsets
from .models import Posts, Forums
from .serializers import PostsSerializer, ForumsSerializer

class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

class ForumsViewSet(viewsets.ModelViewSet):
    queryset = Forums.objects.all()
    serializer_class = ForumsSerializer
    
    
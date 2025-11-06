from rest_framework import viewsets
from .models import Teachers, Students
from .serializers import TeachersSerializer, StudentsSerializer

class TeachersViewSet(viewsets.ModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

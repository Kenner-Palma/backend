from rest_framework import viewsets
from .models import Evaluations, Attempts, Deliveries, StudentDeliveries
from .serializers import EvaluationsSerializer, AttemptsSerializer, DelievriesSerializer, StudentsDeliveriesSerializer

class EvaluationsViewSet(viewsets.ModelViewSet):
    queryset = Evaluations.objects.all()
    serializer_class = EvaluationsSerializer

class AttemptsViewSet(viewsets.ModelViewSet):
    queryset = Attempts.objects.all()
    serializer_class = AttemptsSerializer

class DeliveriesViewSet(viewsets.ModelViewSet):
    queryset = Deliveries.objects.all()
    serializer_class = DelievriesSerializer

class StudentDeliveriesViewSet(viewsets.ModelViewSet):
    queryset = StudentDeliveries.objects.all()
    serializer_class = StudentsDeliveriesSerializer
    
    
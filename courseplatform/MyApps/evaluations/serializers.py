from rest_framework import serializers
from .models import Evaluations, Attempts, Deliveries, StudentDeliveries

class EvaluationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluations
        fields = '__all__'
        
class AttemptsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attempts
        fields = '__all__'
        
class DelievriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliveries
        fields = '__all__'
        
class StudentsDeliveriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDeliveries
        fields = '__all__'
        
        
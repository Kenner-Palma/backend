from rest_framework import serializers
from .models import Evaluations, Attempts, Deliveries, StudentDeliveries

class EvaluationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluations
        fields = '__all__'
        
    def to_representation(self, instance):
        """Convierte las fechas a formato ISO con microsegundos para Angular"""
        ret = super().to_representation(instance)

        # Verifica que las claves existan en ret
        if all(key in ret for key in ['available_from', 'available_until', 'limit_date']):
            
            # Verifica que no sean None
            if instance.available_from and instance.available_until and instance.limit_date:
                ret['available_from'] = instance.available_from.isoformat()
                ret['available_until'] = instance.available_until.isoformat()
                ret['limit_date'] = instance.limit_date.isoformat()

        return ret

class AttemptsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attempts
        fields = '__all__'
        
    def to_representation(self, instance):
        """Convierte las fechas a formato ISO con microsegundos para Angular"""
        ret = super().to_representation(instance)

        # Verifica que las claves existan en ret
        if all(key in ret for key in ['attempt_date', 'start_date', 'end_time']):
            
            # Verifica que no sean None
            if instance.attempt_date and instance.start_date and instance.end_time:
                ret['attempt_date'] = instance.attempt_date.isoformat()
                ret['start_date'] = instance.start_date.isoformat()
                ret['end_time'] = instance.end_time.isoformat()

        return ret
        
class DelievriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliveries
        fields = '__all__'
        
    def to_representation(self, instance):
        """Convierte las fechas a formato ISO con microsegundos para Angular"""
        ret = super().to_representation(instance)

        # Verifica que las claves existan en ret
        if all(key in ret for key in ['limit_date']):
            
            # Verifica que no sean None
            if instance.limit_date:
                ret['limit_date'] = instance.limit_date.isoformat()

        return ret
        
class StudentsDeliveriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDeliveries
        fields = '__all__'
        
    def to_representation(self, instance):
        """Convierte las fechas a formato ISO con microsegundos para Angular"""
        ret = super().to_representation(instance)

        # Verifica que las claves existan en ret
        if all(key in ret for key in ['delivery_date']):
            
            # Verifica que no sean None
            if instance.delivery_date :
                ret['delivery_date'] = instance.delivery_date.isoformat()
                

        return ret
        
        
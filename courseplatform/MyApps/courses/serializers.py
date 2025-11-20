from rest_framework import serializers
from .models import Courses, Modules, Lessons, Registrations

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'
        
class ModulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modules
        fields = '__all__'
        
class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = '__all__'
        
class RegistrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registrations
        fields = '__all__'
    
    def to_representation(self, instance):
        """Convierte la fecha a formato ISO con microsegundos para Angular"""
        ret = super().to_representation(instance)
        if 'registration_date' in ret and ret['registration_date']:
            # Convierte a formato ISO: YYYY-MM-DDTHH:mm:ss.sssZ
            ret['registration_date'] = instance.registration_date.isoformat()
        return ret
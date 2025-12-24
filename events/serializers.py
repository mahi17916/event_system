from rest_framework import serializers
from .models import events, Registration

class eventSerializer(serializers.ModelSerializer):
    class Meta:
        model = events
        fields = 'all'
        
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration 
        fields = 'all'
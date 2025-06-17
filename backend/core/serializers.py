from rest_framework import serializers
from .models import DisasterEvent

class DisasterEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisasterEvent
        fields = '__all__'
from rest_framework import serializers
from .models import Proximity


class ProximitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Proximity
        fields = ['id', 'distance', 'timestamp']

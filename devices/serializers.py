from .models import Controller
from rest_framework import serializers
from django.utils import timezone
from .models import Controller, Proximity, Sensor



# The choice between ModelSerializer and HyperlinkedModelSerializer depends on your API design and requirements. If you want to provide hyperlinks to represent relationships between models and improve API discoverability, HyperlinkedModelSerializer is a good choice. If you prefer a more straightforward representation of relationships using nested data or primary keys, ModelSerializer is a better fit.


class ControllerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Controller
        fields = ['type', 'model', 'network_address', 'chip_id', 'created_at']


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'sensor', 'model', 'chip_id']

    def to_representation(self, instance):
        return f'{instance.model}: {instance.chip_id}'


class ProximitySerializer(serializers.HyperlinkedModelSerializer):
    sensor = SensorSerializer(read_only=True)
    class Meta:
        model = Proximity
        # fields = ['id', 'sensor', 'sensor_chip_id', 'distance', 'timestamp']
        fields = ['id', 'sensor', 'distance', 'timestamp']
    

class ProximityUpdateSerializer(serializers.ModelSerializer):
    sensor = SensorSerializer(read_only=True)
    class Meta:
        model = Proximity
        fields = ['sensor', 'distance', 'timestamp']

    
    def validate_distance(self, value):
        """
        Validate the 'distance' field.
        """
        value = int(value)
        if value < 0:
            raise serializers.ValidationError(
                "Distance can not be less than 0cm.")
        elif value > 30:
            raise serializers.ValidationError(
                "Distance must be less or equal to 30 cm.")
        else:
            return value
    
    # def validate(self, attrs):
        #     """
        #     Validate the entire serializer data.
        #     """
        #     # Perform additional validation logic here
        #     # Access and validate multiple fields if needed

        #     return attrs
    
    def clean(self, data):
        data['chip_id'] = data.get('chip_id', '').strip()
        data['distance'] = data.get('distance', '').strip()
        return data

    def update(self, instance, validated_data):
        # Update the 'distance' field
        instance.distance = validated_data.get('distance', instance.distance)

        # Update the 'timestamp' field
        instance.timestamp = timezone.now()

        # Save the updated instance
        instance.save()

        return instance

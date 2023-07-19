from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import check_password
from .models import Controller, Proximity, Sensor


# The choice between ModelSerializer and HyperlinkedModelSerializer depends on your API design and requirements. If you want to provide hyperlinks to represent relationships between models and improve API discoverability, HyperlinkedModelSerializer is a good choice. If you prefer a more straightforward representation of relationships using nested data or primary keys, ModelSerializer is a better fit.


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'model', 'chip_id']

    def to_representation(self, instance):
        return f'{instance.model}: {instance.chip_id}'


class ProximitySerializer(serializers.HyperlinkedModelSerializer):
    sensor = SensorSerializer(read_only=True)
    sensor_chip_id = serializers.CharField(write_only=True)
    class Meta:
        model = Proximity
        fields = ['id', 'sensor', 'sensor_chip_id', 'distance', 'timestamp']

    def validate_distance(self, value):
        """
        Validate the 'distance' field.
        """
        value = int(value)
        if value < 0:
            raise serializers.ValidationError("Distance can not be less than 0cm.")
        elif value > 30:
            raise serializers.ValidationError("Distance must be less or equal to 30 cm.")
        else:
            return value

    # def validate(self, attrs):
    #     """
    #     Validate the entire serializer data.
    #     """
    #     # Perform additional validation logic here
    #     # Access and validate multiple fields if needed

    #     return attrs
    def create(self, validated_data):
        sensor_chip_id = validated_data.pop('sensor_chip_id')
        try:
            sensor = Sensor.objects.get(chip_id=sensor_chip_id)
        except Sensor.DoesNotExist:
            raise serializers.ValidationError("Invalid sensor chip ID.")

        proximity = Proximity.objects.create(sensor=sensor, **validated_data)
        return proximity


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    chip_id = serializers.CharField()
    access_key = serializers.CharField()

    def validate(self, attrs):
        chip_id = attrs.get("chip_id")
        access_key = attrs.get("access_key")

        # Add your custom validation logic here
        try:
            controller = Controller.objects.get(
                chip_id=chip_id)
            # if access_key == controller.access_key:
            if check_password(access_key, controller.access_key):
                attrs["user"] = controller
            else:
                raise serializers.ValidationError(
                    "Invalid controller credentials.")
        except Controller.DoesNotExist:
            raise serializers.ValidationError("Controller not found.")

        return attrs

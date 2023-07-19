from rest_framework import serializers
from .models import Proximity


# The choice between ModelSerializer and HyperlinkedModelSerializer depends on your API design and requirements. If you want to provide hyperlinks to represent relationships between models and improve API discoverability, HyperlinkedModelSerializer is a good choice. If you prefer a more straightforward representation of relationships using nested data or primary keys, ModelSerializer is a better fit.

class ProximitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proximity
        fields = ['id', 'distance', 'timestamp']

    # def validate_distance(self, value):
    #     """
    #     Validate the 'distance' field.
    #     """
    #     if value <= 0:
    #         raise serializers.ValidationError("Distance must be greater than zero.")
    #     return value

    # def validate(self, attrs):
    #     """
    #     Validate the entire serializer data.
    #     """
    #     # Perform additional validation logic here
    #     # Access and validate multiple fields if needed

    #     return attrs

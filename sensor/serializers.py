from rest_framework import serializers
from .models import Proximity


# The choice between ModelSerializer and HyperlinkedModelSerializer depends on your API design and requirements. If you want to provide hyperlinks to represent relationships between models and improve API discoverability, HyperlinkedModelSerializer is a good choice. If you prefer a more straightforward representation of relationships using nested data or primary keys, ModelSerializer is a better fit.

class ProximitySerializer(serializers.HyperlinkedModelSerializer): 
    class Meta:
        model = Proximity
        fields = ['id', 'distance', 'timestamp']

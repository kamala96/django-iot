from rest_framework import generics, status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from .authentication import MicroControllerAuthentication
from .models import Controller, Proximity, Sensor
from .serializers import ProximitySerializer, ProximityUpdateSerializer

# Create your views here.


class TokenObtainPairView(TokenObtainPairView):
    pass

class ProximityListView(generics.ListAPIView):
    queryset = Proximity.objects.all().order_by('-timestamp')
    serializer_class = ProximitySerializer


# class ProximityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Proximity.objects.all()
#     serializer_class = ProximitySerializer


class ProximityRetrieveView(generics.RetrieveAPIView):
    queryset = Proximity.objects.all()
    serializer_class = ProximitySerializer


class ProximityUpdateView(generics.UpdateAPIView):
    authentication_classes = [MicroControllerAuthentication]
    queryset = Proximity.objects.all()
    serializer_class = ProximityUpdateSerializer
    http_method_names = ['patch']

    def get_object(self):
        # Get the Proximity object based on the chip_id provided in the request data
        try:
            chip_id = self.request.data.get('chip_id')
            proximity = Proximity.objects.get(sensor__chip_id=chip_id)
            return proximity
        except Proximity.DoesNotExist:
            raise serializers.ValidationError("Sensor not found.")
        except Exception as e:
            raise serializers.ValidationError(f"Error occurred: {str(e)}")
    
    def perform_update(self, serializer):
        # Validate the serializer data
        serializer.is_valid(raise_exception=True)
        serializer.save()  # Save the updated data

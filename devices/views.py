from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import IsAuthenticated
from .models import Proximity
from .serializers import ProximitySerializer

# Create your views here.


class TokenObtainPairView(TokenObtainPairView):
    pass


class HelloAPI(APIView):
    def get(self, request):
        data = {'message': 'Hello world!'}
        return Response(data)


class ProximityListCreateView(generics.ListCreateAPIView):
    queryset = Proximity.objects.all().order_by('-timestamp')
    serializer_class = ProximitySerializer


class ProximityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proximity.objects.all()
    serializer_class = ProximitySerializer

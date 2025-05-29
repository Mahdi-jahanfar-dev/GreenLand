from django.shortcuts import render
from rest_framework import viewsets
from .models import Zone, GreenLand
from .serializers import ZoneSerializer, GrenlandSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from Account.models import CustomUser




class GreenLandViewSet(viewsets.ViewSet):
    serializer_class = GrenlandSerializer
    permission_classes = [IsAuthenticated]


    def list(self, request):
        green_lands = GreenLand.objects.filter(owner = request.user.id)
        serializer = self.serializer_class(green_lands, many = True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


class ZonesViewSet(viewsets.ViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
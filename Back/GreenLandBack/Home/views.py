from django.shortcuts import render
from rest_framework import viewsets
from .models import Zone, GreenLand, SetRole
from .serializers import ZoneSerializer, GreenlandSerializer, SetRoleSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from Account.models import CustomUser
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
import openmeteo_requests
from openmeteo_sdk.Variable import Variable
from random import randint
from .weather_request_api import weather_api_request_sender





class GreenLandViewSet(viewsets.ViewSet):
    serializer_class = GreenlandSerializer
    permission_classes = [IsAuthenticated]


    def list(self, request):
        green_lands = GreenLand.objects.filter(owner = request.user.id)
        serializer = self.serializer_class(green_lands, many = True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner = request.user)
        return Response(serializer.data)

class GreenLandRetriveViewset(viewsets.ViewSet):
    serializer_class = GreenlandSerializer

    def retrieve(self, request, id):
        try:
            greenland = GreenLand.objects.get(id = id)
        except:
            return Response({'404': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        if greenland.owner == request.user:
            serializer = self.serializer_class(greenland)
            return Response(serializer.data)
        else:
            return Response({'404': 'not found'}, status=status.HTTP_404_NOT_FOUND)
    





class AddUserToGreenLand(viewsets.ViewSet):

    serializer_class = SetRoleSerializer

    def list(self, request, id):
        try:
            greenland = GreenLand.objects.get(id = id)
        except:
            return Response({'404': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if request.user == greenland.owner:
            users = SetRole.objects.filter(greenland = greenland)
            serializer = self.serializer_class(users, many = True)
            return Response(serializer.data)
        else:
            return Response({'404': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def create(self, request, id):
        try:
            greenland = GreenLand.objects.get(id = id)
        except:
            return Response({'404': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        if request.user == greenland.owner:
            serializer = SetRoleSerializer(data = request.data)
            serializer.is_valid(raise_exception=True)
            if SetRole.objects.filter(user=serializer.validated_data['user'], greenland=greenland).exists():
                return Response({'error': 'this user is already exists'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                if serializer.validated_data['user'].allow_users_add_greenlands:
                    serializer.save(greenland = greenland)
                    return Response('created', status=status.HTTP_201_CREATED)
                else:
                    return Response({'error': 'you cant add this user'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'404': 'not found'}, status=status.HTTP_404_NOT_FOUND)


class ZonesCreateViewSet(viewsets.ViewSet):

    serializer_class = ZoneSerializer
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.validated_data['greenland'].owner == request.user:
            response = weather_api_request_sender()
            data = response.data['current']
            serializer.save(temperature = data['temperature'],
                            humidity = data['humidity'],
                            solidMoisture = data['solidMoisture'],
                            latitude = data['latitude'],
                            longitude = data['longitude'],
                            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'erro': 'your not owner of this greenland'}, status=status.HTTP_400_BAD_REQUEST)
        

class ZonesDestroyViewset(viewsets.ViewSet):
        
        
        def destroy(self, request, id, pk):
            try:
                greenland = GreenLand.objects.get(id = id)
            except GreenLand.DoesNotExist:
                return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)
            
            is_owner = greenland.owner == request.user
            has_permission = False

            if not is_owner:
                try:
                    role = SetRole.objects.get(user = request.user, greenland = greenland)
                    if role.role == 'read_and_write':
                        has_permission = True
                except SetRole.DoesNotExist:
                    return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)

            if not (is_owner or has_permission):
                    return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)
            try:
                zone = Zone.objects.get(id = pk)
            except Zone.DoesNotExist:
                return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)

            if zone.greenland == greenland:
                zone.delete()
                return Response({'detail': 'deleted'}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'you cant delete this zone'}, status=status.HTTP_400_BAD_REQUEST)
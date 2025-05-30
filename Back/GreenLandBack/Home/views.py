from django.shortcuts import render
from rest_framework import viewsets
from .models import Zone, GreenLand, SetRole
from .serializers import ZoneSerializer, GreenlandSerializer, SetRoleSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from Account.models import CustomUser
from rest_framework import status




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
        return Response(serializer.data)

class GreenLandRetriveViewset(viewsets.ViewSet):
    serializer_class = GreenlandSerializer

    def retrieve(self, request, id):
        try:
            greenland = GreenLand.objects.get(id = id)
        except:
            return Response({'404': 'not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(greenland)
        return Response(serializer.data)





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
            if SetRole.objects.filter(user=serializer.validated_data['user'], greenland=greenland).exists:
                return Response({'error': 'this user is already exists'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                if serializer.validated_data['user'].allow_users_add_greenlands == True:
                    serializer.validated_data['greenland'] = greenland
                    serializer.save()
                    return Response('created', status=status.HTTP_201_CREATED)
                else:
                    return Response({'error': 'you cant add this user'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'404': 'not found'}, status=status.HTTP_404_NOT_FOUND)


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
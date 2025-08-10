from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ProfileSerilizer, UserSerializer
from .models import CustomUser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status


class UserRegisterView(APIView):
    
    model = CustomUser
    serializer_class = UserSerializer
    
    def post(self, request):
        
        serializer = self.serializer_class(data = request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'user created'}, status=status.HTTP_201_CREATED)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class UserProfile(APIView):
    model = CustomUser
    serializer_class = ProfileSerilizer

    def get(self, request, id):
        user = get_object_or_404(self.model, id = id)
        if request.user.id == user.id:
            serializer = self.serializer_class(user)
            return Response(serializer.data)
        else:
            return Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        
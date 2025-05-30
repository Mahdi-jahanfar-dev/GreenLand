from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ProfileSerilizer
from .models import CustomUser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status



class UserProfile(APIView):
    model = CustomUser
    serializer_class = ProfileSerilizer

    def get(self, request, id):
        user = get_object_or_404(self.model, id = id)
        if request.user.id == user.id:
            serializer = self.serializer_class(self.model.objects.get(id = id))
            return Response(serializer.data)
        else:
            return Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        
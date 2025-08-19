from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ProfileSerilizer, UserRegisterSerializer, UserLoginSerializer
from .models import CustomUser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema



class UserRegisterView(APIView):
    
    model = CustomUser
    serializer_class = UserRegisterSerializer
    
    @swagger_auto_schema(request_body=serializer_class)
    def post(self, request):
        
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': f'user created : {serializer.data}'}, status=status.HTTP_201_CREATED)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserLoginVIew(APIView):
    
    serializer_class = UserLoginSerializer

    @swagger_auto_schema(request_body=serializer_class)
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        
        refresh_token = RefreshToken.for_user(user)
        
        return Response ({
            "user": user.username,
            "access_token": str(refresh_token.access_token),
            "refresh_token": str(refresh_token),
            },
            status=status.HTTP_200_OK
        )
        


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
        
from rest_framework import serializers
from .models import CustomUser
from Home.serializers import GreenlandSerializer, SetRoleSerializer
from django.contrib.auth import authenticate




class ProfileSerilizer(serializers.ModelSerializer):
    green_land = GreenlandSerializer(many = True)
    role = SetRoleSerializer(many = True)
    class Meta:
        model = CustomUser
        fields = ['username', 'full_name', 'email', 'is_staff', 'is_superuser', 'allow_users_add_greenlands', 'green_land', 'role']
        read_only_fields = ['is_staff', 'is_superuser']
        
        
        
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 20, required = True, write_only = True, min_length = 8)
    password_2 = serializers.CharField(max_length = 20, required = True, write_only = True, min_length = 8)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'full_name', 'email', 'password', 'password_2']
        
    def validate(self, data):
        if data['password'] != data['password_2']:
            raise serializers.ValidationError({"password_confirmation": "Passwords do not match."})
        return data
        
    def create(self, validated_data):
        validated_data.pop('password_2')
        user = CustomUser.objects.create_user(
            username = validated_data['username'],
            full_name = validated_data['full_name'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
        
    def validate(self, data):
        
        user = authenticate(
            username = data.get("username"),
            password = data.get("password")
        )
        
        if not user:
            raise serializers.ValidationError("username or password wrong")
        
        data["user"] = user
        return data
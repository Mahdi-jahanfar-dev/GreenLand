from rest_framework import serializers
from .models import CustomUser
from Home.serializers import GreenlandSerializer, SetRoleSerializer



class ProfileSerilizer(serializers.ModelSerializer):
    green_land = GreenlandSerializer(many = True)
    role = SetRoleSerializer(many = True)
    class Meta:
        model = CustomUser
        fields = ['username', 'full_name', 'email', 'is_staff', 'is_superuser', 'allow_users_add_greenlands', 'green_land', 'role']
        read_only_fields = ['is_staff', 'is_superuser']
        
        
        
class UserSerializer(serializers.ModelSerializer):
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
            user = self.model.create_user(
                username = validated_data['username'],
                full_name = validated_data['full_name'],
                email = validated_data['email'],
                password = validated_data['password']
            )
            return user

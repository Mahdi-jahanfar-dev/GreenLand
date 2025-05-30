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
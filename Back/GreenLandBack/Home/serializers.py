from rest_framework import serializers
from .models import Zone, GreenLand, SetRole



class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ['id',
                  'greenland',
                  'name',
                  'status',
                  'temperature',
                  'humidity',
                  'light',
                  'solidMoisture',
                  'smoke',
                  'lastUpdate',
                  'image']
        read_only_fields = ['temperature', 'humidity', 'solidMoisture']
        

class GreenlandSerializer(serializers.ModelSerializer):
    zones = ZoneSerializer(many = True)

    class Meta:
        model = GreenLand
        fields = ['id','name', 'owner','zones']


class SetRoleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    greenland = serializers.SerializerMethodField()
    class Meta:
        model = SetRole
        fields = ['user', 'greenland', 'role']
        read_only_fields = ['greenland',]

    def get_user(self,obj):
        return obj.user.username
    
    def get_greenland(self,obj):
        return obj.greenland.name
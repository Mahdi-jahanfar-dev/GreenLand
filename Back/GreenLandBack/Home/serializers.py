from rest_framework import serializers
from .models import Zone, GreenLand



class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ['greenland',
                  'name',
                  'status',
                  'temperature',
                  'humidity',
                  'light',
                  'solidMoisture',
                  'smoke',
                  'lastUpdate',
                  'image']
        

class GrenlandSerializer(serializers.ModelSerializer):
    class Meta:
        model = GreenLand
        fields = ['name', 'owner']
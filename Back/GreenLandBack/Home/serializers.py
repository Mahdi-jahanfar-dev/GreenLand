from rest_framework import serializers
from .models import Zone



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
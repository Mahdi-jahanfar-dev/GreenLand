from django.db import models
from .choices import ZoneStatus, UserRole
from Account.models import CustomUser



class GreenLand(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE ,related_name='green_land')

    def __str__(self):
        return self.name

class SetRole(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='role')
    greenland = models.ForeignKey(GreenLand, on_delete=models.CASCADE)
    role = models.CharField(choices=UserRole.choices)

    def __str__(self):
        return f'{self.user} - {self.role} - {self.greenland}'

class Zone(models.Model):
    greenland = models.ForeignKey(GreenLand, on_delete=models.CASCADE, related_name='zones')
    name = models.CharField(max_length=200)
    status = models.CharField(choices=ZoneStatus.choices)
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    light = models.IntegerField()
    solidMoisture = models.IntegerField()
    smoke = models.CharField(choices=ZoneStatus)
    lastUpdate = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.name
    
class ZoneUpdate(models.Model):
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    solidMoisture = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.zone} - {self.time}"

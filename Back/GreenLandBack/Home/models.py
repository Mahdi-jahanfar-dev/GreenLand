from django.db import models
from .choices import ZoneStatus, UserRole
from Account.models import CustomUser



class GreenLand(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE ,related_name='green_land')

    def __str__(self):
        return self.name

class SetRole(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    greenland = models.ForeignKey(GreenLand, on_delete=models.CASCADE)
    role = models.CharField(choices=UserRole.choices)

class Zone(models.Model):
    greenland = models.ForeignKey(GreenLand, on_delete=models.CASCADE, related_name='zones')
    name = models.CharField(max_length=200)
    status = models.CharField(choices=ZoneStatus.choices)
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    light = models.IntegerField()
    solidMoisture = models.IntegerField()
    smoke = models.IntegerField(choices=ZoneStatus)
    lastUpdate = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()


    def __str__(self):
        return self.name
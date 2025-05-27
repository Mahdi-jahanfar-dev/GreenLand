from django.db import models


class ZoneStatus(models.IntegerChoices):
    good = 1
    normal = 2
    bad = 3


class Zone(models.Model):
    name = models.CharField(max_length=200)
    status = models.IntegerField(choices=ZoneStatus.choices)
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    light = models.IntegerField()
    solidMoisture = models.IntegerField()
    smoke = models.IntegerField(choices=ZoneStatus)
    lastUpdate = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()


    def __str__(self):
        return self.name
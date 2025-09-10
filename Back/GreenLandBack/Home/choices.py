from django.db import models


# text choice for choose status of zones
class ZoneStatus(models.TextChoices):
    good = 'good', 'good'
    normal = 'normal', 'normal'
    bad = 'bad', 'bad'


# text choice for choose user role in greenlands
class UserRole(models.TextChoices):
    read_and_write = 'read_and_write', 'read_and_write'
    read_only = 'read_only', 'read_only'
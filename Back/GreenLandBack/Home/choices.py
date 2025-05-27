from django.db import models


class ZoneStatus(models.IntegerChoices):
    good = 1
    normal = 2
    bad = 3

class UserRole(models.IntegerChoices):
    read_and_write = 1
    read_only = 2
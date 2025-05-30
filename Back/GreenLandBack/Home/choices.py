from django.db import models


class ZoneStatus(models.TextChoices):
    good = 'good', 'good'
    normal = 'normal', 'normal'
    bad = 'bad', 'bad'

class UserRole(models.TextChoices):
    read_and_write = 'read_and_write', 'read_and_write'
    read_only = 'read_only', 'read_only'
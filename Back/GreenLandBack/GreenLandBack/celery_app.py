import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GreenLandBack.settings')

app = Celery('greenland_celery')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
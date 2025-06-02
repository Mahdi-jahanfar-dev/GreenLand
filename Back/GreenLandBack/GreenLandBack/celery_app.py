import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GreenLandBack.settings')

app = Celery('GreenLandBack')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'refresh-zone-data-every-10-seconds': {
        'task': 'Home.tasks.refresh_data',
        'schedule': crontab(minute=0),
        # 'args': (), # if you have args use this
    },
}
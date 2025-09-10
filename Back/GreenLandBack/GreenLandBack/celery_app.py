import os
from celery import Celery
from celery.schedules import crontab, schedule


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GreenLandBack.settings')

# celery app instance
app = Celery('GreenLandBack')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# celery beat config
app.conf.beat_schedule = {
    'refresh-zone-data-every-1-day': {
        'task': 'Home.tasks.refresh_data',
        'schedule': crontab(minute=0),
        # 'args': (), # if you have args use this
    },
    
    'checking-updated-zone-data':{
        'task': 'Home.tasks.cheking_zone_updated_data',
        'schedule': crontab(minute=0),
    },
}
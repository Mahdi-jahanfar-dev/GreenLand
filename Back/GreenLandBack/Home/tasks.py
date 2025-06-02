from GreenLandBack.celery_app import app
from .models import Zone
from .weather_request_api import weather_api_request_sender


@app.task()
def refresh_data():
    zones = Zone.objects.all()
    for zone in zones:
        latitude = zone.latitude
        longitude = zone.longitude
        response = weather_api_request_sender(latitude, longitude)
        data = response.data['current']
        zone.temperature = data['temperature']
        zone.humidity = data['humidity']
        zone.solidMoisture = data['solidMoisture']
        zone.save()
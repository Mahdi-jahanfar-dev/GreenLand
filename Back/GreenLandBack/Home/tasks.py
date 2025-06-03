from GreenLandBack.celery_app import app
from .models import Zone, ZoneUpdate
from .weather_request_api import weather_api_request_sender


@app.task()
def refresh_data():
    zones = Zone.objects.all()
    for zone in zones:
        latitude = zone.latitude
        longitude = zone.longitude
        response = weather_api_request_sender(latitude, longitude)
        data = response.data['current']
        if zone.temperature != data['temperature'] or zone.humidity != data['humidity'] or zone.solidMoisture != data['solidMoisture']:
            ZoneUpdate.objects.create(zone=zone,
                                      temperature=data['temperature'],
                                      humidity=data['humidity'], solidMoisture=data['solidMoisture']
                                      )
        zone.temperature = data['temperature']
        zone.humidity = data['humidity']
        zone.solidMoisture = data['solidMoisture']
        zone.save()
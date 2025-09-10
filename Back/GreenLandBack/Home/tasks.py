from GreenLandBack.celery_app import app
from .models import Zone, ZoneUpdate
from .weather_request_api import weather_api_request_sender
from datetime import datetime, timedelta
from channels.layers import get_channel_layer
import asyncio
import json



# Celery task for refreshing data at a specified interval
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
            changed = True
        zone.temperature = data['temperature']
        zone.humidity = data['humidity']
        zone.solidMoisture = data['solidMoisture']
        zone.save()

        if changed:
            channel_layer = get_channel_layer()
            group_name = f'greenland_{Zone.greenland.id}'
            async def sent_update_to_websocket():
                await channel_layer.group_send(
                        group_name,
                        {
                            'type': 'send_update',
                            'message': json.dumps({
                                "temperature": data['temperature'],
                                "humidity": data['humidity'],
                                "solidMoisture": data['solidMoisture'],
                            })
                        }
                        )
            asyncio.run(sent_update_to_websocket())


# If data is older than 7 days, it will be deleted
@app.task()
def cheking_zone_updated_data():
    zone_updates = ZoneUpdate.objects.all()
    now = datetime.now()
    seven_days_ago = now - timedelta(days=7)
    for item in zone_updates:
        if item.time == seven_days_ago:
            item.delete()
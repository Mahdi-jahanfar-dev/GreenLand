import openmeteo_requests
from openmeteo_sdk.Variable import Variable
from rest_framework.response import Response
from random import randint


def weather_api_request_sender():

    om = openmeteo_requests.Client()

    latitude = randint(10, 70)
    longitude = randint(10, 70)

    params_1 = {
        "latitude": latitude,
        "longitude": longitude,
        "current": ["temperature_2m", "relative_humidity_2m"]
    }
    params_2 = {
        "latitude": latitude,
        "longitude": longitude,
        "current": ["pm2_5", "pm10", "european_aqi"]
    }


    responses_1 = om.weather_api("https://api.open-meteo.com/v1/forecast", params=params_1)
    response_1 = responses_1[0]
    current_1 = response_1.Current()

    responses_2 = om.weather_api("https://air-quality-api.open-meteo.com/v1/air-quality", params=params_2)
    response_2 = responses_2[0]
    current_2 = response_2.Current()
    

    current_data = {
        "temperature": int(current_1.Variables(0).Value()),
        "humidity": int(current_1.Variables(1).Value()),
        "solidMoisture": int(current_2.Variables(0).Value()),
        "smoke": int(current_2.Variables(1).Value()),

    }

    return Response({
        "current": current_data
    })
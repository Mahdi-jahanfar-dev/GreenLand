from django.test import TestCase
from rest_framework.test import APITestCase
from Home.weather_request_api import weather_api_request_sender


# test for open weather api request sender function
class OpenWeatherApiTest(APITestCase):
    
    def test_request(self):
        response = weather_api_request_sender()
        self.assertEqual(response.status_code, 200)
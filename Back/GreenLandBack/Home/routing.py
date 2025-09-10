from django.urls import re_path
from . import consumers

# websocket urls
websocket_urlpatterns = [
        re_path(r'ws/greenhouse/(?P<greenland_id>\d+)/$', consumers.GreenLandConsumer.as_asgi()),
]
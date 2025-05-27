from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ZonesViewSet


router = DefaultRouter()

router.register('zones', ZonesViewSet, basename='zones-url')


urlpatterns = [
    
]

urlpatterns += router.urls
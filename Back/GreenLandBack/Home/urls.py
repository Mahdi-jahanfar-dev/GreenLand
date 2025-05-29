from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()




urlpatterns = [
    path('zones/', views.ZonesViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('greenlands/', views.GreenLandViewSet.as_view({'get': 'list', 'post': 'create'}))
]

urlpatterns += router.urls
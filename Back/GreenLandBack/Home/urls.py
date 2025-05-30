from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()




urlpatterns = [
    path('zones/', views.ZonesViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('greenlands/', views.GreenLandViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('greenland/<int:id>/', views.GreenLandRetriveViewset.as_view({'get': 'retrieve'})),
    path('greenland/set-role/<int:id>/', views.AddUserToGreenLand.as_view({'get': 'list', 'post': 'create'})),
]

urlpatterns += router.urls
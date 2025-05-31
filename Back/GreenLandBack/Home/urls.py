from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()




urlpatterns = [
    path('zones/', views.ZonesCreateViewSet.as_view({'post': 'create'})),
    path('zones/delete/<int:id>/<int:pk>/', views.ZonesDestroyViewset.as_view({'delete': 'destroy'})),
    path('greenlands/', views.GreenLandViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('greenland/<int:id>/', views.GreenLandRetriveViewset.as_view({'get': 'retrieve', 'post': 'create'})),
    path('greenland/set-role/<int:id>/', views.AddUserToGreenLand.as_view({'get': 'list', 'post': 'create'})),
    path('weather/', views.test_weather_api, name='weather')
]

urlpatterns += router.urls
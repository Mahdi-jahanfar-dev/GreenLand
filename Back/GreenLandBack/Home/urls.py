from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()



# project home app urls
urlpatterns = [
    path('zones/', views.ZonesCreateViewSet.as_view({'post': 'create'})),
    path('zones/<int:id>/', views.ZonesDestroyViewset.as_view({'delete': 'destroy'})),
    path('greenlands/', views.GreenLandViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('greenland/<int:id>/', views.GreenLandRetriveViewset.as_view({'get': 'retrieve', 'post': 'create'})),
    path('greenland/set-role/<int:id>/', views.AddUserToGreenLand.as_view({'get': 'list', 'post': 'create'})),
]

urlpatterns += router.urls
from django.urls import path
from .views import UserProfile


urlpatterns = [
    path('profile/<int:id>/', UserProfile.as_view(), name='profile')
]
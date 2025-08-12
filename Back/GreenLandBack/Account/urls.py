from django.urls import path
from . import views


urlpatterns = [
    path('profile/<int:id>/', views.UserProfile.as_view(), name='profile'),
    path('register/', views.UserRegisterView.as_view(), name='register')
]
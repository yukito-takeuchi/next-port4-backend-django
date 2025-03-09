from django.urls import path
from rest_framework import routers
from .views import DeviceAPIView 

router = routers.DefaultRouter()
router.register(r'device', DeviceAPIView)


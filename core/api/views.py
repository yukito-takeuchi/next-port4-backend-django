
# Import necessary modules
from django.shortcuts import render
from rest_framework import viewsets
from ..models import Post
from .serializers import DeviceSerializer


class DeviceAPIView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = DeviceSerializer

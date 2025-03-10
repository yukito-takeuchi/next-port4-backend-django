
# Import necessary modules
from django.shortcuts import render
from rest_framework import viewsets
from ..models import Post
from .serializers import DeviceSerializer
from rest_framework.views import APIView 

from rest_framework.response import Response
from rest_framework import status

class DeviceAPIView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = DeviceSerializer

class UserCreateView(APIView):
    def post(self, request):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # モデルインスタンスを保存
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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







    def delete(self, request, pk):
        try:
            user = Post.objects.get(pk=pk)
            user.delete()
            return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Post.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
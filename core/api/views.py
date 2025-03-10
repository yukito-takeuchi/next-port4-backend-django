
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

class UserUpdateView(APIView):
    def put(self, request, pk):
        try:
            user = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = DeviceSerializer(user, data=request.data)  # 既存のインスタンスを渡す
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserDeleteView(APIView):
    def delete(self, request, pk):
        try:
            user = Post.objects.get(pk=pk)
            user.delete()
            return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Post.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
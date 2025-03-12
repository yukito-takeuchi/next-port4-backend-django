from rest_framework import serializers
from ..models import Post, Job

# class DeviceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post 
#         fields = ['id', 'title', 'content']

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'spot', 'rank', 'acucess', 'fun', 'many', 'view']
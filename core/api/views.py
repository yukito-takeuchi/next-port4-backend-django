from django.shortcuts import get_object_or_404
from rest_framework import status, views
from rest_framework.response import Response
from .serializers import DeviceSerializer

from ..models import Post


class TaskCreateListAPIView(views.APIView):
  """ Taskモデルの登録API """
  def post(self, request, *args, **kwargs):
    # Serializerを作成
    serializer = DeviceSerializer(data=request.data)
    # バリデーション実行
    serializer.is_valid(raise_exception=True)
    # モデルオブジェクトを登録
    serializer.save()
    # JSON文字列をレスポンスとして返す
    return Response(serializer.data, status.HTTP_201_CREATED)

  def get(self, request, *args, **kwargs):
    """ Taskモデルの一覧取得API """
    # 複数のobjectの場合、many=Trueを指定します
    serializer = DeviceSerializer(instance=Post.objects.all(), many=True)
    return Response(serializer.data, status.HTTP_200_OK)

class TaskRetrieveUpdataDestroyAPIView(views.APIView):
  """ Taskモデルのpk APIクラス """

  def get(self, request, pk, *args, **kwargs):
    """ Taskモデルの詳細取得API """
    # モデルオブジェクトを取得
    task = get_object_or_404(Post, pk=pk)
    serializer = DeviceSerializer(instance=task)
    return Response(serializer.data, status.HTTP_200_OK)

  def put(self, request, pk, *args, **kwargs):
    """ Taskモデルの更新API """
    task = get_object_or_404(Post, pk=pk)
    serializer = DeviceSerializer(instance=task, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status.HTTP_200_OK)

  def patch(self, request, pk, *args, **kwargs):
    """ Taskモデルの更新API """
    task = get_object_or_404(Post, pk=pk)
    # partial=Trueにより、request.dataで指定したデータのみ更新される
    serializer = DeviceSerializer(instance=task, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status.HTTP_200_OK)

  def delete(self, request, pk, *args, **kwargs):
    """ Taskモデルの削除API """
    task = get_object_or_404(Post, pk=pk)
    task.delete()
    return Response(status.HTTP_200_OK)
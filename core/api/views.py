from django.shortcuts import get_object_or_404
from rest_framework import status, views
from rest_framework.response import Response
from .serializers import DeviceSerializer

from ..models import Post, Job
import requests
from bs4 import BeautifulSoup
import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


class TaskCreateListAPIView(views.APIView):
  """ Taskモデルの登録API """
  def get(self, request, *args, **kwargs):
     """ Taskモデルの一覧取得API """
     # 複数のobjectの場合、many=Trueを指定します
     jobs = scrape_and_save()
    #  serializer = DeviceSerializer(instance=Job.objects.all(), many=True)
     return Response(jobs, status.HTTP_200_OK)
  
  def post(self, request, *args, **kwargs):
    # JSON文字列をレスポンスとして返す
    serializer = DeviceSerializer(data=request.data)
    # バリデーション実行
    serializer.is_valid(raise_exception=True)
    # モデルオブジェクトを登録
    serializer.save()
    # JSON文字列をレスポンスとして返す
    return Response(serializer.data, status.HTTP_201_CREATED)




@csrf_exempt
def scrape_and_api(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        try:
            jobs = scrape(url)
            data = {'jobs': jobs}
            return JsonResponse(data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
            return JsonResponse({'error': 'POSTリクエストのみ受け付けます'}, status=405)

class TaskRetrieveUpdataDestroyAPIView(views.APIView):
  """ Taskモデルのpk APIクラス """

  def get(self, request, pk, *args, **kwargs):
    """ Taskモデルの詳細取得API """
    # モデルオブジェクトを取得
    task = get_object_or_404(Job, pk=pk)
    serializer = DeviceSerializer(instance=task)
    return Response(serializer.data, status.HTTP_200_OK)

  def put(self, request, pk, *args, **kwargs):
    """ Taskモデルの更新API """
    task = get_object_or_404(Job, pk=pk)
    serializer = DeviceSerializer(instance=task, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status.HTTP_200_OK)

  def patch(self, request, pk, *args, **kwargs):
    """ Taskモデルの更新API """
    task = get_object_or_404(Job, pk=pk)
    # partial=Trueにより、request.dataで指定したデータのみ更新される
    serializer = DeviceSerializer(instance=task, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status.HTTP_200_OK)

  def delete(self, request, pk, *args, **kwargs):
    """ Taskモデルの削除API """
    task = get_object_or_404(Job, pk=pk)
    task.delete()
    return Response(status.HTTP_200_OK)
  

def scrape_and_save():
    amazonURL = 'https://scraping-for-beginner.herokuapp.com/ranking/'

    amazonPage = requests.get(amazonURL)
    soup = BeautifulSoup(amazonPage.text, "html.parser")
    data = []
    spots = soup.find_all('div', class_='u_areaListRankingBox row')
    # get_a = content.find_all('a')
    for spot in spots:
        spot_name = spot.find(class_='u_title col s12')
        spot_name.find('span').extract()
        spot_name = spot_name.text.replace('\n','')
        rank = float(spot.find(class_='evaluateNumber').text )


        categoryItems = spot.find(class_='u_categoryTipsItem col s12')
        categoryItems = categoryItems.find_all('dl')

        details = {}
        for categoryItem in categoryItems:
            rank = float(categoryItem.dd.text)
            category = categoryItem.dt.text
            details[category] = rank

        detum = details
        detum['観光地名'] = spot_name
        detum['評点'] = rank
        data.append(detum)
        # print(details['楽しさ'])
        # jobs = Job.objects.create(spot = detum['観光地名'], rank = detum['評点'], acucess = detum['アクセス'], fun = detum['楽しさ'], many = detum['人混みの多さ'], view = detum['景色'])
 
    return data
    # print(data[0]['楽しさ'])

def scrape(url):
    amazonURL = url

    amazonPage = requests.get(amazonURL)
    soup = BeautifulSoup(amazonPage.text, "html.parser")
    data = []
    spots = soup.find_all('div', class_='u_areaListRankingBox row')
    # get_a = content.find_all('a')
    for spot in spots:
        spot_name = spot.find(class_='u_title col s12')
        spot_name.find('span').extract()
        spot_name = spot_name.text.replace('\n','')
        rank = float(spot.find(class_='evaluateNumber').text )


        categoryItems = spot.find(class_='u_categoryTipsItem col s12')
        categoryItems = categoryItems.find_all('dl')

        details = {}
        for categoryItem in categoryItems:
            rank = float(categoryItem.dd.text)
            category = categoryItem.dt.text
            details[category] = rank

        detum = details
        detum['観光地名'] = spot_name
        detum['評点'] = rank
        data.append(detum)
        # print(details['楽しさ'])
        # jobs = Job.objects.create(spot = detum['観光地名'], rank = detum['評点'], acucess = detum['アクセス'], fun = detum['楽しさ'], many = detum['人混みの多さ'], view = detum['景色'])
 
    return data
    # print(data[0]['楽しさ'])


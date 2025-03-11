import requests
from bs4 import BeautifulSoup
amazonURL = 'https://www.wantedly.com/projects?new=true&page=1&occupationTypes=jp__engineering&hiringTypes=internship&areas=kyoto&order=mixed'
import time

# from core.api.serializers import DeviceSerializer











def amazonTrackingPrice():
    amazonPage = requests.get(amazonURL)
    soup = BeautifulSoup(amazonPage.content, "html.parser")
    # print(soup)

    title = soup.find('p', class_="ProjectListJobPostsLaptop__ProjectCount-sc-79m74y-2 cdJpsZ wui-reset wui-text wui-text-subhead").get_text()
    # price = soup.find("p", class_="styles_price__OKzE5").get_text()
    convertedPrice = title[3:5]
    # intPrice = int(convertedPrice)
    print(convertedPrice)
    # serializer = DeviceSerializer(title=convertedPrice, content= 'test')
    # # バリデーション実行
    # serializer.is_valid(raise_exception=True)
    # # モデルオブジェクトを登録
    # serializer.save()





amazonTrackingPrice()
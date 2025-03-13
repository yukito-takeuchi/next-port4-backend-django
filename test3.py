import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_and_save():
    amazonURL = 'https://www.wantedly.com/projects?new=true&page=1&occupationTypes=jp__engineering&hiringTypes=internship&areas=kyoto&order=mixed'

    amazonPage = requests.get(amazonURL)
    soup = BeautifulSoup(amazonPage.text, "html.parser")
    data = []
    spots = soup.find_all('div', class_='u_areaListRankingBox row')
    # get_a = content.find_all('a')



    # 共通レイアウトここまで
    # 個別レイアウトここから
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
 
    # return data
    # print(data[0]['楽しさ'])
    print(data[0])

scrape_and_save()
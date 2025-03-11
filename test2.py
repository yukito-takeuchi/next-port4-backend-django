import requests
from bs4 import BeautifulSoup
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
    # print(spot_name)
    eval_num = float(spot.find(class_='evaluateNumber').text )
    # print(eval_num)

    categoryItems = spot.find(class_='u_categoryTipsItem col s12')
    categoryItems = categoryItems.find_all('dl')

    # categoryItem = categoryItems[0]
    # rank = categoryItem.dd.text
    # print(rank)
    # category = categoryItem.dt.text
    # print(category)

    details = {}
    for categoryItem in categoryItems:
        rank = float(categoryItem.dd.text)
        category = categoryItem.dt.text
        details[category] = rank

    detum = details 
    detum['観光地名'] = spot_name
    detum['評点'] = eval_num
    data.append(detum)

print(data)
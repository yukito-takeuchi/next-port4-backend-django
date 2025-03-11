import requests
from bs4 import BeautifulSoup
amazonURL = 'https://scraping-for-beginner.herokuapp.com/ranking/'

amazonPage = requests.get(amazonURL)
soup = BeautifulSoup(amazonPage.text, "html.parser")

content = soup.find_all('div', class_='u_areaListRankingBox row')
# get_a = content.find_all('a')
spot = content[0]
# print(spot)

eval_num = spot.find('span', class_='evaluateNumber').text
# print(eval_num)

categoryItems = spot.find(class_='u_categoryTipsItem col s12')
categoryItems = categoryItems.find_all('dl')
categoryItem = categoryItems[0]
# print(categoryItem)
rank = categoryItem.dd.text
print(rank)
category = categoryItem.dt.text
print(category)


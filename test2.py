import requests
from bs4 import BeautifulSoup
amazonURL = 'https://scraping-for-beginner.herokuapp.com/ranking/'

amazonPage = requests.get(amazonURL)
soup = BeautifulSoup(amazonPage.text, "html.parser")

content = soup.find_all('div', class_='u_areaListRankingBox row')
# get_a = content.find_all('a')
print(content[0])


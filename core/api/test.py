import requests
from bs4 import BeautifulSoup
amazonURL = 'https://www.wantedly.com/projects?new=true&page=1&occupationTypes=jp__engineering&hiringTypes=internship&areas=kyoto&order=mixed'
import time












def amazonTrackingPrice():
    amazonPage = requests.get(amazonURL)
    soup = BeautifulSoup(amazonPage.content, "html.parser")
    print(soup)

    # title = soup.find('p', class_="styles_name__u228e").get_text()
    # price = soup.find("p", class_="styles_price__OKzE5").get_text()
    # convertedPrice = price[0:5].replace(",", "")
    # intPrice = int(convertedPrice)
    # print(title)
    # print(price)
    # print(convertedPrice)

amazonTrackingPrice()
import requests
from bs4 import BeautifulSoup
import pandas as pd

from core.models import Job 

def scrape_and_save():
    url = "https://example.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    items = soup.find_all("div", class_="item")
    for item in items:
        title = item.find("h2").text
        price = float(item.find("span").text.replace("¥", ""))
        item_url = item.find("a")["href"]

        Job.objects.create(title=title, price=price, url=item_url)
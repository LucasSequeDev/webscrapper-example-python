# Scrapper para obtener el precio de la playadito

import requests
from bs4 import BeautifulSoup

URL = "https://www.cotodigital3.com.ar/sitios/cdigi/producto/-yerba-mate-suave-playadito-500-gr/_/A-00502007-00502007-200"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

priceRaw = soup.find(class_="atg_store_newPrice")

priceRawList = priceRaw.text.strip().split('\n')

price = priceRawList[-1].split('$')[1].replace(',','.')

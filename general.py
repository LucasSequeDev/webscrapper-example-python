# Scrapper para obtener el precio de la playadito

import requests
from bs4 import BeautifulSoup
import pandas as pd

URL_BASE = "https://www.cotodigital3.com.ar"
URL = "https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-almac%C3%A9n-infusiones-mate/_/N-vra9dh"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

productsContainer = soup.find(id="products")

products = productsContainer.find_all("li")

productsDB = []

for product in products:
    productName = product.find(class_="atg_store_productTitle")
    productInfoContainer = product.find(class_="product_info_container")
    producURL = productInfoContainer.find_all("a")

    priceRaw = product.find(class_="atg_store_newPrice")
    priceRawList = priceRaw.text.strip().split('\n')

    price = priceRawList[-1].split('$')[1].replace(',','.')

    productsDB.append({
        "producto": productName.text.strip().split('\n')[0].strip(),
        "url": URL_BASE + producURL[0]["href"],
        "precio": price
    })

df = pd.DataFrame(productsDB)

df.to_csv('precios.csv')


import requests
from bs4 import BeautifulSoup
def parser():
    url = "https://www.banki.ru/products/currency/usd/"
    page = requests.get(url)
    s = BeautifulSoup(page.text, "html.parser")
    usd = s.find("div", class_="currency-table__large-text").text
    usd=usd.replace(",",".")
    return float(usd)

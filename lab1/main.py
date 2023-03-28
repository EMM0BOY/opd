import requests
from bs4 import BeautifulSoup
import xlsxwriter
data = [['Название', 'Автор', 'Цена']]
def parse():
    slovo=input("введите запрос:")
    for p in range(1, 5 + 1):
        url = f"https://www.chitai-gorod.ru/search?phrase={slovo}&page={p}"
        page = requests.get(url)
        print(page.status_code)
        soup = BeautifulSoup(page.text, "html.parser")
        item_card = soup.findAll('article', class_='product-card product-card product')
        for article in item_card:
            article_nazvanie = article.find("div", class_="product-title__head").text.strip()
            article_avtor = article.find("div", class_="product-title__author").text.strip()
            try:
                article_price = article.find("div", class_="product-price__value").text.strip()
            except:
                article_price="Not Found"
            data.append([article_nazvanie, article_avtor, article_price])
def writer():
    parse()
    with xlsxwriter.Workbook('res.xlsx') as workbook:
        worksheet = workbook.add_worksheet()
        for row_num, info in enumerate(data):
            worksheet.write_row(row_num, 0, info)


































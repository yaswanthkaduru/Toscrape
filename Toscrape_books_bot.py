# Importing libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
books = []
# Loop for getting info from all 50 pages
for i in range(1, 51):
    URL = f'http://books.toscrape.com/catalogue/page-{i}.html'
    page = requests.get(URL)
    page = page.content
    soup = BeautifulSoup(page, 'html.parser')
    ol = soup.find('ol')
    articles = ol.find_all('article', class_='product_pod')
    for article in articles:
        image = article.find('img')
        title = image.attrs['alt']
        star = article.find('p')
        star = star['class'][1]
        price = article.find('p', class_='price_color').text
        price = float(price[1:])
        books.append([title, price, star])
# Defining pandas dataframe
df = pd.DataFrame(books, columns=['Title', 'Price', 'Star Rating'])
# Storing the results in a csv file
df.to_csv('books(output).csv')

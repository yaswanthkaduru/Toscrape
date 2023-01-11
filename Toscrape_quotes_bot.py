# Importing libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
quotes = []
# Loop for getting info from all 10 pages
for i in range(1, 11):
    URL = f'http://quotes.toscrape.com/page/{i}/'
    page = requests.get(URL)
    page = page.content
    soup = BeautifulSoup(page, 'html.parser')
    soup = BeautifulSoup(soup.prettify(), 'html.parser')
    all_quotes = soup.find_all(class_='quote')
    for quote in all_quotes:
        quotation = quote.find(class_='text')
        quotation = quotation.get_text(separator=" ")
        quotation = quotation.strip()
        author = quote.find(class_='author')
        bio_link = quote.find('a')
        bio_link = bio_link['href']
        full_bio_link = f'http://quotes.toscrape.com{bio_link}'
        author = author.get_text()
        author = author.strip()
        tag = quote.find('meta', class_='keywords')
        tags = tag['content']
        tags = tags.strip()
        quotes.append([quotation, author, full_bio_link, tags])
# Defining pandas dataframe
df = pd.DataFrame(quotes, columns=['Quotation', 'Author', 'Bio link', 'Tags'])
# Storing the results in a csv file
df.to_csv('quotes(output).csv')

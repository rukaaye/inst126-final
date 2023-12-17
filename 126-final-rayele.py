
##Advance topic: Web scraping. Help from YOUtube video: 
from bs4 import BeautifulSoup
import requests

# URL of the page to scrape
page_to_scrape = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

# Finding all quotes and authors
quotes = soup.findAll("span", attrs={"class": "text"})
authors = soup.findAll("small", attrs={"class": "author"})

# Printing each quote
for quote in quotes:
    print(quote.text)
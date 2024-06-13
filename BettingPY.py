from sqlite3 import Timestamp
from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime

page_to_scrape = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")


quotes = soup.findAll("span", attrs={"class":"text"})
authors = soup.findAll("small", attrs={"class":"author"})

timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
filename = f"scraped_quotes_{timestamp}.csv"

file = open("scraped_quotes_{timestamp}.csv", "w")
writer = csv.writer(file)

writer.writerow(["QUOTES", "SEPARATOR", "AUTHORS"])


for quotes, authors in zip(quotes, authors):
    print(quotes.text + " - " + authors.text)
    writer.writerow([quotes.text, authors.text])
file.close()
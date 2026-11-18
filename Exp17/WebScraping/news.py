
import requests
from bs4 import BeautifulSoup
import csv

url = "https://feeds.bbci.co.uk/news/rss.xml"

response = requests.get(url, headers={
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/rss+xml, application/xml, text/xml"
})
response.raise_for_status()

soup = BeautifulSoup(response.content, "xml")

articles = soup.find_all("item")

print("Articles found:", len(articles))

with open("news.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Headline", "Date", "Category"])

    for article in articles:
        headline = article.find("title")
        date = article.find("pubDate")
        category = article.find("category")

        title = headline.get_text(strip=True) if headline else "Not available"
        pub_date = date.get_text(strip=True) if date else "Not available"
        cat = category.get_text(strip=True) if category else "Not available"

        writer.writerow([title, pub_date, cat])

        print("Headline:", title)
        print("Date:", pub_date)
        print("Category:", cat)
        print("--------------------")

print("News data saved successfully in news.csv")

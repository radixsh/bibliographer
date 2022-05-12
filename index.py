import requests
from bs4 import BeautifulSoup
import datetime

class Citation:
    def __init__(self, article_title, url, website_title, date_accessed,
            date_published, publisher):
        self.article_title = article_title
        self.url = url
        self.website_title = website_title
        self.date_accessed = date_accessed
        self.date_published = date_published
        self.publisher = publisher

    def 

# r = requests.get('https://www.newyorker.com/culture/on-and-off-the-avenue/the-allure-of-the-nap-dress-the-look-of-gussied-up-oblivion')
r = requests.get('https://www.geeksforgeeks.org/python-web-scraping-tutorial/')
soup = BeautifulSoup(r.content, 'html.parser')
# https://stackoverflow.com/questions/36768068/get-meta-tag-content-property-with-beautifulsoup-and-python#36768533
# https://www.browserling.com/tools/html-prettify

# print("Status code: " + str(r))

article_title = soup.find("meta", property="og:title")
print("Article title: " + str(article_title))

url = soup.find("meta", property="og:url")
print("URL: " + str(url))

website_title = soup.find("meta", property="og:site_name")
print("Website title: " + str(website_title))

# https://www.w3schools.com/python/python_datetime.asp
date_accessed = datetime.datetime.now()
date_accessed = date_accessed.strftime("%B %d, %Y")
print("Date accessed: " + date_accessed)

date_published = soup.find("meta", property="article:published_time")
print("Date published: " + str(date_published))

# ask user??
publisher = input("Publisher, if you know it (this is really hard to find\
        programmatically, sorry): ")
print("Publisher: " + str(date_published))

mycitation = Citation(article_title, url, website_title, date_accessed,
        date_published, publisher)


print("1: Article title")
print("2: Website title")
print("3: Date accessed")
print("4: Date published")
print("5: Publisher")
while True:
    thing = input("Add in any information you have...")
    if (thing == 1 || thing == "Article title"): 
        article_title = input("Article title: ")
    elif (thing == 2 || thing == website_title):
        website_title = input("Website title: ")
    elif (thing == 3 || thing == "Date accessed"):
        date_accessed = input("Date accessed: ")
    elif (thing == 4 || thing ==  "Date published")
        date_published = input("Date published: ")
    elif (thing == 5 || thing == "Publisher"):
        publisher = input("Publisher: ")
    }

import requests
from bs4 import BeautifulSoup
import datetime

class Citation:
    def __init__(self, details):
        self.details = details
        # self.url = url
        # self.website_title = website_title
        # self.date_accessed = date_accessed
        # self.date_published = date_published
        # self.publisher = publisher

# r = requests.get('https://www.newyorker.com/culture/on-and-off-the-avenue/the-allure-of-the-nap-dress-the-look-of-gussied-up-oblivion')
r = requests.get('https://www.geeksforgeeks.org/python-web-scraping-tutorial/')
soup = BeautifulSoup(r.content, 'html.parser')
# https://stackoverflow.com/questions/36768068/get-meta-tag-content-property-with-beautifulsoup-and-python#36768533
# https://www.browserling.com/tools/html-prettify

# print('Status code: ' + str(r))

details = {} # dictionary of strings, mapping categories to values

article_title = soup.find('meta', property='og:title')
details['Article title'] = str(article_title)
# print('Article title: ' + details['Article title']) 

url = soup.find('meta', property='og:url')
details['URL'] = str(url)

website_title = soup.find('meta', property='og:site_name')
details['Website title'] = str(website_title)

# https://www.w3schools.com/python/python_datetime.asp
date_accessed = datetime.datetime.now()
date_accessed = date_accessed.strftime('%B %d, %Y')
details['Date accessed'] = date_accessed

date_published = soup.find('meta', property='article:published_time')
details['Date published'] = date_published

# ask user??
publisher = input('Publisher, if you know it (this is really hard to find\
        programmatically, sorry): ')
details['Publisher'] = publisher
print('Publisher: ' + details['Publisher'])

# mycitation = Citation(details)

print("0: Quit")
print("1: Article title")
print("2: Website title")
print("3: Date accessed")
print("4: Date published")
print("5: Publisher")
thing = input('Add in any information you have...')
while thing:
    thing = input('Add in any information you have...')
    if thing == 1:
        details['Article title'] = input('Article title: ')
    elif thing == 2:
        string = input('Website title: ')
        details['Website title'] = string 
    elif thing == 3:
        details['Date accessed'] = input('Date accessed: ')
    elif thing == 4:
        details['Date published'] = input('Date published: ')
    elif thing == 5:
        details['Publisher'] = input('Publisher: ')
    else:
        break

print(details)

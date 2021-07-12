import os
import sys
from requests_html import HTMLSession 
import requests

os.system(' clear ')
session = HTMLSession()
url = 'https://www.cshub.com/article'
r = session.get(url)
r.html.render(sleep=1, scrolldown=1)
articles = r.html.find('article') 
newslist = []
for item in articles:
    try:
        newsitem = item.find('h3', first=True)
        newslist.append(f"{newsitem.text}\n{newsitem.absolute_links}\n")
    except:
        pass       
print(len(newslist))          
for x in newslist:
    print(x)

url = " https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en " 
try:
    session = HTMLSession()
    response = session.get(url)
except requests.exceptions.RequestException as e:
    print(e)
r = session.get(url)
r.html.render(sleep=1, scrolldown=50)
articles = r.html.find('article') 
newslist = []
for item in articles:
    try:
        newsitem = item.find('h3', first=True)
        newslist.append(f"{newsitem.text}\n{newsitem.absolute_links}\n")
    except:
        pass        
print(len(newslist))          
for x in newslist:
    print(x)                   
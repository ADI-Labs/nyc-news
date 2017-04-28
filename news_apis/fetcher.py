import requests
import json
import gnp
import article
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

def getGoogleArticles(q):
    c = gnp.get_google_news_query(q)
    articles = c['stories']

    for i in articles:
        i['title'] = i['title'].decode("utf-8")
        i['source'] = i['source'].decode("utf-8")
        i['link'] = i['link'].decode("utf-8")
        i['content_snippet'] = i['content_snippet'].decode("utf-8")
        i['category'] = i['category']
    
    #articles = {"artcl1": "ssup", "at2": { "hey": "lol", 'l': "you"}}

    with open('/Users/salimmjahad/Desktop/tara/data.json', 'w') as fp:
        for i in articles:
            json.dump(i, fp)

getGoogleArticles("New York City")

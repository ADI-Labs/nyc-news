import requests
import json
import gnp

API_KEY = 'de1e47c2942a4547b768b538887273d4'

c = gnp.get_google_news_query()
print(c)


def url_builder(source):
    url = 'https://newsapi.org/v1/articles?source='
    url = url + source + '&apiKey=' + API_KEY
    return url


def get_google():
    r = requests.get(url_builder('google-news'))
    source = r.json()
    return source

def make_article_object(dic_article):

    t = True
    for c in dic_article:
        if dic_article[c] == None:
            t = False

    if  t:
        title = dic_article['title']
        author = dic_article['author']
        publishedAt = dic_article['publishedAt']
        description = dic_article['description']
        url = dic_article['url']

        article = Article(title, author, publishedAt, description, url)
        return article

    return None

def print_articles(source):
    if source['status'] == 'ok':
        articles = source['articles']
        for c in articles:
            print_article(c)

def print_article(article):
    t = True
    for c in article:
        if article[c] == None:
            t = False
    if t:
        print(article['title'] + '\n' +
              "By " + article['author'] + '\n' +
              'Published ' + article['publishedAt'][:10] + '\n\n' +
              article['description'] + '\n\n' +
              "URL: " + article['url'] + '\n\n\n\n'
              )


print_articles(get_google())
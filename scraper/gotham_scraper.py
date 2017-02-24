from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
'''
This thing doesnt work because gotham doesnt allow scraping (or even urllib-ing)
'''



""" Given a URL, returns a BeautifulSoup object for that page
"""

def get_soup(url):
    raw_url = urllib.request.urlopen(url)
    raw_page = raw_url.read()
    soup = BeautifulSoup(raw_page, "html.parser")
    return soup


def scrape_new_stories_URLs():
    soup = get_soup("http://www.columbia.edu/~msm2243/")

#    stories = soup.find_all("li", class_="latestnews-item catid-126 featured")

#   print(str(stories))
    print(str(soup))

scrape_new_stories_URLs()
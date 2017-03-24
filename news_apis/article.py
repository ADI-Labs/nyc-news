
""""
This class is the abstraction of an article object

The constructor takes the title, author, time of publishing, description and url

Each API fetcher will have a method to be the intermediate between this constructor
and the content of the fetched dictionary
"""

class Article:

    def __init__(self, title, author, publishedAt, description, url):

        self.title = title
        self.author = author
        self.publishedAt = publishedAt
        self.description = descript
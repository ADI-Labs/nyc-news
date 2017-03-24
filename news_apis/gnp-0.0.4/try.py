
import gnp

#b = gnp.get_google_news(gnp.EDITION_ENGLISH_US,geo='Durham, NC')
q = input("What would you like to search? ")
c = gnp.get_google_news_query(q)
print (c)


